import os
import tempfile
from tkinter import ttk
from tkinter import*
import tkinter.messagebox
import time
import datetime
import random
import sqlite3
root=Tk()
root.maxsize(1360,900)
root.minsize(1300,800)
root.title('New Traffic Rules Fine')
root.configure(bg='Powder Blue')
#heading
top=Frame(root,bg='black',pady=5,bd=10,relief=RIDGE)
top.pack(side=TOP)


menuframe=Frame(root,bg='white',pady=5,bd=10,relief=RIDGE)
menuframe.pack(side=LEFT)
intro2=Frame(menuframe,bg='white',pady=5,bd=10,relief=RIDGE)
intro2.pack(side=LEFT)
intro=Frame(intro2,bg='powder blue',pady=5,bd=10,relief=RIDGE)
intro.grid(row=0,column=0)
intro1=Frame(intro2,bg='black',pady=5,bd=10,relief=RIDGE)
intro1.grid(row=12,column=0)
menu=Frame(menuframe,bg='orange',pady=5,bd=10,relief=RIDGE)
menu.pack(side=TOP)


#int
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()
var11=IntVar()
var12=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()
var19=IntVar()
var20=IntVar()
var21=IntVar()
var22=IntVar()
var23=IntVar()
var24=IntVar()
var25=IntVar()
var26=IntVar()

#var
name=StringVar()
age=StringVar()
gender=StringVar()
re=StringVar()
Date=StringVar()
phone=StringVar()
addr=StringVar()

general1=StringVar()
general2=StringVar()
ticket=StringVar()
violation=StringVar()
disobeying=StringVar()
unautho=StringVar()
drivingw=StringVar()
drivingd=StringVar()
dang=StringVar()
over=StringVar()
drunk=StringVar()
first2=StringVar()
second2=StringVar()
accident=StringVar()
racing=StringVar()
uniserved=StringVar()
taking=StringVar()
causing=StringVar()
#app
coste=StringVar()
Date=StringVar()
Date.set(time.strftime ("%d/%m/%Y"))
re.set(random.randint(100,10000000))
#set
coste.set(' ')
name.set('')
age.set('')
gender.set('')
phone.set('')
addr.set('')
#
general1.set('0')
general2.set('0')
ticket.set('0')
violation.set('0')
disobeying.set('0')
unautho.set('0')
drivingw.set('0')
drivingd.set('0')
dang.set('0')
over.set('0')
drunk.set('0')
first2.set('0')
second2.set('0')
racing.set('0')
accident.set('0')
uniserved.set('0')
taking.set('0')
causing.set('0')
def iExit ():
    iExit=tkinter.messagebox.askyesno ("New Traffic Rules Fine", "Confirm if you want to exit")
    if iExit >= 0:
        root.destroy()
        return
