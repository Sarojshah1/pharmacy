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
    import medicine2
    
# add function
def update():
    top=Toplevel(root)
    top.title("update medicine credentials")
    top.geometry(f"{width_screen}x{height_screen}")
    top.iconbitmap('medicine.ico')
    top.state('zoomed')
    def edit():
        if user_name_entry.get()=='' and user_price_entry.get()=='':
            messagebox.showerror("error","please fill all fields")
        else:
            try:
                con=mysql.connect(host='localhost',user='root',password="saroj@0777",port="3306",database='pharmacy')
                mycursor=con.cursor()
            except:
                messagebox.showerror("error","connection error")
                return
        try:
            vals={
                    
                    "name": user_name_entry.get(),
                    "price":user_price_entry.get(),
                    "category": user_category_entry.get(),
                    "quantity":quantity_entry.get(),
                    "medicineId":medid.get()
            }
            query='UPDATE medicine  SET name=%s,price=%s,quantity=%s,category=%s WHERE medicineId=%s',(vals['name'],int(vals['price']),vals['quantity'],vals['category'],vals['medicineId'])

            mycursor.execute(*query)
            con.commit()
            mycursor.close()
            con.close()
            user_name_entry.delete(0,'end')
            user_price_entry.delete(0,'end')
            user_category_entry.delete(0,'end')
            quantity_entry.delete(0,'end')
        except:
            user_name_entry.delete(0,'end')
            user_price_entry.delete(0,'end')
            user_category_entry.delete(0,'end')
            quantity_entry.delete(0,'end')
    def search():
        user_name_entry.delete(0,'end')
        user_price_entry.delete(0,'end')
        user_category_entry.delete(0,'end')
        quantity_entry.delete(0,'end')
        # data base
        try:
                con=mysql.connect(host='localhost',user='root',password="saroj@0777",port="3306",database='pharmacy')
                mycursor=con.cursor()
        except:
              messagebox.showerror("error","connection error!please add your medicine again")
              return
        quary="select * from medicine where medicineId = %s"
        mycursor.execute(quary,[int(medid.get())])
        row=mycursor.fetchone()
        user_name_entry.insert(0,row[1])
        user_price_entry.insert(0,row[3])
        user_category_entry.insert(0,row[2])
        quantity_entry.insert(0,row[4])
        con.commit()
        mycursor.close()
        con.close()
    def quit():
        top.destroy()
        # *******header frame *******
    frame1=Frame(top,bg='#FAFAFA')
    frame1.place(x=0,y=0,width=700,height=60)


    # ***********heading********************************
    heading=Label(frame1,text='ABC Pharmacy Store',bg='#FAFAFA',fg='black',font=("camb",20,'bold'))
    heading.place(x=100,y=5)


    # ********add medicine product ****************************
    add_medicine=Label(top,text='Update Medicine',fg='#363740',font=("Poppins", 20,"bold"))
    add_medicine.place(x=600,y=150)
    info=Label(top,text='Information',fg='#363740',font=("Poppins", 15,"bold"))
    info.place(x=200,y=200)
    a=Label(top,text='________________________________________________________________________________________________________________________________________________________________________________________________')
    a.place(x=190,y=230)
    user_name=Label(top,text='Name',fg='#363740',width=5,font=("Poppins",15))
    user_name.place(x=190,y=300)
    user_name_entry=Entry(top,text='',width=100)
    user_name_entry.place(x=400,y=300,height=35)

    user_category=Label(top,text='category',fg='#363740',font=("Poppins",15))
    user_category.place(x=190,y=350)
    user_category_entry=Entry(top,text='',width=100)
    user_category_entry.place(x=400,y=350,height=35)

    user_price=Label(top,text='Price',fg='#363740',font=("Poppins",15))
    user_price.place(x=190,y=400)
    user_price_entry=Entry(top,text='',width=100)
    user_price_entry.place(x=400,y=400,height=35)
    
    quantity=Label(top,text='quantity',fg='#363740',font=("Poppins",15))
    quantity.place(x=190,y=450)
    quantity_entry=Entry(top,text='',width=100)
    quantity_entry.place(x=400,y=450,height=35)
    
    med=Label(top,text='Medicine Id',fg='#363740',font=("Poppins",10))
    med.place(x=950,y=200)
    medid=Entry(top,text='',width=10)
    medid.place(x=1030,y=200,height=20)
    Button(top,text='search',bg='#FF702A',width=5,command=search).place(x=1120,y=200,height=20)


    save_button=Button(top,text='Update',border=1,width=15,height=2,bg='#3ECF0A',fg='#FAFAFA',font=("Poppins",10),command=edit)
    save_button.place(x=880,y=500)
    quit=Button(top,text='Quit',border=1,width=15,height=2,bg='red',fg='#FAFAFA',font=("Poppins",10),command=quit)
    quit.place(x=200,y=500)

    top.mainloop()
    
