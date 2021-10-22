from tkinter import *
master = Tk()
master.title("Calculator")
entry = Entry(master, borderwidth=10, width=40)
entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)
#buttons
button1 = Button(master, text="1",padx=20, pady=20)
button2 = Button(master, text="2",padx=20, pady=20)
button3 = Button(master, text="3",padx=20, pady=20)
button4 = Button(master, text="4",padx=20, pady=20)
button5 = Button(master, text="5",padx=20, pady=20)
button6 = Button(master, text="6",padx=20, pady=20)
button7 = Button(master, text="7",padx=20, pady=20)
button8 = Button(master, text="8",padx=20, pady=20)
button9 = Button(master, text="9",padx=20, pady=20)
button0 = Button(master, text="0",padx=20, pady=20)

buttonPercent = Button(master, text="%", padx=20, pady=20)
buttonClearEntry = Button(master, text="CE", padx=20, pady=20)
buttonAllClear = Button(master, text="C", padx=20, pady=20)

buttonDecimal = Button(master, text="1/x", padx=20, pady=20)
buttonSquare = Button(master, text="x²", padx=20, pady=20)
buttonSRoot = Button(master, text="²√x", padx=20, pady=20)

buttonDelete= Button(master, text="⌫", padx=20, pady=20)
buttonPlus = Button(master, text="+", padx=20, pady=20)
buttonMinus= Button(master, text="-", padx=20, pady=20)
buttonDivided = Button(master, text="÷", padx=20, pady=20)
buttonMultiply = Button(master, text="X", padx=20, pady=20)

buttonEquals = Button(master, text="=", padx=20, pady=20)
buttonDot = Button(master, text=".", padx=20, pady=20)
buttonNegative = Button(master, text="+/-", padx=20, pady=20)
#buttonsgrid

buttonPercent.grid(row=1 , column=0)
buttonClearEntry.grid(row=1 , column=1)
buttonAllClear.grid(row=1, column=2)
buttonDelete.grid(row=1, column=3)

buttonDecimal.grid(row=2 , column=0)
buttonSquare.grid(row=2 , column=1)
buttonSRoot.grid(row=2 , column=2)
buttonDivided.grid(row=2, column=3)

button1.grid(row=5 , column=0 )
button2.grid(row=5 , column=1 )
button3.grid(row=5 , column=2 )
buttonPlus.grid(row=5, column=3)

button4.grid(row=4 , column=0 )
button5.grid(row=4 , column=1 )
button6.grid(row=4 , column=2 )
buttonMinus.grid(row=4, column=3)

button7.grid(row=3 , column=0 )
button8.grid(row=3 , column=1 )
button9.grid(row=3 , column=2 )
buttonMultiply.grid(row=3, column=3)

buttonNegative.grid(row=6, column=0)
button0.grid(row=6 , column=1)
buttonDot.grid(row=6, column=2)
buttonEquals.grid(row=6, column=3)

master.mainloop()