def search():
    if(name.get()!=''):
        e=name.get().lower()
        sw=Tk()
        sw.maxsize(700,700)
        sw.minsize(600,600)
        sw.configure(bg='Powder Blue')
        sw.title('Search Details')
    #----------------------------
        lab1=Label(sw,text='Slip No:',font=('arial 16 bold'),bg='powder blue')
        lab1.grid(row=1,column=0)
        lab2=Label(sw,text='Name:',font=('arial 16 bold'),bg='powder blue')
        lab2.grid(row=0,column=0)
        lab3=Label(sw,text='Age:',font=('arial 16 bold'),bg='powder blue')
        lab3.grid(row=2,column=0)
        lab4=Label(sw,text='Gender:',font=('arial 16 bold'),bg='powder blue')
        lab4.grid(row=3,column=0)
        lab5=Label(sw,text='Phone No:',font=('arial 16 bold'),bg='powder blue')
        lab5.grid(row=4,column=0)
        lab6=Label(sw,text='Address:',font=('arial 16 bold'),bg='powder blue')
        lab6.grid(row=5,column=0)
        lab7=Label(sw,text='Total Fine:',font=('arial 16 bold'),bg='powder blue')
        lab7.grid(row=6,column=0)
        lab8=Label(sw,text='Date of Fine:',font=('arial 16 bold'),bg='powder blue')
        lab8.grid(row=7,column=0)
    #-----------------------------------
        out1=Text(sw,width=15,height=1,font=('arial 16 bold'))
        out1.grid(row=0,column=1)
        out2=Text(sw,width=15,height=1,font=('arial 16 bold'))
        out2.grid(row=1,column=1)
        out3=Text(sw,width=15,height=1,font=('arial 16 bold'))
        out3.grid(row=2,column=1)
        out4=Text(sw,width=15,height=1,font=('arial 16 bold'))
        out4.grid(row=3,column=1)
        out5=Text(sw,width=15,height=1,font=('arial 16 bold'))
        out5.grid(row=4,column=1)
        out6=Text(sw,width=15,height=1,font=('arial 16 bold'))
        out6.grid(row=5,column=1)
        out7=Text(sw,width=15,height=1,font=('arial 16 bold'))
        out7.grid(row=6,column=1)
        out8=Text(sw,width=15,height=1,font=('arial 16 bold'))
        out8.grid(row=7,column=1)
        out9=Text(sw,width=20,height=5,font=('arial 16 bold'))
        out9.grid(row=8,column=1)
        def clk():
            crr=sqlite3.connect('slip.db')
            c=crr.cursor()
            c.execute('select* from slip')
            o=c.fetchall()
            d={}
            for row in o:
                d[row[0]]=row[1],row[2],row[3],row[4],row[5],row[6],row[7]
            try:
                b=d[e]
                slip=b[0]
                age=b[1]
                gender=b[2]
                phone=b[3]
                address=b[4]
                fine=b[5]
                dates=b[6]
                out2.insert(0.0,slip)
                out3.insert(0.0,age)
                out4.insert(0.0,gender)
                out5.insert(0.0,phone)
                out6.insert(0.0,address)
                out7.insert(0.0,fine)
                out8.insert(0.0,dates)
                out9.insert(0.0,'Name Found!')
            except:
                out9.insert(0.0,'Name Not Found!')
            out1.insert(0.0,e)
        
        clk()
        sw.mainloop()
    else:
        tkinter.messagebox.showinfo("program",'Please Enter Name')
def reset():
    
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    coste.set(' ')
    re.set(random.randint(100,10000000))
    name.set('')
    age.set('')
    gender.set('')
    phone.set('')
    addr.set('')
    #
    general1.set('0')
    general2.set('0')
    ticket.set('0')
    violation.set('0')
    disobeying.set('0')
    unautho.set('0')
    drivingw.set('0')
    drivingd.set('0')
    dang.set('0')
    over.set('0')
    drunk.set('0')
    first2.set('0')
    second2.set('0')
    racing.set('0')
    accident.set('0')
    uniserved.set('0')
    taking.set('0')
    causing.set('0')
    #
    sliptxt.configure(state=DISABLED)
    generaltxt2.configure(state=DISABLED)
    ticketxt.configure(state=DISABLED)
    violationtxt.configure(state=DISABLED)
    disobediancetxt.configure(state=DISABLED)
    unauthotxt.configure(state=DISABLED)
    dritxt.configure(state=DISABLED)
    drivtxt.configure(state=DISABLED)
    drivtxt.configure(state=DISABLED)
    overtxt.configure(state=DISABLED)
    dantxt.configure(state=DISABLED)
    drunktxt.configure(state=DISABLED)
   
    secondtxt.configure(state=DISABLED)
    acctxt.configure(state=DISABLED)
    racetxt.configure(state=DISABLED)
    unitxt.configure(state=DISABLED)
    unitxt.configure(state=DISABLED)
    taktxt.configure(state=DISABLED)
    cutxt.configure(state=DISABLED)

            
