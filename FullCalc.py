from tkinter import *
import sys

Plus = False
Minus = False
Divide = False
Multiply = False

def Nine():
    NumNine = 9
    Entry.insert(CalcEnt, END, NumNine)

def Eight():
    NumEight = 8
    Entry.insert(CalcEnt, END, NumEight)
    
def Seven():
    NumSeven = 7
    Entry.insert(CalcEnt, END, NumSeven) 
    
def Six():
    NumSix = 6
    Entry.insert(CalcEnt, END, NumSix) 
  
def Five():
    NumFive = 5
    Entry.insert(CalcEnt, END, NumFive)  

def Four():
    NumFour = 4
    Entry.insert(CalcEnt, END, NumFour)

def Three():
    NumThree = 3
    Entry.insert(CalcEnt, END, NumThree)
    
def Two():
    NumTwo = 2
    Entry.insert(CalcEnt, END, NumTwo) 
    
def One():
    NumOne = 1
    Entry.insert(CalcEnt, END, NumOne)  
    
def Zero():
    NumZero = 0
    Entry.insert(CalcEnt, END, NumZero) 
    
def Clear():
    CalcEnt.delete(first=0, last=9999)  
    
def Add():
    try:
        global FirstCalc
        FirstCalc = Entry.get(CalcEnt)
        FirstCalc = int(FirstCalc)
        CalcEnt.delete(first=0, last=9999)
        global Plus
        Plus = True
        global Minus
        Minus = False
        global Divide
        Divide = False
        global Multiply
        Multiply = False
        
    except:
        CalcEnt.delete(first=0, last=9999)
        Entry.insert(CalcEnt, 0, "Error")
    
def Subtract():
    try:
        global FirstCalc
        FirstCalc = Entry.get(CalcEnt)
        FirstCalc = int(FirstCalc)
        CalcEnt.delete(first=0, last=9999)
        global Plus
        Plus = False
        global Minus
        Minus = True
        global Divide
        Divide = False
        global Multiply
        Multiply = False
        
    except:
        CalcEnt.delete(first=0, last=9999)
        Entry.insert(CalcEnt, 0, "Error")
    
def Divided():
    try: 
        global FirstCalc
        FirstCalc = Entry.get(CalcEnt)
        FirstCalc = int(FirstCalc)
        CalcEnt.delete(first=0, last=9999)
        global Plus
        Plus = False
        global Minus
        Minus = False
        global Divide
        Divide = True
        global Multiply
        Multiply = False
        
    except:
        CalcEnt.delete(first=0, last=9999)
        Entry.insert(CalcEnt, 0, "Error")
    
def Multiplied():
    try:      
        global FirstCalc
        FirstCalc = Entry.get(CalcEnt)
        FirstCalc = int(FirstCalc)
        CalcEnt.delete(first=0, last=9999)
        global Plus
        Plus = False
        global Minus
        Minus = False
        global Divide
        Divide = False
        global Multiply
        Multiply = True
        
    except:
        CalcEnt.delete(first=0, last=9999)
        Entry.insert(CalcEnt, 0, "Error")
    
def Equal():
    try:
        SecondCalc = Entry.get(CalcEnt)
        SecondCalc = int(SecondCalc)
        if Plus:
            Addition = FirstCalc + SecondCalc
            CalcEnt.delete(first=0, last=9999)
            Entry.insert(CalcEnt, 0 , Addition)
        elif Minus:
            Subtraction = FirstCalc - SecondCalc
            CalcEnt.delete(first=0, last=9999)
            Entry.insert(CalcEnt, 0 , Subtraction)
        elif Divide:
            Division = FirstCalc / SecondCalc
            CalcEnt.delete(first=0, last=9999)
            Entry.insert(CalcEnt, 0 , Division)
        if Multiply:
            Multiplication = FirstCalc * SecondCalc
            CalcEnt.delete(first=0, last=9999)
            Entry.insert(CalcEnt, 0 , Multiplication)
            
    except:
        CalcEnt.delete(first=0, last=9999)
        Entry.insert(CalcEnt, 0, "Error")
         
app = Tk()
app.title("Calculator")
app.geometry("800x400")


CalcEnt = Entry(app, bd=5)
CalcEnt.grid(column=0, row=0)

BtnNine = Button(app, bd=5, text="Nine", command=Nine)
BtnNine.grid(column=1, row=2)

BtnEight = Button(app, bd=5, text="Eight", command=Eight)
BtnEight.grid(column=2, row=2)

BtnSeven = Button(app, bd=5, text="Seven", command=Seven)
BtnSeven.grid(column=3, row=2)

BtnSix = Button(app, bd=5, text="Six", command=Six)
BtnSix.grid(column=1, row=3)

BtnFive = Button(app, bd=5, text="Five", command=Five)
BtnFive.grid(column=2, row=3)

BtnFour = Button(app, bd=5, text="Four", command=Four)
BtnFour.grid(column=3, row=3)

BtnThree = Button(app, bd=5, text="Three", command=Three)
BtnThree.grid(column=1, row=4)

BtnTwo = Button(app, bd=5, text="Two", command=Two)
BtnTwo.grid(column=2, row=4)

BtnOne = Button(app, bd=5, text="One", command=One)
BtnOne.grid(column=3, row=4)

BtnZero = Button(app, bd=5, text="Zero", command=Zero)
BtnZero.grid(column=2, row=5)

PlusBtn = Button(app, text="+", bd=5, command=Add)
PlusBtn.grid(column=1, row=6)

MinusBtn = Button(app, bd=5, text="-", command=Subtract)
MinusBtn.grid(column=2, row=6)

TimesBtn = Button(app, text="*", bd=5, command=Multiplied)
TimesBtn.grid(column=3, row=6)

DivBtn = Button(app, text="/", bd=5, command=Divided)
DivBtn.grid(column=4, row=6)

ClearBtn = Button(app, bd=5, text="Clear", command=Clear)
ClearBtn.grid(column=2, row=7)

EqualBtn = Button(app, bd=5, text="=", command=Equal)
EqualBtn.grid(column=2, row=8)

app.mainloop()
