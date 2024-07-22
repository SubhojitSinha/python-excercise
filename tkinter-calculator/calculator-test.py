from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=20, borderwidth=0, font=('Courier', 30))
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

label = Label(root, text="0", font=('Courier', 20))
label.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

def button_click(x):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(x))

def clear_all():
    label.config(text="0")
    e.delete(0, END)

def operator_button(operator):
    global f_num
    global op

    f_num = float(e.get())
    op = operator

    label.config(text=str(f_num)+" "+str(op))
    e.delete(0, END)

def equal_button():
    global f_num
    global op

    label.config(text=str(f_num)+" "+str(op)+" "+str(float(e.get())))
    result = 0
    current = float(e.get())
    print("f_num: ",f_num)
    print("op: ", op)
    print("current: ",current)

    if op == "+":
        result = f_num + current
    elif op == "-":
        result = f_num - current
    elif op == "*":
        result = f_num * current
    elif op == "/":
        result = float(f_num / current)

    print("result: ",result)

    e.delete(0, END)
    e.insert(0, result)
    label.config(text=str(f_num)+" "+str(op)+" "+str(current)+" = "+str(result))

    f_num = 0

button_1 = Button(root, text="1", padx=40, pady=20, font=('Courier', 30), command=lambda:button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, font=('Courier', 30), command=lambda:button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, font=('Courier', 30), command=lambda:button_click(3))

button_4 = Button(root, text="4", padx=40, pady=20, font=('Courier', 30), command=lambda:button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, font=('Courier', 30), command=lambda:button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, font=('Courier', 30), command=lambda:button_click(6))

button_7 = Button(root, text="7", padx=40, pady=20, font=('Courier', 30), command=lambda:button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, font=('Courier', 30), command=lambda:button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, font=('Courier', 30), command=lambda:button_click(9))

button_0 = Button(root, text="0", padx=40, pady=20, font=('Courier', 30), command=lambda:button_click(0))
button_adds = Button(root, text="+", padx=40, pady=20, font=('Courier', 30), command=lambda:operator_button("+"))
button_subs = Button(root, text="-", padx=40, pady=20, font=('Courier', 30), command=lambda:operator_button("-"))

button_multi = Button(root, text="*", padx=40, pady=20, font=('Courier', 30), command=lambda:operator_button("*"))
button_div = Button(root, text="/", padx=40, pady=20, font=('Courier', 30), command=lambda:operator_button("/"))
button_equal = Button(root, text="=", padx=40, pady=20, font=('Courier', 30), bg="blue", fg="white", command=equal_button)

button_dot = Button(root, text=".", padx=40, pady=20, font=('Courier', 30), command=lambda:button_click("."))
button_clear = Button(root, text="Clear!", padx=80, pady=25, font=('Courier', 20), command=clear_all)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)

button_0.grid(row=5, column=0)
button_adds.grid(row=5, column=1)
button_subs.grid(row=5, column=2)

button_multi.grid(row=6, column=0)
button_div.grid(row=6, column=1)
button_equal.grid(row=6, column=2)

button_dot.grid(row=7, column=0)
button_clear.grid(row=7, column=1, columnspan=2)



root.mainloop()