def receipt():
    a=str(name.get().lower())
    g=str(age.get())
    s=str(gender.get())
    b=str(phone.get())
    c=str(addr.get())
    d=str(coste.get())
    x=str(re.get())
    y=str(Date.get())
    q="insert into slip values"+'('+'"'+a+'"'+','+'"'+x+'"'+','+'"'+g+'"'+','+'"'+s+'"'+','+'"'+b+'"'+','+'"'+c+'"'+','+'"'+d+'"'+','+'"'+y+'"'+')'
    crr=sqlite3.connect('slip.db')
    c=crr.cursor()
    #c.execute("create table slip(Name TEXT,SlipNO TEXT,Age TEXT,Gender TEXT,PhoneNo TEXT,Adress TEXT,TotalFine TEXT,Date TEXT)")
    c.execute(q)
    crr.commit()
    c.close()
    #
    root1=Tk()
    fra=Frame(root1)
    fra.pack(side=TOP)
    root1.title('Receipt')
    txtreceipt=Text (fra,width = 60, height = 100, bg = "dark blue", bd = 4, font = ('arial', 12, 'bold'))
    txtreceipt.grid (row = 0, column = 0)
    root1.maxsize(700,700)
    def code():
        q=txtreceipt.get('1.0','end-1c')
        filename=tempfile.mktemp('.txt')
        open(filename,'w').write(q)
        os.startfile(filename)
    
 

    txtreceipt.insert(END,'Slip No.:\t\t\t\t\t'+re.get()+'\n')
    txtreceipt.insert(END,'Date:    \t\t\t\t\t'+Date.get()+'\n')
    if(name.get()!=''):
        if name.get().isalpha()==True:
            txtreceipt.insert(END,'Name:    \t\t\t\t\t'+name.get()+'\n')
        else:
            tkinter.messagebox.showinfo("program",'Please Enter correct Name !')
            txtreceipt.delete("1.0",END)
            
    if(age.get()!=''):
        
        if age.get().isnumeric() ==True:
            
                if len(age.get())==2:
                    txtreceipt.insert(END,'Age: \t\t\t\t\t'+age.get()+'\n')
                        
                else:
                    tkinter.messagebox.showinfo("program",'Please Enter correct Age !')
                    root1.destroy()
        else:
            tkinter.messagebox.showinfo("program",'Please Enter correct Age !')
            txtreceipt.delete("1.0",END)
            root1.destroy()
    if(gender.get()!=''):
        txtreceipt.insert(END,'Gender:\t\t\t\t\t'+gender.get()+'\n')
    if(phone.get()!=''):
        txtreceipt.insert(END,'Phone No:\t\t\t\t\t'+phone.get()+'\n')
    if(addr.get()!=''):
        
        txtreceipt.insert(END,'Address: \t\t\t\t\t'+addr.get()+'\n')
    txtreceipt.insert(END,'--------------------------------------------------------------------------------------'+'\n')
    
    if (var7.get()==1):
        txtreceipt.insert(END,'General:   \t\t\t\t\t'+str(general2.get())+'\n')
    if (var19.get()==1):
        txtreceipt.insert(END,'Driving when mentally physically unfit to drive:\t'+str(second2.get())+'\n')
    
    if(var10.get()==1):
        txtreceipt.insert(END,'Without Road Tax payer:\t\t\t'+ticket.get()+'\n')
    if(var11.get()==1):
        txtreceipt.insert(END,'Violation of road regulation:\t\t\t'+violation.get()+'\n')
    if(var12.get()==1):
        txtreceipt.insert(END,'Disobediance of order of Authority:\t\t'+disobeying.get()+'\n')
    if(var13.get()==1):
        txtreceipt.insert(END,'Unauthorised use of vehicles without license:\t'+unautho.get()+'\n')
    if(var14.get()==1):
        txtreceipt.insert(END,'Driving Without license:\t\t\t'+drivingw.get()+'\n')
    if(var15.get()==1):
        txtreceipt.insert(END,'Driving despite disqualification:\t\t'+drivingd.get()+'\n')
    if(var16.get()==1):
        txtreceipt.insert(END,'Over-Speeding:\t\t\t\t'+over.get()+'\n')
    if(var17.get()==1):
        txtreceipt.insert(END,'Traffic Light Violation:\t\t\t'+dang.get()+'\n')
    if(var18.get()==1):
        txtreceipt.insert(END,'Drunk Driving:\t\t\t\t'+drunk.get()+'\n')
    if(var22.get()==1):
        txtreceipt.insert(END,'Offence relating to accident:\t\t\t'+accident.get()+'\n')
    if(var23.get()==1):
        txtreceipt.insert(END,'Racing and Speeding:\t\t\t'+racing.get()+'\n')
    if(var24.get()==1):
        txtreceipt.insert(END,'Driving uninsured vechile:\t\t\t'+uniserved.get()+'\n')
    if(var25.get()==1):
        txtreceipt.insert(END,'Taking vechicle without lawful authority:\t'+taking.get()+'\n')
    if(var26.get()==1):
        txtreceipt.insert(END,'Causing obstruction to free flow of traffic:\t'+causing.get()+'\n')
        
    if(var7.get()!=''):
        txtreceipt.insert(END,'------------------------------------------------------------------------------------'+'\n')
        txtreceipt.insert(END,'Total Fine:                                                          '+coste.get()+'\n')
        txtreceipt.insert(END,'--------------------------------------------------------------------------------------'+'\n')
    #txtreceipt.insert(END,'Date:\t'+Date.get()+'\n')
    if(name.get()==''):
        tkinter.messagebox.showinfo("program",'Please Enter Name')
        txtreceipt.delete("1.0",END)
       
    if(age.get()==''):
        tkinter.messagebox.showinfo("program",'Please Enter Age')
        txtreceipt.delete("1.0",END)
        
    if(gender.get()==''):
        tkinter.messagebox.showinfo("program",'Please Enter Gender')
        txtreceipt.delete("1.0",END)
        
    if(len(phone.get())<=9):
        tkinter.messagebox.showinfo("program",'Please Enter Correct Phone No')
        txtreceipt.delete("1.0",END)
        
    if(len(phone.get())>=11):
        tkinter.messagebox.showinfo("program",'Please Enter Correct Phone No')
        txtreceipt.delete("1.0",END)
        
    if(addr.get()==''):
        tkinter.messagebox.showinfo("program",'Please Enter Adress')
        txtreceipt.delete("1.0",END)
      
    if(coste.get()==' '):
        tkinter.messagebox.showinfo("program",'Please Enter Total Fine') 
        txtreceipt.delete("1.0",END)
      
    
    
    code()
    root1.destroy()
    root1.mainloop()

