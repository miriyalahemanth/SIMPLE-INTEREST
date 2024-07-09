from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("Simple Interest")
root.geometry("700x500")
root.configure(bg="cyan")
root.resizable(0,0)
def calculate_si():
    p=pvalue.get()
    r=rvalue.get()
    t=tvalue.get()
    si=p*(t*12)*r/100
    messagebox.showinfo("result",f"si is:{si}")
    
pvalue=IntVar()
rvalue=IntVar()
tvalue=IntVar()
l=Label(root,text="Simple Interest Calculator",font="arial 20",fg="blue").place(x=100,y=30)
l1=Label(root,text="principal",font="arial 20",fg="blue").place(x=50,y=100)
l1_entry=Entry(root,font="arial 20",bd=5,fg="blue",width=15,textvariable=pvalue).place(x=400,y=100)
l12=Label(root,text="rate of interest(per month)",font="arial 20",fg="blue").place(x=50,y=200)
l2_entry=Entry(root,font="arial 20",bd=5,fg="blue",width=15,textvariable=rvalue).place(x=400,y=200)
l13=Label(root,text="time(years)",font="arial 20",fg="blue").place(x=50,y=300)
l3_entry=Entry(root,font="arial 20",bd=5,width=15,fg="blue",textvariable=tvalue).place(x=400,y=300)
btn=Button(text="calculate",font="arial 20",bg="red",fg="white",command=calculate_si).place(x=250,y=350)
root.mainloop()
