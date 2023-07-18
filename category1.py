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

# add function
def add():
    root.destroy()
    import category2
    
# add function
def update():
    top=Toplevel(root)
    top.title("update category credentials")
    top.geometry(f"{width_screen}x{height_screen}")
    top.iconbitmap('medicine.ico')
    top.state('zoomed')
    def edit():
        if user_name_entry.get()=='' or user_category_entry.get()=='':
            messagebox.showerror("error","please fill all fields")
        else:
            try:
                con=mysql.connect(host='localhost',user='root',password="saroj@0777",port="3306",database='pharmacy')
                mycursor=con.cursor()
            except:
                messagebox.showerror("error","connection error")
                return
        vals={
                
                "categoryId": user_name_entry.get(),
        "category": user_category_entry.get(),
        }
        query='UPDATE category  SET name=%s WHERE categoryId=%s',(vals['category'],int(vals['categoryId']))

        mycursor.execute(*query)
        con.commit()
        mycursor.close()
        con.close()
        user_name_entry.delete(0,'end')
        user_category_entry.delete(0,'end')
        
    def quit():
        top.destroy()
        # *******header frame *******
    frame1=Frame(top,bg='#FAFAFA')
    frame1.place(x=0,y=0,width=1250,height=60)


    # ***********heading********************************
    heading=Label(frame1,text='ABC Pharmacy Store',bg='#FAFAFA',fg='black',font=("camb",20,'bold'))
    heading.place(x=500,y=5)


    # ********add medicine product ****************************
    add_medicine=Label(top,text='Update Category',fg='#363740',font=("Poppins", 20,"bold"))
    add_medicine.place(x=600,y=150)
    info=Label(top,text='Information',fg='#363740',font=("Poppins", 15,"bold"))
    info.place(x=200,y=200)
    a=Label(top,text='________________________________________________________________________________________________________________________________________________________________________________________________')
    a.place(x=190,y=230)
    user_name=Label(top,text='category ID',fg='#363740',font=("Poppins",15))
    user_name.place(x=190,y=300)
    user_name_entry=Entry(top,text='',width=100)
    user_name_entry.place(x=400,y=300,height=35)

    user_category=Label(top,text='category',fg='#363740',font=("Poppins",15))
    user_category.place(x=190,y=350)
    user_category_entry=Entry(top,text='',width=100)
    user_category_entry.place(x=400,y=350,height=35)


    save_button=Button(top,text='Update',border=1,width=15,height=2,bg='#3ECF0A',fg='#FAFAFA',font=("Poppins",10),command=edit)
    save_button.place(x=880,y=500)
    quit=Button(top,text='Quit',border=1,width=15,height=2,bg='red',fg='#FAFAFA',font=("Poppins",10),command=quit)
    quit.place(x=200,y=500)

    top.mainloop()
    
# ***************buttons of the dashboard side********************************
dash=Button(text='Dashboard',width=19,height=2,border=0,bg='#363740',fg='white',font=("Inter", 10, "bold"),cursor='hand2',command=dashboard)
dash.place(x=1,y=30)
medicine=Button(text='Medicine',border=0,bg='#363740',fg='white',font=("Inter", 10, "bold"),cursor='hand2',command=medicine)
medicine.place(x=10,y=90)
category=Button(text='Category',width=19,height=2,border=0,bg='#595B67',fg='white',font=("Inter", 10, "bold"),cursor='hand2',command=category)
category.place(x=1,y=130)
categoryimg=PhotoImage(file='category.png')
img=Label(root,image=categoryimg,bg='#595B67')
img.place(x=6,y=135)
# indicator for category
category_indicator=Button(root,text='',bg='#FF702A')
category_indicator.place(x=1,y=130,width=5,height=40)

billing=Button(text='Billing',border=0,bg='#363740',fg='white',font=("Inter", 10, "bold"),cursor='hand2',command=billing)
billing.place(x=10,y=170)
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

# ********total product ****************************
total_product=Label(root,text='Total Category:',fg='#363740',font=("Poppins", 17,"bold"))
total_product.place(x=200,y=80)
add_button=Button(root,text='+ Add Category',border=1,bg='#FF702A',fg='#FAFAFA',font=("Poppins",15),command=add)
add_button.place(x=700,y=80)
# product listing frame
product_frame=Frame(root,bg='#D9D9D9',width=560,height=30,border=20)
product_frame.place(x=400,y=150)
sn=Label(text="S.N",bg='#D9D9D9',font=("poppins",12,"bold"))
sn.place(x=400,y=150)
product_name=Label(text="Category ID",bg='#D9D9D9',font=("poppins",12,"bold"))
product_name.place(x=600,y=150)
fees=Label(text="Category",bg='#D9D9D9',font=("poppins",12,"bold"))
fees.place(x=830,y=150)

Button(root,text='Edit',bg='#FF702A',fg='white',width=6,border=1,font=("Poppins",15),command=update).place(x=870,y=80,height=37)
#  scrollbar to store category name    
categoryListframe=Frame(root,width=700,height=550,bg='#FAFAFA')
categoryListframe.place(x=400,y=185)
scrolly=Scrollbar(categoryListframe,orient=VERTICAL)
categoryarea=Text(categoryListframe,yscrollcommand=scrolly.set,font=("Poppins",10),fg='black')
scrolly.pack(side=RIGHT,fill=Y)
scrolly.config(command=categoryarea.yview)
categoryarea.pack(fill=BOTH,expand=1)



# data base
try:
            con=mysql.connect(host='localhost',user='root',password="saroj@0777",port="3306",database='pharmacy')
            mycursor=con.cursor()
except:
            messagebox.showerror("error","connection error")
            
query='select * from category'
mycursor.execute(query)
row=mycursor.fetchall()
x=1
for i in row:
    b=list(i)
    categoryarea.insert(END,f"\n\n  {x}\t\t\t\t{b[0]}\t\t\t\t{b[1]}")
    x=x+1
       
root.mainloop()