def cost():
    item1=float(general1.get())
    item2=float(general2.get())
    item3=float(ticket.get())
    item4=float(violation.get())
    item5=float(disobeying.get())
    item6=float(unautho.get())
    item7=float(drivingw.get())
    item8=float(drivingd.get())
    item9=float(dang.get())
    item10=float(over.get())
    item11=float(drunk.get())
    item12=float(first2.get())
    item13=float(second2.get())
    item14=float(accident.get())
    item15=float(racing.get())
    item16=float(uniserved.get())
    item17=float(taking.get())
    item18=float(causing.get())
    totals=item1+item2+item3+item4+item5+item6+item7+item8+item9+item10+item11+item12\
            +item13+item14+item15+item16+item17+item18
    totalse='Rs. '+str(totals)
    coste.set(totalse)
    

def generaly():
    if(var7.get()==1):
        generaltxt2.configure(state=NORMAL)
    elif(var7.get()==0):
        generaltxt2.configure(state=DISABLED)
        general2.set('0')
def first1():
    if(var8.get()==1):
        #generaltxt2.configure(state=NORMAL)
        generaltxt2.focus()
        generaltxt2.delete('0',END)
        if(var7.get()==1):
            general2.set(500)
            var9.set(0)
        else:
            general2.set('0')
    elif(var8.get()==0):
        generaltxt2.configure(state=DISABLED)
        general2.set('0')
def second1():
    if(var9.get()==1):
        #generaltxt2.configure(state=NORMAL)
        generaltxt2.focus()
        generaltxt2.delete('0',END)
        if(var7.get()==1):
            general2.set(1500)
            var8.set(0)
        else:
            general2.set('0')
    
    elif(var9.get()==0):
        generaltxt2.configure(state=DISABLED)
        general2.set('0')

def tic():
    if(var10.get()==1):
        ticketxt.configure(state=NORMAL)
        ticketxt.focus()
        ticketxt.delete('0',END)
        ticket.set(500)
    elif(var10.get()==0):
        ticketxt.configure(state=DISABLED)
        ticket.set('0')
def vio():
    if(var11.get()==1):
        violationtxt.configure(state=NORMAL)
        violationtxt.focus()
        violationtxt.delete('0',END)
        violation.set(500)
    elif(var11.get()==0):
        violationtxt.configure(state=DISABLED)
        violation.set('0')
