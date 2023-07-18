from tkinter import *
from tkinter import messagebox
import customtkinter as ctk
import mysql.connector as mysql


root=Tk()
width_screen=root.winfo_screenwidth()
height_screen=root.winfo_screenheight()
root.title("login page")
root.geometry(f"{width_screen}x{height_screen}")
root.minsize(400,400)
root.iconbitmap('medicine.ico')
root.configure(bg='#fff')
root.state('zoomed')
#  signin function
def signin():
    
    if username.get()=='' and code.get()=='':
        messagebox.showerror("error","please fill all fields")
    else:
        try:
            con=mysql.connect(host='localhost',user='root',password="saroj@0777",port="3306",database='pharmacy')
            mycursor=con.cursor()
        except:
            messagebox.showerror("error","connection error")
            return
        query='use pharmacy'
        mycursor.execute(query)
        query='select * from admin where email=%s and password=%s'
        mycursor.execute(query,(username.get(),code.get()))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror("error","invalid username or password")
        else:
            root.destroy()
            import das
def forget():
    top=Toplevel()
    top.title("Forget Password")
    top.geometry(f"{width_screen}x{height_screen}")
    top.iconbitmap('medicine.ico')
    top.state('zoomed')
    def show():
        eyeimg.config(file='icons8-eye-24.png')
        new_password.config(show="")
        eyebutton.config(command=hide)
    def hide():
        eyeimg.config(file='icons8-closed-eye-24.png')
        new_password.config(show='*')
        eyebutton.config(command=show)
    
    def show1():
        eyeimg2.config(file='icons8-eye-24.png')
        confirm_password.config(show="")
        eyebutton2.config(command=hide1)
    def hide1():
        eyeimg2.config(file='icons8-closed-eye-24.png')
        confirm_password.config(show='*')
        eyebutton2.config(command=show1)
        
    def save():
        try:
                con=mysql.connect(host='localhost',user='root',password="saroj@0777",port="3306",database='pharmacy')
                mycursor=con.cursor()
        except:
                messagebox.showerror("error","connection error")
                return
            
        if new_password.get() == confirm_password.get():
            vals={
                
                "password": confirm_password.get(),
        "Email": username1.get()
        }
            query='UPDATE admin  SET password=%s WHERE Email=%s',(vals['password'],vals['Email'])
            print(query)
            mycursor.execute(*query)
            con.commit()
            mycursor.close()
            con.close()
            messagebox.showinfo("Success","password updated successfully")
        # frame for displaying setting details 
    display_frame=Frame(top,bg='#FAFAFA',width=624,height=550)
    display_frame.place(x=350,y=100)
    settings=Label(top,text='Forget Password',fg='#363740',bg='#fafafa',font=('inter',15,'bold'))
    settings.place(x=360,y=110)
    # username  function
    def on_enter(e):
        username1.delete(0,'end')
        
    def on_leave(e):
        name=username1.get()
        if name=='':
            username1.insert(0,"")
        # return name  
    # username 
    username1=Entry(top,fg='black',bg='#FAFAFA',border=1,font=('microsoft yaHei UI light',15),width=40,cursor='hand2')
    username1.place(x=440,y=200,height=40)
    username1.insert(5,'Email')
    username1.bind('<FocusIn>',on_enter)
    username1.bind('<FocusOut>',on_leave) 

    # password functionality
    def on_enter(e):
        new_password.delete(0,'end')
    def on_leave(e):
        name=new_password.get()
        if name=='':
            new_password.insert(5,'')
    # /password workspace     
    new_password=Entry(top,width=40,fg='black',bg='#FAFAFA',border=1,font=('microsoft yaHei UI light',15),cursor='hand2',show='*')
    new_password.place(x=440,y=300,height=40)
    new_password.insert(5,'New Password')
    new_password.bind('<FocusIn>',on_enter)
    new_password.bind('<FocusOut>',on_leave)
    eyeimg=PhotoImage(file='icons8-closed-eye-24.png')
    eyebutton=Button(top,image=eyeimg,bd=0,bg='white',activebackground='white',cursor='hand2',command=show)
    eyebutton.place(x=855,y=310)

    # password functionality
    def on_enter(e):
        confirm_password.delete(0,'end')
    def on_leave(e):
        name=confirm_password.get()
        if name=='':
            confirm_password.insert(5,'')
    # /password workspace     
    confirm_password=Entry(top,width=40,fg='black',bg='#FAFAFA',border=1,font=('microsoft yaHei UI light',15),cursor='hand2',show='*')
    confirm_password.place(x=440,y=400,height=40)
    confirm_password.insert(5,'Confirm Password')
    confirm_password.bind('<FocusIn>',on_enter)
    confirm_password.bind('<FocusOut>',on_leave)
    eyeimg2=PhotoImage(file='icons8-closed-eye-24.png')
    eyebutton2=Button(top,image=eyeimg2,bd=0,bg='white',activebackground='white',cursor='hand2',command=show1)
    eyebutton2.place(x=855,y=410)

    save=Button(top,text='SAVE',width=10,bg='green',fg='white',font=("microsoft yaHei UI light",12),cursor='hand2',command=save)
    save.place(x=780,y=500)  

    
