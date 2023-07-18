from tkinter import *
from PIL import ImageTk, Image, ImageDraw
from tkinter import ttk
import mysql.connector as mysql
from tkinter import messagebox
root=Tk()
width_screen=root.winfo_screenwidth()
height_screen=root.winfo_screenheight()
root.title("Medicine/pharmacy_management_system")
root.geometry(f"{width_screen}x{height_screen}")
root.minsize("400","300")
root.iconbitmap('medicine.ico')
root.state("zoomed")
# ****************************dashboard frame************************************
frame=Frame(width=160,padx=30,bg='#363740')
frame.pack(side=LEFT,fill=Y)


# ****************************logo image************************************
logoImg=PhotoImage(file='logo.png')
logo=Label(image=logoImg,bg='white',fg='black',width=159,height=27)
logo.place(x=0,y=0)

# logout function
def logout():
    root.destroy()
    import login
    
# dashboard function
def dashboard():
    root.destroy()
    import das
# medicine function
def medicine():
    root.destroy()
    import medicine1
    
# category function
def category():
    root.destroy()
    import category1

# billing function
def billing():
    root.destroy()
    import billing
# settings function
def settings():
    root.destroy()
    import settings

# username  function
def on_enter(e):
    username.delete(0,'end')
    
def on_leave(e):
    name=username.get()
    if name=='':
        username.insert(0,'')
        
# to show and hide in password field
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
       "Email": username.get()
       }
        query='UPDATE admin  SET password=%s WHERE Email=%s',(vals['password'],vals['Email'])
        print(query)
        mycursor.execute(*query)
        con.commit()
        mycursor.close()
        con.close()
        
    # root.destroy()
    # import das
        
    
# ***************buttons of the dashboard side********************************
dash=Button(text='Dashboard',width=19,height=2,border=0,bg='#595B67',fg='white',font=("Inter", 10, "bold"),cursor='hand2',command=dashboard)
dash.place(x=1,y=30)
medicine=Button(text='Medicine',border=0,bg='#363740',fg='white',font=("Inter", 10, "bold"),cursor='hand2',command=medicine)
medicine.place(x=10,y=90)
category=Button(text='Category',border=0,bg='#363740',fg='white',font=("Inter", 10, "bold"),cursor='hand2',command=category)
category.place(x=10,y=130)
billing=Button(text='Billing',border=0,bg='#363740',fg='white',font=("Inter", 10, "bold"),cursor='hand2',command=billing)
billing.place(x=10,y=170)
setting=Button(text='Pharmacy Setting',width=19,border=0,bg='#595B67',fg='white',font=("Inter", 10, "bold"),cursor='hand2',command=settings)
setting.place(x=1,y=210,height=40)
# indicator for setting
setting_indicator=Button(root,text='',bg='#FF702A')
setting_indicator.place(x=1,y=210,width=5,height=40)


# ***************log out button*******************************
logout=Button(text='Log Out',border=0,bg='#363740',fg='white',font=("Inter", 10, "bold"),cursor='hand2',command=logout)
logout.place(x=10,y=250)

# *******header frame *******
frame1=Frame(root,bg='#FAFAFA')
frame1.place(x=164,y=0,width=1150,height=60)


# ***********heading********************************
heading=Label(frame1,text='ABC Pharmacy Store',bg='#FAFAFA',fg='black',font=("camb",20,'bold'))
heading.place(x=100,y=5)

#************* profile image****************************
profileImg=PhotoImage(file='profile.png')
profile=Label(image=profileImg,fg='black',bg='#FAFAFA')
profile.place(x=1050,y=0)
name=Label(text="Admin",fg='black',bg='#FAFAFA',font=("Poppins", 10))
name.place(x=1100,y=25)
name=Label(text="Saroj Kumar Sah",bg='#FAFAFA',fg='black',font=("Poppins", 10))
name.place(x=1100,y=5)

# frame for displaying setting details 
display_frame=Frame(root,bg='#FAFAFA',width=624,height=550)
display_frame.place(x=350,y=100)
settings=Label(root,text='Pharmacy Settings',fg='#363740',bg='#fafafa',font=('inter',15,'bold'))
settings.place(x=360,y=110)
# username 
username=Entry(root,fg='black',bg='#FAFAFA',border=1,font=('microsoft yaHei UI light',15),width=40,cursor='hand2')
username.place(x=440,y=200,height=40)
username.insert(5,'Email')
username.bind('<FocusIn>',on_enter)
username.bind('<FocusOut>',on_leave) 

# password functionality
def on_enter(e):
    new_password.delete(0,'end')
def on_leave(e):
    name=new_password.get()
    if name=='':
        new_password.insert(5,'')
# /password workspace     
new_password=Entry(root,width=40,fg='black',bg='#FAFAFA',border=1,font=('microsoft yaHei UI light',15),cursor='hand2',show='*')
new_password.place(x=440,y=300,height=40)
new_password.insert(5,'New Password')
new_password.bind('<FocusIn>',on_enter)
new_password.bind('<FocusOut>',on_leave)
eyeimg=PhotoImage(file='icons8-closed-eye-24.png')
eyebutton=Button(root,image=eyeimg,bd=0,bg='white',activebackground='white',cursor='hand2',command=show)
eyebutton.place(x=855,y=310)

# password functionality
def on_enter(e):
    confirm_password.delete(0,'end')
def on_leave(e):
    name=confirm_password.get()
    if name=='':
        confirm_password.insert(5,'')
# /password workspace     
confirm_password=Entry(root,width=40,fg='black',bg='#FAFAFA',border=1,font=('microsoft yaHei UI light',15),cursor='hand2',show='*')
confirm_password.place(x=440,y=400,height=40)
confirm_password.insert(5,'Confirm Password')
confirm_password.bind('<FocusIn>',on_enter)
confirm_password.bind('<FocusOut>',on_leave)
eyeimg2=PhotoImage(file='icons8-closed-eye-24.png')
eyebutton2=Button(root,image=eyeimg2,bd=0,bg='white',activebackground='white',cursor='hand2',command=show1)
eyebutton2.place(x=855,y=410)

save=Button(root,text='SAVE',width=10,bg='green',fg='white',font=("microsoft yaHei UI light",12),cursor='hand2',command=save)
save.place(x=780,y=500)



root.mainloop()