def diso():
    if(var12.get()==1):
        disobediancetxt.configure(state=NORMAL)
        disobediancetxt.focus()
        disobediancetxt.delete('0',END)
        disobeying.set(2000)
    elif(var12.get()==0):
        disobediancetxt.configure(state=DISABLED)
        disobeying.set('0')
def unau():
    if(var13.get()==1):
        unauthotxt.configure(state=NORMAL)
        unauthotxt.focus()
        unauthotxt.delete('0',END)
        unautho.set(5000)
    elif(var13.get()==0):
        unauthotxt.configure(state=DISABLED)
        unautho.set('0')
def drivw():
    if(var14.get()==1):
        dritxt.configure(state=NORMAL)
        dritxt.focus()
        dritxt.delete('0',END)
        drivingw.set(5000)
    elif(var14.get()==0):
        dritxt.configure(state=DISABLED)
        drivingw.set('0')
def drivd():
    if(var15.get()==1):
        drivtxt.configure(state=NORMAL)
        drivtxt.focus()
        drivtxt.delete('0',END)
        drivingd.set(10000)
    elif(var15.get()==0):
        drivtxt.configure(state=DISABLED)
        drivingd.set('0')
def overs():
    if(var16.get()==1):
        overtxt.configure(state=NORMAL)
        overtxt.focus()
        overtxt.delete('0',END)
        over.set(4000)
    elif(var16.get()==0):
        overtxt.configure(state=DISABLED)
        over.set('0')
def dango():
    if(var17.get()==1):
        dantxt.configure(state=NORMAL)
        dantxt.focus()
        dantxt.delete('0',END)
        dang.set(10000)
    elif(var17.get()==0):
        dantxt.configure(state=DISABLED)
        dang.set('0')
def dru():
    if(var18.get()==1):
        drunktxt.configure(state=NORMAL)
        drunktxt.focus()
        drunktxt.delete('0',END)
        drunk.set(10000)
    elif(var18.get()==0):
        drunktxt.configure(state=DISABLED)
        drunk.set('0')

def dre():
    if(var19.get()==1):
        secondtxt.configure(state=NORMAL)
    elif(var19.get()==0):
        secondtxt.configure(state=DISABLED)
        second2.set('0')

def First2():
    if(var20.get()==1):
        #secondtxt.configure(state=NORMAL)
        secondtxt.focus()
        secondtxt.delete('0',END)
        
        if(var19.get()==1):
            second2.set(1000)
            var21.set(0)
        else:
            second2.set('0')
    elif(var20.get()==0):
        secondtxt.configure(state=DISABLED)
        second2.set('0')  
def Second2():
    if(var21.get()==1):
        #secondtxt.configure(state=NORMAL)
        secondtxt.focus()
        secondtxt.delete('0',END)
        
        if(var19.get()==1):
            second2.set(10000)
            var20.set(0)
        else:
            second2.set('0')
    elif(var21.get()==0):
        secondtxt.configure(state=DISABLED)
        second2.set('0')
def accidentee():
    if(var22.get()==1):
        acctxt.configure(state=NORMAL)
        acctxt.focus()
        acctxt.delete('0',END)
        accident.set(5000)
    elif(var22.get()==0):
        acctxt.configure(state=DISABLED)
        accident.set('0')
def race():
    if(var23.get()==1):
        racetxt.configure(state=NORMAL)
        racetxt.focus()
        racetxt.delete('0',END)
        racing.set(5000)
    elif(var23.get()==0):
        racetxt.configure(state=DISABLED)
        racing.set('0')
def unise():
    if(var24.get()==1):
        unitxt.configure(state=NORMAL)
        unitxt.focus()
        unitxt.delete('0',END)
        uniserved.set(5000)
    elif(var24.get()==0):
        unitxt.configure(state=DISABLED)
        uniserved.set('0')
def take():
    if(var25.get()==1):
        taktxt.configure(state=NORMAL)
        taktxt.focus()
        taktxt.delete('0',END)
        taking.set(10000)
    elif(var25.get()==0):
        taktxt.configure(state=DISABLED)
        taking.set('0')