# to show and hide in password field
def show():
    eyeimg.config(file='icons8-eye-24.png')
    code.config(show="")
    eyebutton.config(command=hide)
def hide():
    eyeimg.config(file='icons8-closed-eye-24.png')
    code.config(show='*')
    eyebutton.config(command=show)
    
# pharmacy image
frame1=Frame(width=width_screen/2,height=height_screen,bg='#FF702A')
frame1.place(x=650,y=0)
img = PhotoImage(file ='pharma-removebg-preview.png')
Label(image=img,width=500,border=0,bg='#FF702A').place(x=717,y=10)
Label(text='''A computerized software application
designed to streamline and automate
various tasks within a pharmacy setting.''',fg='white',bg='#FF702A',width=45,height=3,font=('poppins',12,'bold')).place(x=740,y=420)
Label(text='Developed By : Let It Be',bg='#FF702A',fg='white',font=('poppins',12,'bold')).place(x=840,y=550)
Label(text='X',font=('Dancing Script',14,'bold'),bg='#FF702A',fg='white').place(x=1030,y=548)


frame=Frame(width=550,height=750,bg='#fff')
frame.place(x=100,y=90)

# heading
heading=Label(frame,text='SIGN IN',fg='#FF702A',bg='white',font=('microsoft yaHei UI light',20,'bold'))
heading.place(x=150,y=28)
heading=Label(frame,text='sign in & get started',fg='#6B6B6B',bg='white',font=('microsoft yaHei UI light',20))
heading.place(x=100,y=65)
# username  function
def on_enter(e):
    username.delete(0,'end')
    
def on_leave(e):
    name=username.get()
    if name=='':
        username.insert(0,"")
    # return name   
 
 
def Username():
    a=username.get()
    return a

# username workspace   
username=Entry(frame,width=35,fg='#6B6B6B',border=1,bg='white',font=('microsoft yaHei UI light',17),cursor='hand2')
username.place(x=20,y=130,height=50)
username.insert(5,'Email')
username.bind('<FocusIn>',on_enter)
username.bind('<FocusOut>',on_leave) 
# password functionality
def on_enter(e):
    code.delete(0,'end')
def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(5,'')
# /password workspace     
code=Entry(frame,width=35,fg='#6B6B6B',border=1,bg='white',font=('microsoft yaHei UI light',17),cursor='hand2',show='*')
code.place(x=20,y=200,height=50)
code.insert(5,'password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)
# eye button on password
eyeimg=PhotoImage(file='icons8-closed-eye-24.png')
eyebutton=Button(root,image=eyeimg,bd=0,bg='white',activebackground='white',cursor='hand2',command=show)
eyebutton.place(x=550,y=300)
forgotbutton=Button(root,text="Forgot Password?",bd=0,bg='white',activebackground='white',cursor='hand2',font=('microsoft yaHei UI light',12,'bold'),command=forget)
forgotbutton.place(x=434,y=340)
# sign in button
Button(frame,width=30,pady=10,text='Sign In',bg='#FF702A',fg='white',border=0,command= signin,font=('Inter',10,'bold'),cursor='hand2').place(x=130,y=320)
# remember me button
checkbox = ctk.CTkCheckBox(root,text='Remember Me')
checkbox.place(x=120,y=350)
# footer
copyright="\u00A9"
l1=Label(root,text=copyright,bg='white',fg='#6B6B6B',font=('poppins',16,'bold'))
l1.place(x=200,y=550)
l2=Label(root,text='2023 copyright| Pharmacy Store',bg='white',fg='#6B6B6B',font=('poppins',13,'bold'))
l2.place(x=220,y=552)

root.mainloop()