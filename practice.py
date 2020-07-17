from tkinter import *

users={
    "user1":"pass1",
    "user2":"pass2",
}

root = Tk()
root.geometry('500x500')
root.title('Login')
logo = Label(root, text='Welcome to My World', bg='#0052cc',fg='#B284BE')
logo.pack()

#user
user_name = Entry(root,width=50)
user_name.insert(0,'User Name')
user_name.pack()

#password
password = Entry(root,show='*', width=50)
password.insert(0,'password')
password.pack()

#submit button
def submit():
    if user_name.get() not in users.keys():
        Label(root, text='User name is incorrect').pack()
        root.after(2000,root.destroy)
    elif users.get(user_name.get()) != password.get():
        Label(root, text='Password is incorrect').pack()
        root.after(2000,root.destroy)
    else:
        Label(root, text='Welcome in').pack()

submit_button = Button(root, text='Submit',  command=submit)
submit_button.pack()
root.mainloop()

 
