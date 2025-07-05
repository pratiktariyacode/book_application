from tkinter import *
import tkinter as tk 
from tkinter import messagebox, ttk , filedialog
import sqlite3




conn = sqlite3.connect("book.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL
    )
''')

conn.commit()


def add():
    title = add_title_entry.get()
    auther = add_author_entry.get()
    if title and auther:
        cursor.execute("INSERT INTO books (title,auther) VALUES (?,?)",(title,auther))
        conn.commit()
        add_title_entry.delete(0,tk.END)
        add_author_entry.delete(0,tk.END)
    else:
        messagebox.showwarning("Warning","insert error")
    book_add_page.destroy()

def __del__(self):
    self.conn.close() 

def list_box_add(page_name):
    global list_box
    list_box = Listbox(page_name,width=70,height=25).pack()

def add_data():
    list_box.delete(0,tk.END)
    cursor.execute("select * from books")
    all_data = cursor.fetchall()
    for row in all_data:
        all_data.insert(tk.END,row[1])                  

        

def delete_task():
        selected_task = list_box.get(tk.ACTIVE)
        if selected_task:
            cursor.execute("DELETE FROM tasks WHERE task=?", (selected_task,))
            conn.commit()
            add_data()
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

def on_closing():
    root.destroy()

def user_loging():
    print("run clicke")
    user_page.withdraw()
    root.deiconify()
    e1.delete(0, END)
    e2.delete(0, END)

def admin_loging():
    admin_page.withdraw()
    root.deiconify()
    e1.delete(0, END)
    e2.delete(0, END)
    

def add_book_page():
    global book_add_page
    book_add_page = Toplevel(root)
    book_add_page.title("Book Add Page")

    Label(book_add_page, text="Add Book", font=("", 15, "bold"), padx=100, pady=10).pack()

    Label(book_add_page, text="Title", font=("", 15, "bold"), pady=2).pack()
    global add_title_entry, add_author_entry
    add_title_entry = Entry(book_add_page)
    add_title_entry.pack()

    Label(book_add_page, text="Author", font=("", 15, "bold"), pady=2).pack()
    add_author_entry = Entry(book_add_page)
    add_author_entry.pack()


    def browse_pdf():
        filename = filedialog.askopenfilename(
            filetypes=[("PDF files", "*.pdf")],
            title="Select a PDF file"
        )
        pdf_entry.delete(0, END)
        pdf_entry.insert(0, filename)
    


    Label(book_add_page, text="PDF", font=("", 15, "bold"), pady=2).pack()
    pdf_entry = Entry(book_add_page)
    pdf_entry.pack()

    Button(book_add_page, text="Browse PDF", command=browse_pdf).pack(pady=5)
    Button(book_add_page,text="add",command=add,pady=3,width=15,bg="black",fg="white").pack()

    book_add_page.minsize(300, 300)
    book_add_page.maxsize(300, 300)
    book_add_page.mainloop()




def admin_page_fun():
    root.withdraw()
    global admin_page
    admin_page = Toplevel(root)
    admin_page.title("book store free Download")
    Label(admin_page, text='Admin Book List', font=('Arial', 16)).pack(pady=10)

    list_box_add(admin_page)
    

    button_frame = Frame(admin_page)
    button_frame.pack(pady=10)


    btn1 = Button(button_frame, text="View")
    btn1.pack(side=LEFT, padx=10)

    btn2 = Button(button_frame, text="Download")
    btn2.pack(side=LEFT, padx=10)

    btn3 = Button(button_frame, text="Add Book",command=add_book_page)
    btn3.pack(side=LEFT, padx=10)

    btn4 = Button(button_frame, text="Edit")
    btn4.pack(side=LEFT, padx=10)

    btn5 = Button(button_frame, text="Delete")
    btn5.pack(side=LEFT, padx=10)

    loggaupt = Button(button_frame, text="Logaut", command=admin_loging)
    loggaupt.pack(side=LEFT, padx=10)
    # admin_page.minsize(500,500)
    # admin_page.maxsize(500,500)
    window_width = 750
    window_height = 550

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)


    admin_page.geometry(f"{window_width}x{window_height}+{x}+{y}")
    admin_page.mainloop()

   

root = Tk()
root.title("book store")
Label(root,text="book store",font=("",16,"bold")).grid(row=0,column=1)
username = Label(root, text='First Name',width=20,height=2).grid(row=1)
password = Label(root, text='password',width=20).grid(row=2)
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



def user_page_fun():
    root.withdraw()
    global user_page
    user_page = Toplevel(root)
    user_page.title("book store free Download")
    Label(user_page, text='Book List', font=('Arial', 16)).pack(pady=10)
    list_box_add(user_page)

    button_frame = Frame(user_page)
    button_frame.pack(pady=10)


    btn1 = Button(button_frame, text="View")
    btn1.pack(side=LEFT, padx=10)

    btn2 = Button(button_frame, text="Download")
    btn2.pack(side=LEFT, padx=10)

    btn3 = Button(button_frame, text="Add Book",command=add_book_page)
    btn3.pack(side=LEFT, padx=10)

    btn4 = Button(button_frame, text="Delete",command=delete_task)
    btn4.pack(side=LEFT, padx=10)

    loggaupt = Button(button_frame, text="Logaut", command=user_loging)
    loggaupt.pack(side=LEFT, padx=10)

    # user_page.minsize(500,500)
    # user_page.maxsize(500,500)
    window_width = 750
    window_height = 550

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)


    user_page.geometry(f"{window_width}x{window_height}+{x}+{y}")
    user_page.mainloop()




def user_password():
    try:
        if e1.get() == "admin" and e2.get() == "admin123":
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
# root.minsize(500,500)
# root.maxsize(500,500)
root.protocol("WM_DELETE_WINDOW", on_closing)
# root.geometry("750x550")

window_width = 750
window_height = 550

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")





if __name__ == '__main__':
    root.mainloop()

