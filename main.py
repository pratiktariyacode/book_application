from tkinter import *
import tkinter as tk 
from tkinter import messagebox, ttk



def command_page():
    print("Loging page")


def admin_page_fun():
    root.destroy()
    admin_page = Tk()
    admin_page.title("admin page")
    admin_page.minsize(500,500)
    admin_page.minsize(500,500)
    admin_page.mainloop()

    

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




def on_tree_select(self, event):
    selected = self.tree.selection()
    if selected:
        self.selected_book_id = int(selected[0])
    else:
        self.selected_book_id = None

def user_loging():
        print("main page")



def user_page_fun():
    root.destroy()
    user_page = Tk()
    user_page.title("book store free Download")
    Label(user_page, text='Book List', font=('Arial', 16)).pack(pady=10)
    tree = ttk.Treeview(user_page, columns=('Title', 'Author','Name'), show='headings')
    tree.heading('Title', text='Title')
    tree.heading('Author', text='Author')
    tree.heading('Name',text='name')
    tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
    tree.bind('<<TreeviewSelect>>', on_tree_select)
    btn1 = Button(user_page,text="View").pack()
    btn2 = Button(user_page,text="Download").pack() 
    loggaupt = Button(user_page,text="Logaut",command=user_loging).pack() 
    user_page.minsize(500,500)
    user_page.maxsize(500,500)
    user_page.mainloop()




def user_password():
    try:
        if e1.get() == "admin" and e2.get() == "admin":
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


if __name__ == '__main__':
    root.mainloop()
    