def cause():
    if(var26.get()==1):
        cutxt.configure(state=NORMAL)
        cutxt.focus()
        cutxt.delete('0',END)
        causing.set(10000)
    elif(var26.get()==0):
        cutxt.configure(state=DISABLED)
        causing.set('0')
#labels
head=Label(top,text='\t New Traffic Rules Fine \t\t',bg='royal blue',
           fg='white',font=('broadway 40 bold'),justify=CENTER)
head.grid(row=0,column=0)
#check buttons
cust_name=Label(intro,text='Name:\t',font=('arial 16 bold')
                ,bg='POWDER Blue').grid(row=1,column=0,sticky=W)
Age=Label(intro,text='Age:\t',font=('arial 16 bold'),bg='Powder Blue'
          ).grid(row=2,column=0,sticky=W)
Gender=Label(intro,text='Gender\t',font=('arial 16 bold'),bg='Powder Blue'
             ).grid(row=3,column=0,sticky=W)
Slip=Label(intro,text='Slip No:\t',font=('arial 16 bold'),bg='Powder Blue'
           ).grid(row=0,column=0,sticky=W)
Phone=Label(intro,text='Phone No:',font=('arial 16 bold'),bg='Powder Blue'
            ).grid(row=4,column=0,sticky=W)
Adress=Label(intro,text='Address:',font=('arial 16 bold'),bg='Powder Blue'
             ).grid(row=5,column=0,sticky=W)

#menu
General=Checkbutton(menu,text='General',font=('arial 16 bold'),bg='Orange',
                    variable=var7,onvalue=1,offvalue=0,command=generaly).grid(row=0,column=0,sticky=W)
First1=Checkbutton(menu,text='First-Time',font=('arial 16 bold'),bg='Orange',
                   variable=var8,onvalue=1,offvalue=0,command=first1).grid(row=0,column=1,sticky=W)
Second1=Checkbutton(menu,text='Second-Time',font=('arial 16 bold'),bg='Orange',
                    variable=var9,onvalue=1,offvalue=0,command=second1).grid(row=0,column=2,sticky=W)
 
Ticketless=Checkbutton(menu,text='Without Road Tax payer',font=('arial 16 bold'),
                       variable=var10,onvalue=1,offvalue=0,command=tic,
                       bg='Orange').grid(row=1,column=0,sticky='w')

Violation=Checkbutton(menu,text='Violation of road regulation\t\t\t',font=('arial 16 bold'),
                      variable=var11,onvalue=1,offvalue=0,command=vio,
                      bg='Orange').grid(row=2,column=0,sticky=W)

Disobedience=Checkbutton(menu,text='Disobediance of order of Authority\t\t',font=('arial 16 bold'),
                         bg='Orange',variable=var12,onvalue=1,command=diso,
                         offvalue=0).grid(row=3,column=0,sticky=W)

Unauthorised=Checkbutton(menu,text='Unauthorised use of vehicles without license\t',font=('arial 16 bold')
                         ,variable=var13,offvalue=0,onvalue=1,command=unau,
                         bg='Orange').grid(row=4,column=0,sticky=W)

DrivingW=Checkbutton(menu,text='Driving Without license\t\t\t',font=('arial 16 bold'),
                     bg='Orange',variable=var14,onvalue=1,command=drivw,
                     offvalue=0).grid(row=5,column=0,sticky=W)

Drivingd=Checkbutton(menu,text='Driving despite disqualification\t\t',font=('arial 16 bold'),
                     bg='Orange',variable=var15,onvalue=1,command=drivd,
                     offvalue=0).grid(row=6,column=0,sticky=W)
Over=Checkbutton(menu,text='Over-Speeding\t\t\t\t',font=('arial 16 bold'),bg='Orange',
                 variable=var16,onvalue=1,command=overs,
                 offvalue=0).grid(row=7,column=0,sticky=W)

Dan=Checkbutton(menu,text='Traffic Light Violation \t\t\t\t',font=('arial 16 bold'),bg='Orange',
                variable=var17,onvalue=1,command=dango,
                offvalue=0).grid(row=8,column=0,sticky=W)
Drunk=Checkbutton(menu,text='Drunk Driving\t\t\t\t',font=('arial 16 bold'),bg='Orange',
                  variable=var18,onvalue=1,command=dru,
                  offvalue=0).grid(row=9,column=0,sticky=W)
