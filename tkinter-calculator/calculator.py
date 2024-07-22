# from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.constants import *

# root = Tk()
# root = tb.Window(themename="minty")
root = tb.Window(themename="darkly")
# root.geometry("250x300")
# root.iconbitmap("Wineass-Ios7-Redesign-Calculator.ico")
photo = tb.PhotoImage(file = 'calc.png')
root.wm_iconphoto(False, photo)

root.resizable(False, False)
root.title("Simple Calculator")

my_style = tb.Style()
my_style.configure('primary.Outline.TButton', font=('Cambria', 20), width=5, border=1, bordercolor='#303030')
my_style.configure('info.Outline.TButton', font=('Cambria', 20), width=5, border=1, bordercolor='#303030')
my_style.configure('danger.Outline.TButton', font=('Cambria', 20), width=5, border=1, bordercolor='#303030')
my_style.configure('success.TButton', font=('Cambria', 20), width=12, border=1, bordercolor='#303030')
my_style.configure('warning.TButton', font=('Cambria', 20), width=12, border=1, bordercolor='#303030')


e = tb.Entry(root, width=27, font=('Cambria', 20), justify=RIGHT)
e.insert(0, "0")
e.grid(row=0, column=0, columnspan=4)

label = tb.Label(root, text="0", font=('Cambria', 15), bootstyle='secondary')
label.grid(row=1, column=0, columnspan=4)

def button_click(x):
    current = e.get()
    print("current: ", current)
    if str(current) == "0":
        current = ""
    elif str(current).count('.') >= 1 and str(x) == '.':
        return
    e.delete(0, END)
    e.insert(0, str(current) + str(x))

def clear_all():
    label.config(text="0")
    e.delete(0, END)
    e.insert(0, "0")

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
    # label.config(text=str(f_num)+" "+str(op)+" "+str(current)+" = "+str(result))

    f_num = 0

def delete_button():
    current = e.get()
    if len(current) == 1:
        e.delete(0, END)
        e.insert(0, "0")
    else:
        e.delete(0, END)
        e.insert(0, current[:-1])


# for i in range(10):
#     print(i)
#     button_1 = tb.Button(root, text="1", style='primary.Outline.TButton', command=lambda:button_click(1))

button_1    = tb.Button(root, text="1", style='primary.Outline.TButton', command=lambda:button_click(1))
button_2    = tb.Button(root, text="2", style='primary.Outline.TButton', command=lambda:button_click(2))
button_3    = tb.Button(root, text="3", style='primary.Outline.TButton', command=lambda:button_click(3))
button_adds = tb.Button(root, text="+", style='info.Outline.TButton',    command=lambda:operator_button("+"))

button_4    = tb.Button(root, text="4", style='primary.Outline.TButton', command=lambda:button_click(4))
button_5    = tb.Button(root, text="5", style='primary.Outline.TButton', command=lambda:button_click(5))
button_6    = tb.Button(root, text="6", style='primary.Outline.TButton', command=lambda:button_click(6))
button_subs = tb.Button(root, text="-", style='info.Outline.TButton',    command=lambda:operator_button("-"))

button_7     = tb.Button(root, text="7", style='primary.Outline.TButton', command=lambda:button_click(7))
button_8     = tb.Button(root, text="8", style='primary.Outline.TButton', command=lambda:button_click(8))
button_9     = tb.Button(root, text="9", style='primary.Outline.TButton', command=lambda:button_click(9))
button_multi = tb.Button(root, text="*", style='info.Outline.TButton',    command=lambda:operator_button("*"))

button_0      = tb.Button(root, text="0", style='primary.Outline.TButton', command=lambda:button_click(0))
button_dot    = tb.Button(root, text=".", style='primary.Outline.TButton', command=lambda:button_click("."))

# bksp_btn = tb.PhotoImage(file='5346420.png', width=5, height=5)

#Let us create a label for button event
button_delete = tb.Button(root, text="<=", style="danger.Outline.TButton", command=delete_button)
button_div    = tb.Button(root, text="/", style='info.Outline.TButton',    command=lambda:operator_button("/"))

button_equal = tb.Button(root, text="=",  style="success.TButton", command=equal_button)
button_clear = tb.Button(root, text="AC", style='warning.TButton', command=clear_all)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_adds.grid(row=2, column=3)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_subs.grid(row=3, column=3)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_multi.grid(row=4, column=3)

button_0.grid(row=5, column=0)
button_dot.grid(row=5, column=1)
button_delete.grid(row=5, column=2)
button_div.grid(row=5, column=3)


button_clear.grid(row=6, column=0, columnspan=2)
button_equal.grid(row=6, column=2, columnspan=2)






root.mainloop()