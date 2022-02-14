import tkinter
from tkinter import *
from tkinter import ttk
import math
import tkinter as tk

window = Tk()
window.title("CALCULATOR")
window.config(padx=20, pady=20)


def on_click(text):

   show.insert(tkinter.END, text)


show = Text(window, width=23, height=4)
show.grid(row=0, column=0, columnspan=4)

clear_button = ttk.Button(window, text="AC", width=13, command=window.destroy)
clear_button.grid(row=1, column=0, columnspan=2)
button_9 = ttk.Button(window, text="9", width=5, command=lambda: on_click(9))
button_9.grid(row=2, column=2)
button_8 = ttk.Button(window, text="8", width=5, command=lambda: on_click(8))
button_8.grid(row=2, column=1)
button_7 = ttk.Button(window, text="7", width=5, command=lambda: on_click(7))
button_7.grid(row=2, column=0)
button_6 = ttk.Button(window, text="6", width=5, command=lambda: on_click(6))
button_6.grid(row=3, column=2)
button_5 = ttk.Button(window, text="5", width=5, command=lambda: on_click(5))
button_5.grid(row=3, column=1)
button_4 = ttk.Button(window, text="4", width=5, command=lambda: on_click(4))
button_4.grid(row=3, column=0)
button_3 = ttk.Button(window, text="3", width=5, command=lambda: on_click(3))
button_3.grid(row=4, column=2)
button_2 = ttk.Button(window, text="2", width=5, command=lambda: on_click(2))
button_2.grid(row=4, column=1)
button_1 = ttk.Button(window, text="1", width=5, command=lambda: on_click(1))
button_1.grid(row=4, column=0)
button_0 = ttk.Button(window, text="0", width=5, command=lambda: on_click(0))
button_0.grid(row=5, column=0)
button_dot = ttk.Button(window, text=".", width=5, command=lambda: on_click("."))
button_dot.grid(row=5, column=1)


def take_input():

   exp = show.get("1.0", "end-1c")
   entry = list(exp)
   length = len(entry)
   ans = ""
   ch = 0
   for i in range(0, length):
      if entry[i] >= "0":
         if entry[i] <= "9":
            ch = ch+1
            ans = ans+entry[i]
      else :
         entry[i - ch] = int(ans)
         while ch > 1:
            ch = ch - 1
            entry[i - ch] = "0"
         ch = 0
         ans = ""
   entry[i - ch + 1] = int(ans)
   while ch > 1:
      ch = ch - 1
      entry[i - ch + 1] = "0"
   i = 0
   l = length
   while i<l:
      if entry[i] == "0":
         entry.remove("0")
         l = l-1
         i = i-1
      i = i+1

   length = len(entry)
   j = 1

   while j < length:
      # if j < length:
         if entry[j] == "/":
            ans = entry[j-1]/entry[j+1]
            entry[j-1] = ans
            del entry[j]
            del entry[j]
            length = length-2
         elif entry[j] == "*":
            ans = entry[j-1]*entry[j+1]
            entry[j-1] = ans
            del entry[j]
            del entry[j]
            length = length-2
         else:
            j = j+2
   j = 1

   while j < length:
         if entry[j] == "+":
            ans = entry[j-1]+entry[j+1]
            entry[j-1] = ans
            del entry[j]
            del entry[j]
            length = length-2
         elif entry[j] == "-":
            ans = entry[j-1]-entry[j+1]
            entry[j-1] = ans
            del entry[j]
            del entry[j]
            length = length-2
         else:
            j = j+2

   print(entry[0])


equalsto_button = ttk.Button(window, text="=", width=13, command=lambda: take_input())
equalsto_button.grid(row=5, column=2, columnspan=2)
plus_button = ttk.Button(window, text="+", width=5, command=lambda: on_click("+"))
plus_button.grid(row=4, column=3)
minus_button = ttk.Button(window, text="-", width=5, command=lambda: on_click("-"))
minus_button.grid(row=3, column=3)
multiply_button = ttk.Button(window, text="*", width=5, command=lambda: on_click("*"))
multiply_button.grid(row=2, column=3)
divide_button = ttk.Button(window, text="/", width=5, command=lambda: on_click("/"))
divide_button.grid(row=1, column=3)
power_button = ttk.Button(window, text="^", width=5, command=lambda: on_click("^"))
power_button.grid(row=1, column=2)




window.mainloop()

