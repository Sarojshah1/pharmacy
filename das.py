from tkinter import *
from PIL import ImageTk, Image, ImageDraw
from tkinter import ttk
import mysql.connector as mysql





root=Tk()
width_screen=root.winfo_screenwidth()
height_screen=root.winfo_screenheight()
root.title("dashboard/pharmacy_management_system")
root.geometry(f"{width_screen}x{height_screen}")
root.minsize("400","300")
root.iconbitmap('medicine.ico')
root.state("zoomed")
# root.configure(bg='blu')
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
# data base
try:
            con=mysql.connect(host='localhost',user='root',password="saroj@0777",port="3306",database='pharmacy')
            mycursor=con.cursor()
except:
            messagebox.showerror("error","connection error")
query1='select * from category'
mycursor.execute(query1)
row1=mycursor.fetchall()
count1=len(row1) 
query2='select * from user'
mycursor.execute(query2)
row2=mycursor.fetchall()
count2=len(row2)          
query='select * from medicine'
mycursor.execute(query)
row=mycursor.fetchall()
count=len(row)
# ***************buttons of the dashboard side********************************
dash=Button(text='Dashboard',width=19,height=2,border=0,bg='#595B67',fg='white',font=("Inter", 10, "bold"),cursor='hand2',command=dashboard)
dash.place(x=1,y=30)
medicine=Button(text='Medicine',border=0,bg='#363740',fg='white',font=("Inter", 10, "bold"),cursor='hand2',command=medicine)
medicine.place(x=10,y=90)
category=Button(text='Category',border=0,bg='#363740',fg='white',font=("Inter", 10, "bold"),cursor='hand2',command=category)
category.place(x=10,y=130)
billing=Button(text='Billing',border=0,bg='#363740',fg='white',font=("Inter", 10, "bold"),cursor='hand2',command=billing)
billing.place(x=10,y=170)
setting=Button(text='Pharmacy Setting',border=0,bg='#363740',fg='white',font=("Inter", 10, "bold"),cursor='hand2',command=settings)
setting.place(x=10,y=210)
# indicator for dashboard
dashboard_indicator=Button(root,text='',bg='#FF702A')
dashboard_indicator.place(x=2,y=30,width=5,height=40)
# ***************log out button*******************************
logout=Button(text='Log Out',border=0,bg='#363740',fg='white',font=("Inter", 10, "bold"),cursor='hand2',command=logout)
logout.place(x=10,y=250)


# *******header frame *******
frame1=Frame(root,bg='#FAFAFA')
frame1.place(x=164,y=0,width=1150,height=60)


# ***********heading********************************
heading=Label(frame1,text='ABC Pharmacy Store',bg='#FAFAFA',fg='black',font=("camb",20,'bold'))
heading.place(x=100,y=5)



# # select button
# def comboFunction(e):#function for selecting
#     combo.set("saroj kumar sah")  
     
