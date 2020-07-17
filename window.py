from tkinter import *

root = Tk()
root.geometry('500x500')
root.title('Hello! Hello!')

def my_click():
    click_label =Label(root, text=myEntry.get() + ",Have a Good Day")
    click_label.pack()


myLabel = Label(root, text="What's up!", font=('Calibri',25))
myEntry = Entry(root, width= 50)
myButton = Button(root, text='click here', width=10, command=my_click)
myLabel.pack()
myEntry.pack()
myButton.pack()

root.mainloop()