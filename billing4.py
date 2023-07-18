from tkinter import *
from PIL import ImageTk, Image, ImageDraw
from tkinter import ttk
import mysql.connector as mysql
from tkinter import messagebox
import os,sys
import tempfile
from win32 import win32print
import win32api


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

x=1
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
def search():
    try:
                con=mysql.connect(host='localhost',user='root',password="saroj@0777",port="3306",database='pharmacy')
                mycursor=con.cursor()
    except:
              messagebox.showerror("error","connection error!please add your medicine again")
              return
    quary="select * from user where contactno = %s"
    mycursor.execute(quary,[int(searchentry.get())])
    row=mycursor.fetchone()
    billarea.insert(5.5,row[1])
    billarea.insert(5.75,row[4])
    # user_Address_entry.insert(0,row[4])
    con.commit()
    mycursor.close()
    con.close()
def medsearch():
    global x
    try:
                con=mysql.connect(host='localhost',user='root',password="saroj@0777",port="3306",database='pharmacy')
                mycursor=con.cursor()
    except:
              messagebox.showerror("error","connection error!please add your medicine again")
              return
    quary="select * from medicine where medicineId = %s"
    mycursor.execute(quary,[int(medicineid_entry.get())])
    row=mycursor.fetchone()
    a=row[3]
    q=row[4]-int(qnty_entry.get())
    print(a)
    if q <0:
        messagebox.showerror("error","you don't have this medicine in your stock")
    else:
        medprice=int(qnty_entry.get())*a
        lst.append(medprice)
        billarea.insert(END,f"\n{x}\t\t{row[1]}\t\t{qnty_entry.get()}\t\t{medprice}\t\t{pre_entry.get()}")
        x=x+1
        con.commit()
        mycursor.close()
        con.close()
def total():
    
    space=" "
    b=sum(lst)
    dis=b-(15/100)*b
    billarea.insert(END,f"\n\n\n{space*80} Total: {b}")
    billarea.insert(END,f"\n{space*80} discount %: 15%")
    billarea.insert(END,f"\n{space*80} to pay: {dis}")
def nikal():
    global x
    try:
                con=mysql.connect(host='localhost',user='root',password="saroj@0777",port="3306",database='pharmacy')
                mycursor=con.cursor()
    except:
              messagebox.showerror("error","connection error!please add your medicine again")
              return
    quary="select * from medicine where medicineId = %s"
    mycursor.execute(quary,[int(medicineid_entry.get())])
    row=mycursor.fetchone()
    if row[4]>0:
        qan=row[4]-int(qnty_entry.get())
        quary1="UPDATE medicine SET  quantity= %s where medicineId = %s"
        mycursor.execute(quary1,[qan,int(medicineid_entry.get())])
        con.commit()
        mycursor.close()
        con.close()
    opt=messagebox.askyesno("Bill","DO YOU WANT TO SAVE")
    if opt==True:
        billdata=billarea.get(1.0,END)
        fh=open("bill/"+ billno_entry.get()+".pdf", "w")
        fh.write(billdata)
        fh.close()
        q=billarea.get(1.0,'end -1c')
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename,"print")
        billarea.delete(10.0,END) 
        x=1      
    
lst=[]   
# ***************buttons of the dashboard side********************************
dash=Button(text='Dashboard',width=19,height=2,border=0,bg='#595B67',fg='white',font=("Inter", 10, "bold"),cursor='hand2',command=dashboard)
dash.place(x=1,y=30)
medicine=Button(text='Medicine',border=0,bg='#363740',fg='white',font=("Inter", 10, "bold"),cursor='hand2',command=medicine)
medicine.place(x=10,y=90)
category=Button(text='Category',border=0,bg='#363740',fg='white',font=("Inter", 10, "bold"),cursor='hand2',command=category)
category.place(x=10,y=130)
billing=Button(text='Billing',width=19,height=2,border=0,bg='#595B67',fg='white',font=("Inter", 10, "bold"),cursor='hand2',command=billing)
billing.place(x=1,y=170)
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

# ************************medicine list frame****************************
medicineListframe=Frame(root,width=700,height=550,bg='#FAFAFA')
medicineListframe.place(x=170,y=80)
# old customer search list 
old=Label(root,text='Search customer',fg='black',bg='#FAFAFA',font=("Poppins", 15,"bold"))
old.place(x=1020,y=80)
SEARCH=Label(root,text='contact:',bg='#FAFAFA',fg='black',font=("Poppins", 10))
SEARCH.place(x=950,y=130)
Button(root,text='search',bg='#FF702A',font=("Poppins",10),width=5,command=search).place(x=1170,y=130,height=20)
searchentry=Entry(root,fg='#363740',font=("Poppins", 10),width=20)
searchentry.place(x=1010,y=130,height=20)

# search medicine field
MEDICINE=Label(root,text='Search Medicine',fg='black',bg='#FAFAFA',font=("Poppins", 15,"bold"))
MEDICINE.place(x=1020,y=180)
medicineid=Label(root,text='Medicine ID',fg='black',bg='#FAFAFA',font=("Poppins", 10))
medicineid.place(x=950,y=230)
qnty=Label(root,text='quantity',fg='black',bg='#FAFAFA',font=("Poppins", 10))
qnty.place(x=950,y=270)
qnty_entry=Entry(root,fg='#363740',font=("Poppins", 10),width=20)
qnty_entry.place(x=1030,y=270,height=20)
pre=Label(root,text='Prescription',fg='black',bg='#FAFAFA',font=("Poppins", 10))
pre.place(x=950,y=320)
pre_entry=Entry(root,fg='#363740',font=("Poppins", 10),width=20)
pre_entry.place(x=1030,y=320,height=20)
billno=Label(root,text='Bill no')
billno.place(x=950,y=350)
billno_entry=Entry(root,fg='#363740',font=("Poppins", 10),width=5)
billno_entry.place(x=1030,y=350,height=20)
Button(root,text='add',bg='#FF702A',font=("Poppins",10),width=5,command=medsearch).place(x=1120,y=400,height=20)
medicineid_entry=Entry(root,fg='#363740',font=("Poppins", 10),width=20)
medicineid_entry.place(x=1030,y=230,height=20)


# schrolbar 

scrolly=Scrollbar(medicineListframe,orient=VERTICAL)
billarea=Text(medicineListframe,yscrollcommand=scrolly.set,font=("Poppins",10),fg='black')
scrolly.pack(side=RIGHT,fill=Y)
scrolly.config(command=billarea.yview)
billarea.pack(fill=BOTH,expand=1)
billarea.delete(1.0,END)
billarea.insert(END,"\t\t\t\tABC Pharmacy Store")
billarea.insert(END,"\n\t\t\t       +977-9888888888, 01-890000000")
billarea.insert(END,"\n\t\t\t\tAnamnagar,Kathmandu")
billarea.insert(END,"\n\nName:")
billarea.insert(END,"\t\t\t\tAddress:")
billarea.insert(END,"\n\n\n\nSN")
billarea.insert(END,"\t\tParticular")
billarea.insert(END,"\t\tQTY")
billarea.insert(END,"\t\tPrice")
billarea.insert(END,"\t\tPrescription")


total=Button(root,text='Total',bg='blue',font=("Poppins",12),command=total)
total.place(x=400,y=480)

print_button=Button(root,text='Print',fg='black',bg='green',font=("Poppins",12),command=nikal)
print_button.place(x=640,y=480,width=90,height=35)






root.mainloop()