# combo = ttk.Combobox(root, values=["saroj kumar sah","Log Out"])
# combo.place(x=1100,y=0)
# combo.config(width=15)
# combo.config(height=15)
# combo.set("saroj kumar sah") 
# combo.bind('<<ComboboxSelected>>',comboFunction)
# combo['state']='readonly'
profileImg=PhotoImage(file='profile.png')
profile=Label(image=profileImg,fg='black',bg='#FAFAFA')
profile.place(x=1050,y=0)
name=Label(text="Admin",fg='black',bg='#FAFAFA',font=("Poppins", 10))
name.place(x=1100,y=25)
name=Label(text="saroj07",bg='#FAFAFA',fg='black',font=("Poppins", 10))
name.place(x=1100,y=5)
# **********medicine buttons****************************
medicineframe=Frame(width=250,height=90,bg="#FAFAFA")
medicineframe.place(x=180,y=100)
med=Button(root,text="Medicine",border=0,fg='black',bg='#FAFAFA',font=("inter",14),cursor='hand2',command=medicine)
med.place(x=180,y=100)
medimg=PhotoImage(file='medi.png')
medi=Label(root,image=medimg,bg='#FAFAFA',fg='black')
medi.place(x=370,y=120)
med_num=Label(root,text=count,fg='black',bg='#FAFAFA',font=("inter",14))
med_num.place(x=190,y=150)
# **********CATEGORIES buttons****************************
categoriesframe=Frame(width=250,height=90,bg="#FAFAFA")
categoriesframe.place(x=580,y=100)
cate=Button(text="Categories",border=0,fg='black',bg='#FAFAFA',font=("inter",14),cursor='hand2',command=category)
cate.place(x=580,y=100)
cateimg=PhotoImage(file='categories.png')
cat=Label(root,image=cateimg,bg='#FAFAFA',fg='black')
cat.place(x=770,y=120)
cate_num=Label(root,text=count1,fg='black',bg='#FAFAFA',font=("inter",14))
cate_num.place(x=590,y=150)
# **********USERS buttons****************************
userframe=Frame(width=250,height=90,bg="#FAFAFA")
userframe.place(x=1000,y=100)
user=Button(text="Users",border=0,width=5,fg='black',bg='#FAFAFA',font=("inter",14),cursor='hand2',command=settings)
user.place(x=1000,y=100)
userimg=PhotoImage(file='3-Friends.png')
use=Label(root,image=userimg,bg='#FAFAFA',fg='black')
use.place(x=1185,y=120)
cate_num=Label(root,text=count2,fg='black',bg='#FAFAFA',font=("inter",14))
cate_num.place(x=1010,y=150)
# *************appoinment booked****************
appoinmentframe=Frame(root,bg='#D2C8C8')
appoinmentframe.place(x=164,y=250,width=1100,height=40)
appo=Label(root,text='Latest Products',bg='#D2C8C8',fg='black',font=("inter",15,"bold"))
appo.place(x=190,y=254)
# form frame
frame3=Frame(root,width=1050,height=300,bg='#FAFAFA')
frame3.place(x=200,y=310)


# ********frame to store usernames****************
frame2=Frame(root,bg='#FF702A')
frame2.place(x=230,y=320,width=1000,height=35)
id=Label(text="Product Id",bg='#FF702A',font=("poppins",12,"bold"))
id.place(x=230,y=328)
product_name=Label(text="Product Name",bg='#FF702A',font=("poppins",12,"bold"))
product_name.place(x=370,y=328)
product_status=Label(text="Product Status",bg='#FF702A',font=("poppins",12,"bold"))
product_status.place(x=620,y=328)
product_quantity=Label(text=" Quantity",bg='#FF702A',font=("poppins",12,"bold"))
product_quantity.place(x=880,y=328)
product_price=Label(text="Price",bg='#FF702A',font=("poppins",12,"bold"))
product_price.place(x=1100,y=328)

a=list(row)
c=50
d=50
e=50
f=50
g=50
for i in a:
    b=list(i)
    for j in range(1,len(b)+1):
        Label(frame3,text=b[0],bg='#FAFAFA',font=("poppins",10)).place(x=40,y=d)
        d=d+30
        Label(frame3,text=b[1],bg='#FAFAFA',font=("poppins",10)).place(x=180,y=c)
        c=c+30
        Label(frame3,text=b[3],bg='#FAFAFA',font=("poppins",10)).place(x=910,y=e)
        e=e+30
        Label(frame3,text=b[4],bg='#FAFAFA',font=("poppins",10)).place(x=700,y=f)
        f=f+30
        if b[4]>0:
            Label(frame3,text='in stock',bg='#FF702A',borderwidth=3,fg='black',font=("poppins",10)).place(x=440,y=g)

            g=g+30
        else:
            Label(frame3,text='out of stock',bg='red',fg='black',font=("poppins",10)).place(x=440,y=g)
            g=g+30
        break
root.mainloop()