Dr=Checkbutton(menu,text='Driving when mentally physically unfit to drive \t\t',font=('arial 16 bold'),
               bg='Orange',variable=var19,onvalue=1,command=dre,
               offvalue=0).grid(row=10,column=0,sticky=W)
First=Checkbutton(menu,text='First-Time',font=('arial 16 bold'),bg='Orange',
                  variable=var20,onvalue=1,command=First2,offvalue=0
                  ).grid(row=10,column=1,sticky=W)
Second=Checkbutton(menu,text='Second-Time',font=('arial 16 bold'),bg='Orange',
                   variable=var21,onvalue=1,offvalue=0,command=Second2).grid(row=10,column=2)


Accident=Checkbutton(menu,text='Offence relating to accident\t\t\t',font=('arial 16 bold'),
                     bg='Orange',variable=var22,onvalue=1,command=accidentee,
                     offvalue=0).grid(row=11,column=0,sticky=W)

Racing=Checkbutton(menu,text='Racing and Speeding\t\t\t',font=('arial 16 bold'),
                   bg='Orange',variable=var23,onvalue=1,command=race,
                   offvalue=0).grid(row=12,column=0,sticky=W)

Uniserved=Checkbutton(menu,text='Driving unisured vechile\t\t\t',font=('arial 16 bold'),
                      bg='Orange',variable=var24,onvalue=1,command=unise,
                      offvalue=0).grid(row=13,column=0,sticky=W)

Taking=Checkbutton(menu,text='Taking vechicle without lawful authority\t',font=('arial 16 bold'),
                   bg='Orange',variable=var25,onvalue=1,command=take,
                   offvalue=0).grid(row=14,column=0,sticky=W)
Causing=Checkbutton(menu,text='Causing obstruction to free flow of traffic\t',font=('arial 16 bold'),
                    bg='Orange',variable=var26,onvalue=1,command=cause,
                    offvalue=0).grid(row=15,column=0,sticky=W)
#entry
#generaltxt1=Entry(menu,textvariable=general1,font=('arial 16 bold'),width=5,justify=RIGHT,
                  #state=DISABLED)
#generaltxt1.grid(row=0,column=2)
generaltxt2=Entry(menu,textvariable=general2,font=('arial 16 bold'),width=5,justify=RIGHT,
                  state=DISABLED)
generaltxt2.grid(row=0,column=3)
ticketxt=Entry(menu,textvariable=ticket,font=('arial 16 bold'),width=5,justify=RIGHT,
                    state=DISABLED)
ticketxt.grid(row=1,column=2)
violationtxt=Entry(menu,textvariable=violation,font=('arial 16 bold'),width=5,justify=RIGHT,
                   state=DISABLED)
violationtxt.grid(row=2,column=2)
disobediancetxt=Entry(menu,textvariable=disobeying,font=('arial 16 bold'),width=5,justify=RIGHT,
                      state=DISABLED)
disobediancetxt.grid(row=3,column=2)
unauthotxt=Entry(menu,textvariable=unautho,font=('arial 16 bold'),width=5,justify=RIGHT,
                 state=DISABLED)
unauthotxt.grid(row=4,column=2)
dritxt=Entry(menu,textvariable=drivingw,font=('arial 16 bold'),width=5,justify=RIGHT,
             state=DISABLED)
dritxt.grid(row=5,column=2)
drivtxt=Entry(menu,textvariable=drivingd,font=('arial 16 bold'),width=5,justify=RIGHT,
              state=DISABLED)
drivtxt.grid(row=6,column=2)
overtxt=Entry(menu,textvariable=over,font=('arial 16 bold'),width=5,justify=RIGHT,
              state=DISABLED)
overtxt.grid(row=7,column=2)
dantxt=Entry(menu,textvariable=dang,font=('arial 16 bold'),width=5,justify=RIGHT,
             state=DISABLED)
dantxt.grid(row=8,column=2)
drunktxt=Entry(menu,textvariable=drunk,font=('arial 16 bold'),width=5,justify=RIGHT,
               state=DISABLED)
drunktxt.grid(row=9,column=2)
#firsttxt=Entry(menu,textvariable=first2,font=('arial 16 bold'),width=5,justify=RIGHT,
               #state=DISABLED)
