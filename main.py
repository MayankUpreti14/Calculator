from tkinter import *

window = Tk()
window.title("CALCULATOR")
window.config(padx=20, pady=20)

show = Text(width=23, height=4)
show.grid(row=0, column=0, columnspan=4)

clear_button = Button(text="AC", width=12)
clear_button.grid(row=1, column=0, columnspan=2)
button_9 = Button(text="9", width=5)
button_9.grid(row=2, column=2)
# button_9.insert()
button_8 = Button(text="8", width=5)
button_8.grid(row=2, column=1)
button_7 = Button(text="7", width=5)
button_7.grid(row=2, column=0)
button_6 = Button(text="6", width=5)
button_6.grid(row=3, column=2)
button_5 = Button(text="5", width=5)
button_5.grid(row=3, column=1)
button_4 = Button(text="4", width=5)
button_4.grid(row=3, column=0)
button_3 = Button(text="3", width=5)
button_3.grid(row=4, column=2)
button_2 = Button(text="2", width=5)
button_2.grid(row=4, column=1)
button_1 = Button(text="1", width=5)
button_1.grid(row=4, column=0)
button_0 = Button(text="0", width=5)
button_0.grid(row=5, column=0)
button_dot = Button(text=".", width=5)
button_dot.grid(row=5, column=1)

equalsto_button = Button(text="=", width=12)
equalsto_button.grid(row=5, column=2, columnspan=2)
plus_button = Button(text="+", width=5)
plus_button.grid(row=4, column=3)
minus_button = Button(text="-", width=5)
minus_button.grid(row=3, column=3)
multiply_button = Button(text="*", width=5)
multiply_button.grid(row=2, column=3)
divide_button = Button(text="/", width=5)
divide_button.grid(row=1, column=3)
power_button = Button(text="^", width=5)
power_button.grid(row=1, column=2)






window.mainloop()
