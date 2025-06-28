from tkinter import *
from tkinter import messagebox

def command_page():
    print("Loging page")


def admin_page_fun():
    admin_page = Tk()
    admin_page.title("admin page")
    admin_page.minsize(500,500)
    admin_page.minsize(500,500)
    admin_page.mainloop()

def user_page_fun():
    root.destroy()
    user_page = Tk()
    user_page.title("user page book store")
    Label(user_page,text="user book store").grid(row=0,column=1)
    user_page.minsize(500,500)
    user_page.maxsize(500,500)
    user_page.mainloop()
    

root = Tk()
root.title("book store")
Label(root,text="book store",font=("",16,"bold")).grid(row=0,column=1)
username = Label(root, text='First Name',width=20,height=2).grid(row=1)
password = Label(root, text='Last Name',width=20).grid(row=2)
e1 = Entry(root)
e2 = Entry(root)
e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
space = Label(root,pady=2).grid(row=3,column=1)



def user_password():
    try:
        if e1.get() == "admin" and e2.get() == "admin":
            root.destroy()
            admin_page_fun()
        elif e1.get() == "" and e2.get() == "":
            messagebox.showinfo('Info',"enter username and password")
        else:
            messagebox.showinfo('Info', 'invelide username password')
            return
    except():
            print("error")




loging_btn = Button(root,text="Loging",command=user_password).grid(row=4,column=1)
space = Label(root,pady=2).grid(row=5,column=1)
user_btn = Button(root,text="Book store",command=user_page_fun).grid(row=6,column=1)

root.minsize(500,500)
root.maxsize(500,500)




if __name__ == "__main__":
    root.mainloop()
    






