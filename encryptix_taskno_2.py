from tkinter import *

my_calculator=Tk()
my_calculator.title("Calculator")
my_calculator.geometry("400x400")
my_calculator.resizable(0,0)

text= Entry(my_calculator,font=("times new roman",15, "bold"), bg="Light blue")
text.pack(fill=X,padx=10,pady=10,ipadx=10,ipady=10)

def addtoText(n):
    text.insert(END,n)

def calculate():
    result = eval(text.get())
    text.delete(0,END)
    text.insert(0,result)
    
frame=Frame(my_calculator)
frame.pack(side=TOP,anchor=NW)

rightFrame=Frame(frame)
rightFrame.pack(side=RIGHT)

frame1 = Frame(frame)
frame1.pack()

button1=Button(frame1,text="1",width=10,height=4, command=lambda:addtoText("1"),bg='orange')
button1.pack(side=LEFT)
button2=Button(frame1,text="2",width=10,height=4, command=lambda:addtoText("2"),bg='orange')
button2.pack(side=LEFT)
button3=Button(frame1,text="3",width=10,height=4, command=lambda:addtoText("3"),bg='orange')
button3.pack(side=LEFT)

frame2 = Frame(frame)
frame2.pack()

button4=Button(frame2,text="4",width=10,height=4, command=lambda:addtoText("4"),bg='light yellow')
button4.pack(side=LEFT)
button5=Button(frame2,text="5",width=10,height=4, command=lambda:addtoText("5"),bg='light yellow')
button5.pack(side=LEFT)
button6=Button(frame2,text="6",width=10,height=4, command=lambda:addtoText("6"),bg='light yellow')
button6.pack(side=LEFT)

frame3 = Frame(frame)
frame3.pack()

button7 = Button(frame3,text="7",width=10,height=4, command=lambda:addtoText("7"),bg='light green')
button7.pack(side=LEFT)
button8 = Button(frame3,text="8",width=10,height=4, command=lambda:addtoText("8"),bg='light green')
button8.pack(side=LEFT)
button9 = Button(frame3,text="9",width=10,height=4, command=lambda:addtoText("9"),bg='light green')
button9.pack(side=LEFT)


frame4 = Frame(frame)
frame4.pack()

buttonpoint = Button(frame4,text=".",width=10,height=4, command=lambda:addtoText("."),bg='light gray')
buttonpoint.pack(side=LEFT)
buttonzero= Button(frame4,text="0",width=10,height=4, command=lambda:addtoText("0"),bg='light gray')
buttonzero.pack(side=LEFT)
buttonequal = Button(frame4,text="=",width=10,height=4, command=lambda:calculate(),bg='light gray')
buttonequal.pack(side=LEFT)

buttonplus = Button(rightFrame,text="+",width=10,height=4, command=lambda:addtoText("+"))
buttonplus.pack()
buttonsub = Button(rightFrame,text="-",width=10,height=4, command=lambda:addtoText("-"))
buttonsub.pack()
buttonmul = Button(rightFrame,text="x",width=10,height=4, command=lambda:addtoText("*"))
buttonmul.pack()
buttondiv = Button(rightFrame,text="/",width=10,height=4, command=lambda:addtoText("/"))
buttondiv.pack()


my_calculator.mainloop()
