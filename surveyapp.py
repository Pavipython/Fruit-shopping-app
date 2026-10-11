from tkinter import *
window=Tk()
window.geometry("800x500")
window.config(background="light blue")
window.title("Survey")

Email = Label(window,text="Email",font=("Arial",15))
Email.place(x=35,y=100)
EmailEntry=Entry(window,font=("Ariel",15))
EmailEntry.place(x=100,y=100)

Password= Label(window,text="Password",font=("Arial",15))
Password.place(x=400,y=100)
PasswordEntry=Entry(window,font=("Ariel",15))
PasswordEntry.place(x=500,y=100)


colour=Label(window,text="what is your favourite color",font=("Comic sans",15))
colour.place(x=80,y=220)
sb1=Spinbox(window,values=("green","blue","yellow","red","black","white"),font=("Comic sans",15))
sb1.place(x=80,y=250)

Animal=Label(window,text="What is your favourite animal",font=("Comic sans",15))
Animal.place(x=450,y=220)
sb2=Spinbox(window,values=("horse","chicken","snake","owl","dog","cat"),font=("Comic sans",15))
sb2.place(x=450,y=250)



window.mainloop()
