from const import colours
from tabulate import tabulate
import os

def clear_terminal():
    # Clear the terminal screen based on the operating system
    os.system('cls' if os.name == 'nt' else 'clear')
def get_user_input(variable):
    while True:
        try:
            return int(input(f"{colours.OKGREEN}{colours.BOLD}{variable}: {colours.ENDC}{colours.ENDC}"))
        except ValueError:
            try:
                return float(input(f"{variable}: "))
            except ValueError:
                print("Please enter int or float value")
def get_user_input_for_metro(prompt):
    while True:
        user_input = input(f"{colours.OKGREEN}{colours.BOLD}{prompt}: {colours.ENDC}{colours.ENDC}")
        if user_input in ['y', 'n', 'Y', 'N']:
            return user_input.lower() == 'y'
        else:
            print(f"{colours.FAIL}-- Invalid input: Please enter `y` or `n`{colours.ENDC}")

def calculate_hra():
    basic_received   = get_user_input("What is your total Basic Salary? ")
    da_received      = get_user_input("Amount of total DA Received? ")
    hra_received     = get_user_input("Amount of total HRA Received? ")
    actual_rent_paid = get_user_input("Amount of actual RENT paid? ")
    living_in_metro  = get_user_input_for_metro("Are you living in any metro Cities (Delhi, Mumbai, Kolkata or Chennai)? [y/n]: ")

    clear_terminal()

    print("Your input:\n")
    input_data = [
        ("Basic Received"  , format(basic_received, '.2f')),
        ("DA Received"     , format(da_received, '.2f')),
        ("HRA Received"    , format(hra_received, '.2f')),
        ("Actual Rent paid", format(actual_rent_paid, '.2f')),
        ("Living in metro" , living_in_metro)
    ]

    print(tabulate(input_data, headers=[
        f"{colours.OKGREEN}{colours.BOLD}Variable{colours.ENDC}{colours.ENDC}",
        f"{colours.OKGREEN}{colours.BOLD}Value{colours.ENDC}{colours.ENDC}"
    ], tablefmt="fancy_grid"))

    total_salary       = basic_received+da_received
    variable1          = hra_received
    variable2          = (total_salary*50/100) if living_in_metro else (total_salary*40/100)
    variable3          = actual_rent_paid - (total_salary*10/100)
    hra_tax_excemption = min(variable1, variable2, variable3)

    label2 = "50" if living_in_metro else "40"
    data = [
        (
            "1.",
            "Actual HRA Received",
            hra_received,
            format(variable1, '.2f')
        ),
        (
            "2.",
            f"{label2} of (Basic + DA)",
            f"[ ({basic_received}+{da_received})*{label2}/100 ]",
            format(variable2, '.2f')
        ),
        (
            "3.",
            "(Actual Rent paid) minus (10% of Basic + DA)",
            f"{actual_rent_paid} - (({basic_received}+{da_received})*10/100)",
            format(variable3, '.2f')
        ),
        (
            "**",
            "Lowest of (1), (2) or (3)",
            f"{colours.BOLD}Final HRA Tax Exemption{colours.ENDC}",
            f"{colours.OKBLUE}{colours.BOLD}{format(hra_tax_excemption, '.2f')}{colours.ENDC}{colours.ENDC}",
        )
    ]
    print("\nFinal Output:\n")
    print(tabulate(data, headers=[
        f"{colours.OKGREEN}{colours.BOLD}Formula{colours.ENDC}{colours.ENDC}",
        f"{colours.OKGREEN}{colours.BOLD}Calculation{colours.ENDC}{colours.ENDC}",
        f"{colours.OKGREEN}{colours.BOLD}Value{colours.ENDC}{colours.ENDC}"
    ], tablefmt="fancy_grid"))

if __name__ == "__main__":
    calculate_hra()
    # print("Completed Execution")