# ***************buttons of the dashboard side********************************
dash=Button(text='Dashboard',width=19,height=2,border=0,bg='#363740',fg='white',font=("Inter", 10, "bold"),cursor='hand2',command=dashboard)
dash.place(x=1,y=30)
medicine=Button(text='Medicine',width=19,height=2,border=0,bg='#595B67',fg='white',font=("Inter", 10, "bold"),cursor='hand2',command=medicine)
medicine.place(x=1,y=90)
medicineimg=PhotoImage(file='medicine.png')
img=Label(root,image=medicineimg,bg='#595B67')
img.place(x=5,y=95)
# indicator for medicine
medicine_indicator=Button(root,text='',bg='#FF702A')
medicine_indicator.place(x=1,y=90,width=5,height=40)
category=Button(text='Category',border=0,bg='#363740',fg='white',font=("Inter", 10, "bold"),cursor='hand2',command=category)
category.place(x=10,y=130)
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
total_product=Label(root,text='Total Product:',fg='#363740',font=("Poppins", 17,"bold"))
total_product.place(x=200,y=80)
add_button=Button(root,text='+ Add Product',border=1,bg='#FF702A',fg='#FAFAFA',font=("Poppins",15),command=add)
add_button.place(x=750,y=80)
# product listing frame
product_frame=Frame(root,bg='#D9D9D9',width=730,height=30,border=20)
product_frame.place(x=300,y=140)
sn=Label(text="S.N",bg='#D9D9D9',font=("poppins",12,"bold"))
sn.place(x=300,y=140)
id=Label(text="Medicine ID",bg='#D9D9D9',font=("poppins",12,"bold"))
id.place(x=380,y=140)

product_name=Label(text="Name",bg='#D9D9D9',font=("poppins",12,"bold"))
product_name.place(x=530,y=140)
product_category=Label(text="Category",bg='#D9D9D9',font=("poppins",12,"bold"))
product_category.place(x=730,y=140)
fees=Label(text="Price",bg='#D9D9D9',font=("poppins",12,"bold"))
fees.place(x=940,y=140)
frame10=Frame(root,width=980,height=400,border=20)
frame10.place(x=200,y=240)
Button(root,text='Edit',bg='#FF702A',fg='white',width=6,border=1,font=("Poppins",15),command=update).place(x=950,y=80,height=37)
# schrolbar 
medicineListframe=Frame(root,width=720,height=550,bg='#FAFAFA')
medicineListframe.place(x=300,y=190)
scrolly=Scrollbar(medicineListframe,orient=VERTICAL)
medicinearea=Text(medicineListframe,yscrollcommand=scrolly.set,font=("Poppins",13),fg='black')
scrolly.pack(side=RIGHT,fill=Y)
scrolly.config(command=medicinearea.yview)
medicinearea.pack(fill=BOTH,expand=1)

# data base
try:
            con=mysql.connect(host='localhost',user='root',password="saroj@0777",port="3306",database='pharmacy')
            mycursor=con.cursor()
except:
            messagebox.showerror("error","connection error")
            
query='select * from medicine'
mycursor.execute(query)
row=mycursor.fetchall()
x=1
for i in row:
    b=list(i)
    medicinearea.insert(END,f"\n\n{x}                 {b[0]}\t\t\t{b[1]}\t\t\t{b[2]}\t\t\t{b[3]}")
    x=x+1
con.commit()
mycursor.close()
con.close()
       




root.mainloop()