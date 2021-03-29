#TKinter Module

import tkinter
window = tkinter.Tk()
window.title("My First Gui Program")
window.minsize(width =500, height=300)

#Label
my_label = tkinter.Label(text= "I am a Label", font=("Arial",24,"bold"))
my_label.pack(side ="left")

window.mainloop()

"""notes 1"""

#unlimited arguments
def add(n1,n2):
    return n1 +n2

def add(*args):
    for n in args:
        print(n)

add(3,4,6)

"""notes 2"""


def add(*args):
    print(args[0])

    sum = 0
    for n in args:
        sum += n
    return sum


print(add(3, 5, 6))

"""notes 3"""

def add(*args):
    print(args[0])

    sum=0
    for n in args:
       sum += n
    return sum

print(add(3,5,6))

def calculate(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key)
        print(value)
calculate(add=3, multiply=5)

def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
calculate(n=2, add= 3, multiply=5)

"""notes 4"""
class Car:

    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        self.model = kwargs.get("model")


my_car = Car( make = "Nissan")
#my_car = Car( make = "Nissan" , model= "GT-R")

print(my_car.model)

""""Notes 5"""

#Label
my_label = tkinter.Label(text= "I am a Label", font=("Arial",24,"bold"))
#my_label.pack(side ="left")
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text = "New Text")

#Button
def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text= new_text)

button = tkinter.Button(text= "Click Me", command=button_clicked)
button.pack()  # Show on screen

#Entry Component
input = tkinter.Entry(width=10)
input.pack()
input.get()