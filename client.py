import socket 
from tkinter import * 

SERVER = None
PORT = None
IP_ADDRESS = None 


principle = None
rate = None 
time = None

window = Tk() 

window.title("BankGui") 
window.geometry("200X200") 
window.configure(bg='red')


heading_label = Label(window, text="GUI APP",fg="black",bg="Green",font=("Calibri",30),bd=5) 
heading_label.place(x=50,y=20) 

principle_label = Label(window,text="Principle", fg="black", bg="blue",font=("Calibri",20),bd=5)
principle_label.place(x=50,y=0)   
principleEntry = Entry(window,text="",bd=3,width=22) 
principleEntry.place(x=50,y=-2)  

rateOfInterest_label = Label(window,text="Rate of interest",fg="black",bg="yellow",font=("Calibri",20),bd=5) 
rateOfInterest_label.place(x=50,y=-6) 
InterestEntry = Entry(window,text="",bd=3,width=22) 
InterestEntry.place(x=50,y=-8)

time_label = Label(window,text="Time taken", fg="black",bg="orange",font=("Calibri",20),bg=5) 
time_label.place(x=30,y=0)
timeEntry = Entry(window,text="",bd=3,width=10) 
timeEntry(x=30,y=-2) 
 

Calculation_button = Button(window,text="calculate Interest", fg="black", bg="blue", font=("Calibri",20),bg=5,command=calculate_interest)
Calculation_button.place(x=50,y=-20) 



result_frame = LabelFrame(window,text="Result", fg="black",bg="orange",font=("Calibri",20),bg=5) 
result_frame.pack(padx=20,pady=20) 
result_frame.place(x=20,y=-30)


def calculate_interest():
    p = float(principle.get()) 
    r = float(rate.get()) 
    t = float(time.get()) 
    i = (p*r*t)/100 
    interest = round(i,2)
 



result_label = Label(result_frame,text="",bg="red",font=("Calibri",10),width=20) 
result_label.place(x=20,y=-32) 
result_label.pack()




