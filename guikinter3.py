'''
def show():
    print("now see the magic")
    win=Tk()
          
root=Tk()
root.geometry("1000x1000")
root.title("Deutschland")

btn=Button(root,
           text="click me",
           command=show)
btn2=Button(root,
            text="click me",
            command=root.destroy)

btn.pack()
btn2.pack()
root.mainloop
'''
from tkinter import *
def datashow():
    print("name is",name.get())
    print("checkbutton1 :",f.get())
    print("checkbutton2 :",se.get())
    print("checkbutton3 :",th.get())

root=Tk()
root.geometry("500x500")

f=StringVar(value="")
se=StringVar(value="")
th=StringVar(value="")

u=Label(root,text="Enter name")
u.pack()

name=Entry(root)
name.pack()

s=Label(root,text="Select")
s.pack()

ch1=Checkbutton(root,text="Java",variable=f, onvalue="Java", offvalue="")
ch2=Checkbutton(root,text="C++",variable=se, onvalue="C++", offvalue="")
ch3=Checkbutton(root,text="Python",variable=th, onvalue="Python", offvalue="")

ch1.pack()
ch2.pack()
ch3.pack()

btn=Button(root,text="Submit",command=datashow)

btn.pack()

root.mainloop
