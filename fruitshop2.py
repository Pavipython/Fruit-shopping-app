from tkinter import *
window=Tk()
window.geometry("500x900")
window.config(background="light blue")
window.title("Spinbox")

def calculator():
    price=0
# The user takes fruit from the spinbox can be obtained using "get()" function 
    fruit=sb1.get()
    if fruit=="mango":
        price=1
    elif fruit=="kiwi":
        price=3
    elif fruit=="apple":
        price=2
    elif fruit=="pear":
        price=4
    elif fruit=="banana":
        price=1
    elif fruit=="tomato":
        price=2
    elif fruit=="watermelon":
        price=7
    elif fruit=="cherry":
        price=5
# The user takes quantity from the spinbox using "int(get())" function
# convert quantity into an integer
    quantity=int(sb2.get())
# price multiplied by quantity
    total=price*quantity
# displays the total price
    totalprice.config(text="the total price you have to pay is :"+str(total))


heading=Label(window,text="fruit shopping app",font=("Comic sans",20,"bold"))
heading.place(x=150,y=0)

instruction=Label(window,text="This is a fruit shopping app",font=("Comic sans",20,"bold"))
instruction.place(x=90,y=100)
instruction2=Label(window,text="choose, buy and check how many fruit you want",font=("Comic sans",12,"bold"))
instruction2.place(x=90,y=150)

fruits=Label(window,text="fruits",font=("Comic sans",15))
fruits.place(x=80,y=220)
sb1=Spinbox(window,values=("mango","kiwi","apple","pear","banana","tomato","watermelon","cherry"),font=("Comic sans",15))
sb1.place(x=80,y=250)

quantity=Label(window,text="select quantity",font=("Comic sans",15))
quantity.place(x=80,y=300)
sb2=Spinbox(window,from_=0,to=10,font=("Comic sans",15))
sb2.place(x=80,y=330)

# pressing the button with the command function will be called in total price
total=Button(window,text="submit",font=("Calibre",20),command=calculator)
total.place(x=120,y=400)

totalprice=Label(window,text="total price: ",font=("Calibre",20))
totalprice.place(x=70,y=490)

window.mainloop()

