import os
import shutil
import sys

def merge_files(folder_path, output_file):
    # Ensure the output file doesn't already exist
    if os.path.exists(output_file):
        print(f"Error: Output file '{output_file}' already exists.")
        return

    # Get a list of all files in the folder
    files = os.listdir(folder_path)

    # Open the output file in binary write mode
    with open(output_file, 'wb') as merged_file:
        for file_name in files:
            file_path = os.path.join(folder_path, file_name)
            # Check if it's a file (not a directory)
            if os.path.isfile(file_path):
                # Read each file and write its contents to the output file
                with open(file_path, 'rb') as current_file:
                    shutil.copyfileobj(current_file, merged_file)
                print(f"Merged: {file_name}")

    print(f"All files merged into '{output_file}'.")



# The starting point
if __name__ == "__main__":
    os.system('clear')
    folder_path = sys.argv[1]
    folder_name = os.path.basename(folder_path.strip("/"))
    output_file = folder_name+'.merged.log'

    merge_files(folder_path, output_file)