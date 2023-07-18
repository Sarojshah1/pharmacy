from tkinter import *
from PIL import ImageTk, Image, ImageDraw
from tkinter import ttk
import mysql.connector as mysql
from tkinter import messagebox
import os

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
def next():
    root.destroy()
    import billing4
def save():
    name=user_name_entry.get()
    address=user_Address_entry.get()
    contact=user_contact_entry.get()
    email=user_email_entry.get()
    if   name=='' or address=='' or contact==''or email=='':
        messagebox.showerror("error","please fill all fields")
    else:
        try:
                con=mysql.connect(host='localhost',user='root',password="saroj@0777",port="3306",database='pharmacy')
                mycursor=con.cursor()
        except:
              messagebox.showerror("error","connection error!please add your medicine again")
              return
        try:
            vals={ 
             "name":name, 
                "email":email, 
                "contactno":contact, 
                "address":address
                 }
            insert_query="""INSERT INTO user( name, email,contactno,address) VALUES( %s, %s, %s, %s)""",( vals['name'],vals['email'],int(vals['contactno']),vals['address'])
            mycursor.execute(*insert_query)
            con.commit()
            mycursor.close()
            con.close()
            user_name_entry.delete(0,'end')
            user_Address_entry.delete(0,'end')
            user_contact_entry.delete(0,'end')
            user_email_entry.delete(0,'end')
            messagebox.showinfo("success","added successfully")
        except:
            user_name_entry.delete(0,'end')
            user_Address_entry.delete(0,'end')
            user_contact_entry.delete(0,'end')
            user_email_entry.delete(0,'end')
            messagebox.showerror("error","invalid inputs")

    
# ***************buttons of the dashboard side********************************
dash=Button(text='Dashboard',width=19,height=2,border=0,bg='#595B67',fg='white',font=("Inter", 10, "bold"),cursor='hand2',command=dashboard)
dash.place(x=1,y=30)
medicine=Button(text='Medicine',border=0,bg='#363740',fg='white',font=("Inter", 10, "bold"),cursor='hand2',command=medicine)
medicine.place(x=10,y=90)
category=Button(text='Category',border=0,bg='#363740',fg='white',font=("Inter", 10, "bold"),cursor='hand2',command=category)
category.place(x=10,y=130)
billing=Button(text='Billing',width=19,border=0,bg='#595B67',fg='white',font=("Inter", 10, "bold"),cursor='hand2',command=billing)
billing.place(x=1,y=170,height=40)
# userimg=PhotoImage(file='category.png')
# img=Label(root,image=userimg,bg='#595B67')
# img.place(x=1,y=135)
# indicator for billing
billing_indicator=Button(root,text='',bg='#FF702A')
billing_indicator.place(x=1,y=170,width=5,height=40)
setting=Button(text='Pharmacy Setting',border=0,bg='#363740',fg='white',font=("Inter", 10, "bold"),cursor='hand2',command=settings)
setting.place(x=10,y=210)

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

# ********add user  ****************************
info=Label(root,text='New Customer',fg='#363740',font=("Poppins", 15,"bold"))
info.place(x=200,y=200)
a=Label(root,text='________________________________________________________________________________________________________________________________________________________________________________________________')
a.place(x=190,y=230)
user_name=Label(root,text='Name',fg='#363740',width=5,font=("Poppins",15))
user_name.place(x=190,y=300)
user_name_entry=Entry(root,text='',width=100)
user_name_entry.place(x=400,y=300,height=35)

user_Address=Label(root,text='Address',fg='#363740',font=("Poppins",15))
user_Address.place(x=190,y=350)
user_Address_entry=Entry(root,text='',width=100)
user_Address_entry.place(x=400,y=350,height=35)

user_contact=Label(root,text='Contact',fg='#363740',font=("Poppins",15))
user_contact.place(x=190,y=400)
user_contact_entry=Entry(root,text='',width=100)
user_contact_entry.place(x=400,y=400,height=35)

user_email=Label(root,text='Email',fg='#363740',font=("Poppins",15))
user_email.place(x=190,y=450)
user_email_entry=Entry(root,text='',width=100)
user_email_entry.place(x=400,y=450,height=35)


next_button=Button(root,text='NEXT',border=1,width=15,height=2,bg='#3ECF0A',fg='#FAFAFA',font=("Poppins",10),command=next)
next_button.place(x=880,y=550)

save_button=Button(root,text='Save Customer',border=1,width=20,height=2,bg='#FFD580',fg='black',font=("Poppins",10),command=save)
save_button.place(x=280,y=560)

root.mainloop()