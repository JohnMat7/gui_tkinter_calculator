from tkinter import *


root = Tk()
root.title("GUI CALCULATOR")

e = Entry(root, width=55, borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


def button_addition():
    first_number = e.get()
    global f_num
    global operation
    operation = "+"
    f_num = int(first_number)
    e.delete(0, END)


def button_subtraction():
    first_number = e.get()
    global f_num
    global operation
    operation = "-"
    f_num = int(first_number)
    e.delete(0, END)


def button_multiplication():
    first_number = e.get()
    global f_num
    global operation
    operation = "*"
    f_num = int(first_number)
    e.delete(0, END)


def button_divide():
    first_number = e.get()
    global f_num
    global operation
    operation = "/"
    f_num = int(first_number)
    e.delete(0, END)


def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if operation == "+":
        e.insert(0, f_num + int(second_number))
    if operation == "-":
        e.insert(0, f_num - int(second_number))
    if operation == "*":
        e.insert(0, f_num * int(second_number))
    if operation == "/":
        e.insert(0, f_num / int(second_number))


def click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, current + str(number))


def clear():
    e.delete(0, END)


# BUTTONS
button_1 = Button(root, text="1", padx=40, pady=20, activeforeground='#000000',
                  activebackground='#999999', command=lambda: click(1))
button_2 = Button(root, text="2", padx=40, pady=20, activeforeground='#000000',
                  activebackground='#999999', command=lambda: click(2))
button_3 = Button(root, text="3", padx=40, pady=20, activeforeground='#000000',
                  activebackground='#999999', command=lambda: click(3))
button_4 = Button(root, text="4", padx=40, pady=20, activeforeground='#000000',
                  activebackground='#999999', command=lambda: click(4))
button_5 = Button(root, text="5", padx=40, pady=20, activeforeground='#000000',
                  activebackground='#999999', command=lambda: click(5))
button_6 = Button(root, text="6", padx=40, pady=20, activeforeground='#000000',
                  activebackground='#999999', command=lambda: click(6))
button_7 = Button(root, text="7", padx=40, pady=20, activeforeground='#000000',
                  activebackground='#999999', command=lambda: click(7))
button_8 = Button(root, text="8", padx=40, pady=20, activeforeground='#000000',
                  activebackground='#999999', command=lambda: click(8))
button_9 = Button(root, text="9", padx=40, pady=20, activeforeground='#000000',
                  activebackground='#999999', command=lambda: click(9))
button_0 = Button(root, text="0", padx=40, pady=20, activeforeground='#000000',
                  activebackground='#999999', command=lambda: click(0))

button_add = Button(root, text="+", padx=39, pady=20,
                    command=button_addition, fg="#ffffff", bg="#999999")
button_subtract = Button(root, text="-", padx=40, pady=20,
                         command=button_subtraction, fg="#ffffff", bg="#999999")
button_multiply = Button(root, text="*", padx=40, pady=20,
                         command=button_multiplication, fg="#ffffff", bg="#999999")
button_divide = Button(root, text="/", padx=40, pady=20,
                       command=button_divide, fg="#ffffff", bg="#999999")
button_equal = Button(root, text="=", padx=182, pady=20,
                      command=button_equal, fg="#ffffff", bg="#999999")

button_clear = Button(root, text="C", padx=40, pady=20,
                      command=clear, fg="#ffffff", bg="#444444")
button_clearall = Button(root, text="CE",
                         padx=36, pady=20, command=clear, fg="#ffffff", bg="#444444")


# GRID/POSITIONING OF BUTTON
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)


button_0.grid(row=4, column=1)
button_clear.grid(row=4, column=0)
button_clearall.grid(row=4, column=2)

button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)
button_equal.grid(row=5, column=0, columnspan=4)


root.mainloop()