#firsttxt.grid(row=10,column=2)
secondtxt=Entry(menu,textvariable=second2,font=('arial 16 bold'),width=5,justify=RIGHT,
                state=DISABLED)
secondtxt.grid(row=10,column=3)
acctxt=Entry(menu,textvariable=accident,font=('arial 16 bold'),width=5,justify=RIGHT,
             state=DISABLED)
acctxt.grid(row=11,column=2)
racetxt=Entry(menu,textvariable=racing,font=('arial 16 bold'),width=5,justify=RIGHT,
              state=DISABLED)
racetxt.grid(row=12,column=2)
unitxt=Entry(menu,textvariable=uniserved,font=('arial 16 bold'),width=5,justify=RIGHT,
             state=DISABLED)
unitxt.grid(row=13,column=2)
taktxt=Entry(menu,textvariable=taking,font=('arial 16 bold'),width=5,justify=RIGHT,
             state=DISABLED)
taktxt.grid(row=14,column=2)
cutxt=Entry(menu,textvariable=causing,font=('arial 16 bold'),width=5,justify=RIGHT,
            state=DISABLED)
cutxt.grid(row=15,column=2)

sliptxt=Entry(intro,textvariable=re,font=('arial 16 bold'),width=8,justify=LEFT,state=DISABLED)
sliptxt.grid(row=0,column=1)
nametxt=Entry(intro,textvariable=name,font=('arial 16 bold'),width=8,justify=LEFT)
nametxt.grid(row=1,column=1)
agetxt=Entry(intro,textvariable=age,font=('arial 16 bold'),width=8,justify=LEFT)
agetxt.grid(row=2,column=1)

#==============
gendertxt=tkinter.ttk.Combobox(intro,textvariable=gender,font=('arial 16 bold'),
                                state='readonly',width=8,justify=LEFT)
gendertxt.grid(row=3,column=1)
gendertxt['value']=("Select","Male","Female","Transgender")
gendertxt.current(0)
#----------------
phonetxt=Entry(intro,textvariable=phone,font=('arial 16 bold'),width=10,justify=LEFT)
phonetxt.grid(row=4,column=1,sticky=W)
adresstxt=Entry(intro,textvariable=addr,font=('arial 16 bold'),width=10,justify=LEFT)
adresstxt.grid(row=5,column=1,sticky=W)
#lab
lblCost= Label (intro, font = ('arial',14,'bold'), text = "Total Fine:\t ", bg = 'Powder Blue',
                fg = 'black')
lblCost.grid (row=9, column=0, sticky = W)
txtCost= Entry (intro, font = ('arial', 14, 'bold'), textvariable =coste, bd = 7,
                bg ="white",width =10, justify = RIGHT,state=DISABLED)
txtCost.grid (row = 9, column = 1)
date=Label(intro,text='Date:',font=('arial 15 bold'),bg='Powder Blue')
date.grid(row=8,sticky=W)
txtdate=Entry(intro,textvariable=Date,font=('arial 12 bold'),justify=LEFT,width=9,state=DISABLED,
              bd=2)
txtdate.grid(row=8,column=1)



total=Button(intro,bg='cyan',text='Total',padx=5,pady=10,bd=7,width=7,
             font=('arial 16 bold'),command=cost).grid(row=10,column=0,sticky=W)
receipt=Button(intro,bg='cyan',text='Receipt',padx=5,pady=10,bd=7,width=7,
              font=('arial 16 bold'),command=receipt).grid(row=10,column=1,sticky=W)
resets=Button(intro,bg='cyan',text='Reset',padx=5,pady=10,bd=7,width=7,
             font=('arial 16 bold'),command=reset).grid(row=11,column=0,sticky=W)
btnExit=Button(intro,font=('arial 16 bold'),text="Exit",padx=5,pady=10,bd=7,width=7,
                   bg ='Red',command=iExit).grid(row=11,column=1,sticky=W)
btnsearch=Button(intro1,bg='sky blue',padx=16,pady=4,bd=7,font=('arial 20 bold'),width=10,
                 text="Search Name\nDetails",command=search).grid(row=12,column=0)
root.mainloop()

