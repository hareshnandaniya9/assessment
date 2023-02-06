from tkinter import ttk
from tkinter.ttk import *
from tkinter import *
import random
from tkinter import messagebox
from tkinter import scrolledtext
import mysql.connector as mysql

ob=Tk()
ob.title('AA Company')
ob.geometry('1360x690+1+1')
ob.minsize(1375,680)

bg1='black'
bg2='white'
bg3='silver'
bg4='lightgray'
bg5='blue'
bg6='lightgreen'
bg7='lightpink'
bg8='lightblue'
bg9='#165484'           ## brown
bg10='#845100'          ## khakhi
bg11='gray'
bg12='#ff6600'
bg13='#483d8b'
bg14='#b7ceec'
bg15='#125658'          # rama

fg1='brown'
fg2='yellow'
fg3='red'
fg4='green'
fg5='#ffa07a'
fg6='#fa8072'
fg7='#bab86c'
fg8='#151b54'

font1=('Algerian 30 bold underline')
font2=('arial 18 bold')
font3=('arial 15 ')
font33=('arial 13')
font4=('arial 15 bold')
font44=('arial 13 bold')
font5=('corbel 15')
font6=('calibrilight 15')
font7=('corbel 12')
font8=('Elephant 24 bold underline')
font9=('Verdana 12 ')
font10=('Verdana 10')

relief1='flat'
relief2='groove'
relief3='ridge'
relief4='sunken'
relief5='solid'
relief6='raise'

db=mysql.connect(host='localhost',user='root',passwd='',database='aacompany')
cur=db.cursor()

notebook=ttk.Notebook()
notebook.pack(fill='both',expand=1)

logintab=Frame(notebook)
rgtab=Frame(notebook)
sutab=Frame(notebook)
customertab=Frame(notebook)
producttab=Frame(notebook)
transtab=Frame(notebook,bg=bg9)
forgottab=Frame(notebook)
canclefortab=Frame(notebook)
notebook.add(logintab,text='Log In')
notebook.add(rgtab,text='Registration')
notebook.add(sutab,text='Sign Up')
notebook.add(customertab,text='Customer')
notebook.add(producttab,text='Product')
notebook.add(transtab,text='Transaction')

notebook.add(forgottab,text='Forgot')
notebook.add(canclefortab,text='change password')

#notebook.select(logintab)
notebook.select(transtab)
notebook.hide(canclefortab)
notebook.hide(rgtab)
notebook.hide(sutab)
#notebook.hide(customertab)
#notebook.hide(producttab)
#notebook.hide(transtab)
notebook.hide(forgottab)
lst=[]
total=[]
summ=0
###-------------------------------------------------------- LOG IN PAGE ---------------------------------------------------------------###

def login():

    def cancel():
        useret.delete(0,END)
        passet.delete(0,END)

    def submit():
        try:
            cur.execute(" select username,password from login where username='{0}' and password='{1}' ".format(useret.get(),passet.get()))
            res=cur.fetchall()
            if res==[]:
                messagebox.showerror('error','incorrect password')
            else:
                notebook.select(customertab)
                messagebox.showinfo('info','you are successfully login')
                notebook.add(producttab)
                notebook.add(transtab)
                notebook.hide(logintab)
            
        except:
            messagebox.showerror('error','fill both value')

    def registration1():
        notebook.select(rgtab)
        notebook.hide(logintab)

    def forgot():
        notebook.hide(logintab)
        notebook.select(forgottab)
        
    
    logfm=Frame(logintab,bg=bg4,highlightcolor=bg1,highlightbackground=bg11,highlightthickness=1)
    logfm.place(x=450,y=200,width=450,height=250)

    userlb=Label(logfm,text='Username   :',bg=bg4,font=font3)
    userlb.place(x=15,y=25)

    useret=Entry(logfm,font=font33,bd=2,relief=relief1,width=30,highlightthickness=1,highlightcolor=bg5)
    useret.place(x=150,y=25)

    passlb=Label(logfm,text='Password   :',bg=bg4,font=font3)
    passlb.place(x=15,y=65)

    passet=Entry(logfm,font=font33,bd=2,relief=relief1,width=30,highlightthickness=1,highlightcolor=bg5,show='*')
    passet.place(x=150,y=65)

    forgotbt=Button(logfm,text='Forgot password ?',font=font7,bg=bg4,activebackground=bg4,width=15,relief=relief1,fg=bg5,command=forgot)
    forgotbt.place(x=155,y=120)
    
    subbt=Button(logfm,text='Submit',font=font5,bg=bg3,activebackground=bg11,width=8,command=submit)
    subbt.place(x=100,y=155)

    cancelbt=Button(logfm,text='Cancel',font=font5,bg=bg3,activebackground=bg11,width=8,command=cancel)
    cancelbt.place(x=260,y=155)

    resbt=Button(logfm,text='Create new account',font=font7,bg=bg4,activebackground=bg4,width=20,relief=relief1,fg=bg5,command=registration1)
    resbt.place(x=130,y=205)
       
login()

###--------------------------------------------------------  REGISTRATION  ------------------------------------------------------------###
def registration():

    def cancel():

        msg=messagebox.askyesno('warning message','Are you want to cancel create account?')
        if msg==0:
            return
        else:
            fnameet.delete(0,END)
            snameet.delete(0,END)
            qval.set('--------------- SELECT ---------------')
            anset.delete(0,END)
            notebook.select(logintab)
            notebook.hide(rgtab)
        
        

    def signupp():
        if fnameet.get()=='' or snameet.get()=='' or qval.get()=='--------------- SELECT ---------------' or anset.get()=='':
            messagebox.showerror('error in details','fill all detail')
        else:
            fn=fnameet.get()
            sn=snameet.get()
            w=str(random.randint(101,1999))
            useret.insert(0,(fn+sn+w))
            notebook.select(sutab)
            notebook.hide(rgtab)
        
    resfm=Frame(rgtab,bg=bg4,highlightcolor=bg1,highlightbackground=bg11,highlightthickness=1)
    resfm.place(x=450,y=200,width=450,height=250)

    fnamelb=Label(resfm,text='Firstname     :',bg=bg4,font=font3)
    fnamelb.place(x=15,y=25)

    fnameet=Entry(resfm,font=font33,bd=2,relief=relief1,width=30,highlightcolor=bg5,highlightthickness=1)
    fnameet.place(x=150,y=25)

    snamelb=Label(resfm,text='Secondname :',bg=bg4,font=font3)
    snamelb.place(x=15,y=65)

    snameet=Entry(resfm,font=font33,bd=2,relief=relief1,width=30,highlightcolor=bg5,highlightthickness=1)
    snameet.place(x=150,y=65)

    qlb=Label(resfm,text='Question       :',bg=bg4,font=font3)
    qlb.place(x=15,y=105)
    
    qval=StringVar()
    qet=Combobox(resfm,width=28,font=font33,textvariable=qval)
    qet.set('--------------- SELECT ---------------')
    qet.place(x=150,y=105)
    qet.config(value=('Which is your favorite game?','Who is your best friend?','Which is your birth place?','Which is your favorite movie?'))

    anslb=Label(resfm,text='Answer         :',font=font3,bg=bg4)
    anslb.place(x=15,y=145)

    anset=Entry(resfm,font=font33,bd=2,relief=relief1,width=30,highlightcolor=bg5,highlightthickness=1)
    anset.place(x=150,y=145)

    nextbt=Button(resfm,text='Next',width=8,font=font5,bg=bg3,activebackground=bg11,command=signupp)
    nextbt.place(x=100,y=195)

    cancelbt=Button(resfm,text='Cancel',font=font5,bg=bg3,activebackground=bg11,width=8,command=cancel)
    cancelbt.place(x=260,y=195)

    ###-----------------------------------------------  SIGN UP   ------------------------------------------------###

    def can():
        msg=messagebox.askyesno('warning','Are you cancel new account?')
        if msg==1:
            useret.delete(0,END)
            passet.delete(0,END)
            cpasset.delete(0,END)
            notebook.select(rgtab)
            notebook.hide(sutab)
        else:
            return

    def createe():
        if useret.get()=='' or passet.get()=='' or cpasset.get()=='':
            messagebox.showerror('warning','fill all details')
        else:
            msg=messagebox.askyesno('Message about account','Are you sure to create new account?')
            if msg==0:
                return
            else:
                if passet.get()==cpasset.get():
                    fn=fnameet.get()
                    sn=snameet.get()
                    qus=qval.get()
                    ans=anset.get()
                    un=useret.get()
                    pw=passet.get()
                    cur.execute(" insert login(username,password,fname,sname,question,answer) value('{0}','{1}','{2}','{3}','{4}','{5}')".format(un,pw,fn,sn,qus,ans))
                    db.commit()
                    db.close()
                    messagebox.showinfo('information','New account is created')
                    fnameet.delete(0,END)
                    snameet.delete(0,END)
                    qval.set('--------------- SELECT ---------------')
                    anset.delete(0,END)
                    useret.delete(0,END)
                    passet.delete(0,END)
                    cpasset.delete(0,END)
                    notebook.select(logintab)
                    notebook.hide(sutab)
                    
                else:
                    messagebox.showerror('error','password and confirm password are not same')

    sufm=Frame(sutab,bg=bg4,highlightcolor=bg1,highlightbackground=bg11,highlightthickness=1)
    sufm.place(x=450,y=200,width=450,height=250)
    
    userlb=Label(sufm,text='Username   :',bg=bg4,font=font3)
    userlb.place(x=15,y=25)

    useret=Entry(sufm,font=font33,bd=2,relief=relief1,width=30,highlightthickness=1,highlightcolor=bg5)
    useret.place(x=150,y=25)

    passlb=Label(sufm,text='Password   :',bg=bg4,font=font3)
    passlb.place(x=15,y=65)

    passet=Entry(sufm,font=font33,bd=2,relief=relief1,width=30,highlightthickness=1,highlightcolor=bg5)
    passet.place(x=150,y=65)

    cpasslb=Label(sufm,text='Confirm      :',bg=bg4,font=font3)
    cpasslb.place(x=15,y=105)

    cpasslb=Label(sufm,text='password',bg=bg4,font=font3)
    cpasslb.place(x=15,y=135)

    cpasset=Entry(sufm,font=font33,bd=2,relief=relief1,width=30,highlightthickness=1,highlightcolor=bg5)
    cpasset.place(x=150,y=105)

    subbt=Button(sufm,text='Submit',width=8,font=font5,bg=bg3,activebackground=bg11,command=createe)
    subbt.place(x=100,y=195)

    cancelbt1=Button(sufm,text='Cancel',font=font5,bg=bg3,activebackground=bg11,width=8,command=can)
    cancelbt1.place(x=260,y=195)

registration()

###-------------------------------------------------- FORGOT --------------------------------------------------###
def forgot():

    def submit():
        uet=useret.get()
        qet=qval.get()
        aet=anset.get()
        try:
            cur.execute(" select username,question,answer from login where username='{0}' and question='{1}' and answer='{2}' ".format(useret.get(),qval.get(),anset.get()))
            res=cur.fetchall()
            if res==[]:
                messagebox.showerror('warning','incorrect answer')
            else:
                notebook.select(canclefortab)
                notebook.hide(forgottab)
                userett.configure(text=useret.get())
                qet.set('--------------- SELECT ---------------')
                aet.delete(0,END)
        except:
            return

    def cancel():
        notebook.hide(forgottab)
        notebook.select(logintab)

        
    logfm=Frame(forgottab,bg=bg4,highlightcolor=bg1,highlightbackground=bg11,highlightthickness=1)
    logfm.place(x=450,y=200,width=450,height=250)

    userlb=Label(logfm,text='Username    :',bg=bg4,font=font3)
    userlb.place(x=15,y=25)

    useret=Entry(logfm,font=font33,bd=2,relief=relief1,width=30,highlightthickness=1,highlightcolor=bg5)
    useret.place(x=150,y=25)

    qlb=Label(logfm,text='Question       :',bg=bg4,font=font3)
    qlb.place(x=15,y=85)
    
    qval=StringVar()
    qet=Combobox(logfm,width=28,font=font33,textvariable=qval)
    qet.set('--------------- SELECT ---------------')
    qet.place(x=150,y=85)
    qet.config(value=('Which is your favorite game?','Who is your best friend?','Which is your birth place?','Which is your favorite movie?'))

    anslb=Label(logfm,text='Answer         :',font=font3,bg=bg4)
    anslb.place(x=15,y=125)

    anset=Entry(logfm,font=font33,bd=2,relief=relief1,width=30,highlightcolor=bg5,highlightthickness=1)
    anset.place(x=150,y=125)

    subbt=Button(logfm,text='Submit',width=8,font=font5,bg=bg3,activebackground=bg11,command=submit)
    subbt.place(x=100,y=195)

    cancelbt1=Button(logfm,text='Cancel',font=font5,bg=bg3,activebackground=bg11,width=8,command=cancel)
    cancelbt1.place(x=260,y=195)

    def sub():
        if passett.get()=='' or cpassett.get()=='':
            messagebox.showerror('warning','fill all details')

        elif passett.get()!=cpassett.get():
            messagebox.showerror('Error in password','Password and confirm password must be same...')

        else:
            msg=messagebox.askyesno('Message about account','Are you sure to reset password?')
            if msg==0:
                return
            else:
                try:
                    cur.execute(" update login set password='{0}' where username='{1}' ".format(passett.get(),useret.get()))
                    db.commit()
                    messagebox.showinfo('Information','Your password is reset successfully...')
                    notebook.hide(canclefortab)
                    notebook.select(logintab)
                except:
                    return


    def can():
        msg=messagebox.askyesno('warning message...','Are you sure to cancel reset password?')
        if msg==0:
            return
        else:
            passett.delete(0,END)
            cpassett.delete(0,END)
            notebook.hide(canclefortab)
            notebook.select(logintab)  
    
    canfm=Frame(canclefortab,bg=bg4,highlightcolor=bg1,highlightbackground=bg11,highlightthickness=1)
    canfm.place(x=450,y=200,width=450,height=250)
            
    userlbb=Label(canfm,text='Username   :',bg=bg4,font=font3)
    userlbb.place(x=15,y=25)

    userett=Label(canfm,font=font33,bd=2,relief=relief1,width=30,highlightthickness=1,highlightcolor=bg5)
    userett.place(x=150,y=25)

    passlbb=Label(canfm,text='Password   :',bg=bg4,font=font3)
    passlbb.place(x=15,y=65)

    passett=Entry(canfm,font=font33,bd=2,relief=relief1,width=30,highlightthickness=1,highlightcolor=bg5)
    passett.place(x=150,y=65)

    cpasslbb=Label(canfm,text='Confirm      :',bg=bg4,font=font3)
    cpasslbb.place(x=15,y=105)

    cpasslbb=Label(canfm,text='password',bg=bg4,font=font3)
    cpasslbb.place(x=15,y=135)

    cpassett=Entry(canfm,font=font33,bd=2,relief=relief1,width=30,highlightthickness=1,highlightcolor=bg5)
    cpassett.place(x=150,y=105)

    subbtt=Button(canfm,text='Submit',width=8,font=font5,bg=bg3,activebackground=bg11,command=sub)
    subbtt.place(x=100,y=195)

    cancelbtt=Button(canfm,text='Cancel',font=font5,bg=bg3,activebackground=bg11,width=8,command=can)
    cancelbtt.place(x=260,y=195)

forgot()
    

###------------------------------------------------- CUSTOMER DETAILS -----------------------------------------------------###

def customer_detail():
    
    topfm=Frame(customertab,bg=bg3,highlightthickness=2,highlightcolor=bg5,bd=4,relief=relief5)
    topfm.place(x=5,y=5,width=1350,height=95)

    lsidefm=Frame(customertab,bg=bg3,bd=3,relief=relief4)
    lsidefm.place(x=5,y=100,width=450,height=500)

    rsidefm=Frame(customertab,bg=bg3,bd=3,relief=relief4)
    rsidefm.place(x=450,y=100,width=905,height=500)

    lbsidefm=Frame(customertab,bg=bg3,highlightthickness=2,highlightcolor=bg5,bd=3,relief=relief5)
    lbsidefm.place(x=5,y=598,width=450,height=60)

    rbsidefm=Frame(customertab,bg=bg3,highlightthickness=2,highlightcolor=bg5,bd=3,relief=relief5)
    rbsidefm.place(x=450,y=598,width=905,height=60)

    def customer():

        def selectionn(self):
            clearr()
            cidet.delete(0,END)
            focus=tv.focus()
            value=tv.item(focus)['values']
            cidet.insert(0,value[0])
            cnameet.insert(0,value[1])
            cityet.insert(0,value[2])
            mobileet.insert(0,value[3])
            gval.set(value[4])

        def clearr():
            cidet.delete(0,END)
            cnameet.delete(0,END)
            cityet.delete(0,END)
            mobileet.delete(0,END)
            malerb.select()
            cur.execute(" select count(cid)+1 from customer")
            res=cur.fetchall()
            cidet.insert(0,res)

        def displayy():
            cidet.delete(0,END)
            cnameet.delete(0,END)
            cityet.delete(0,END)
            mobileet.delete(0,END)
            malerb.select()
            try:
                cur.execute(" select * from customer")
                res=cur.fetchall()
                if len(res)!=0:
                    tv.delete(*tv.get_children())
                    for a in res:
                        tv.insert('',END,value=a)
                        
                cur.execute(" select count(cid) from customer")
                res=cur.fetchall()
                tcet.configure(text=res)

                cur.execute(" select count(cid)+1 from customer")
                res=cur.fetchall()
                cidet.insert(0,res)
            except:
                return

        def insertt():
            cid=cidet.get()
            cname=cnameet.get()
            city=cityet.get()
            mobile=mobileet.get()
            gender=gval.get()

            msg=messagebox.askyesno('insert new record','are you sure to insert new record?')
            if msg==1:
                try:
                    cur.execute("insert into customer value({0},'{1}','{2}',{3},'{4}')".format(cid,cname,city,mobile,gender))
                    db.commit()
                    messagebox.showinfo('insert record','new record is successfully inserted')
                    displayy()
                    clearr()
                except:
                    return
            else:
                return

        def deletee():
            msg=messagebox.askyesno('warning about to delete','Are you sure to delete selected record?')
            if msg==1:
                try:
                    cur.execute("delete from customer where cid={}".format(cidet.get()))
                    db.commit()
                    displayy()
                    clearr()
                except:
                    return
            else:
                return

        def updatee():
            cid=cidet.get()
            cname=cnameet.get()
            city=cityet.get()
            mobile=mobileet.get()
            gender=gval.get()

            if cidet.get()!='':
                msg=messagebox.askyesno('update record','are you sure to update selected record?')
                if msg==1:
                    try:
                        cur.execute("update customer set cname='{0}',city='{1}',mobile={2},gender='{3}' where cid={4}".format(cname,city,mobile,gender,cid))
                        db.commit()
                        messagebox.showinfo('update record','selected record is successfully updated')
                        displayy()
                        clearr()
                    except:
                        return
                else:
                    return
            else:
                messagebox.showerror('error','please insert Customer ID')


        def searchh():
            cid=cidet.get()
            if cid!='':
                try:
                    cur.execute(" select * from customer where cid={0}".format(cid))
                    res=cur.fetchall()
                    clearr()
                    cidet.delete(0,END)
                    for a in res:
                        cidet.insert(0,a[0])
                        cnameet.insert(0,a[1])
                        cityet.insert(0,a[2])
                        mobileet.insert(0,a[3])
                        gval.set(a[4])
                except:
                    return
            else:
                messagebox.showerror('error in detail','Please insert Customer ID')
                
        toplb=Label(topfm,text='Customer Management',bg=bg3,fg=fg2,font=font1)
        toplb.place(x=450,y=15)

        cidlb=Label(lsidefm,text='Customer ID   :',bg=bg3,font=font44)
        cidlb.place(x=10,y=15)

        cidet=Entry(lsidefm,width=28,bd=1,relief=relief5,highlightcolor=bg1,highlightthickness=1,font=font33)
        cidet.place(x=170,y=15)

        cnamelb=Label(lsidefm,text='Customer name :',bg=bg3,font=font44)
        cnamelb.place(x=10,y=55)

        cnameet=Entry(lsidefm,width=28,bd=1,relief=relief5,highlightcolor=bg1,highlightthickness=1,font=font33)
        cnameet.place(x=170,y=55)

        citylb=Label(lsidefm,text='Customer city :',bg=bg3,font=font44)
        citylb.place(x=10,y=95)

        cityet=Entry(lsidefm,width=28,bd=1,relief=relief5,highlightcolor=bg1,highlightthickness=1,font=font33)
        cityet.place(x=170,y=95)

        mobilelb=Label(lsidefm,text='Mobile No.  :',bg=bg3,font=font44)
        mobilelb.place(x=10,y=135)

        mobileet=Entry(lsidefm,width=28,bd=1,relief=relief5,highlightcolor=bg1,highlightthickness=1,font=font33)
        mobileet.place(x=170,y=135)

        gval=StringVar()
        genderlb=Label(lsidefm,text='Gender    :',bg=bg3,font=font44)
        genderlb.place(x=10,y=175)

        malerb=Radiobutton(lsidefm,text='Male',value='male',variable=gval,width=5,bg=bg3,font=font33)
        malerb.select()
        malerb.place(x=170,y=175)
        

        femalerb=Radiobutton(lsidefm,text='Female',value='female',variable=gval,width=5,bg=bg3,font=font33)
        femalerb.place(x=300,y=175)

        addbt=Button(lsidefm,text='Add',width=8,bd=2,relief=relief3,activebackground=bg11,activeforeground=bg5,font=font2,command=insertt)
        addbt.place(x=15,y=360)

        updatebt=Button(lsidefm,text='Update',width=8,bd=2,relief=relief3,activebackground=bg11,activeforeground=bg5,font=font2,command=updatee)
        updatebt.place(x=155,y=360)

        deletebt=Button(lsidefm,text='Delete',width=8,bd=2,relief=relief3,activebackground=bg11,activeforeground=bg5,font=font2,command=deletee)
        deletebt.place(x=295,y=360)

        displaybt=Button(lsidefm,text='Display',width=8,bd=2,relief=relief3,activebackground=bg11,activeforeground=bg5,font=font2,command=displayy)
        displaybt.place(x=15,y=420)

        searchbt=Button(lsidefm,text='Search',width=8,bd=2,relief=relief3,activebackground=bg11,activeforeground=bg5,font=font2,command=searchh)
        searchbt.place(x=155,y=420)

        clearbt=Button(lsidefm,text='Clear',width=8,bd=2,relief=relief3,activebackground=bg11,activeforeground=bg5,font=font2,command=clearr)
        clearbt.place(x=295,y=420)

        tclb=Label(rbsidefm,text='Total customer  :',bg=bg3,font=font44)
        tclb.place(x=10,y=10)

        tcet=Label(rbsidefm,text='0',bg=bg3,font=font44)
        tcet.place(x=200,y=10)

        tvlb=Label(rsidefm,text='Customer Detail',bg=bg3,font=font8,fg=bg13)
        tvlb.place(x=300,y=20)

        style=ttk.Style()
        style.theme_use('clam')
        style.configure('Treeview',background=bg14,foreground=fg8,rowheight=30,fieldbackground=bg8,font=font9)

        tv=Treeview(rsidefm,column=('cid','cname','city','mobile','gender'),show="headings",height=12)
        tv.place(x=15,y=80)

        tv.column('cid',width=100,minwidth=100,anchor='center')
        tv.column('cname',width=200,stretch=True,minwidth=200)
        tv.column('city',width=200,stretch=True,minwidth=200)
        tv.column('mobile',width=200,stretch=True,minwidth=200,anchor='center')
        tv.column('gender',width=150,minwidth=150,anchor='center')

        tv.heading('cid',text='Customer ID')
        tv.heading('cname',text='Customer Name')
        tv.heading('city',text='Customer City')
        tv.heading('mobile',text='Mobile No.')
        tv.heading('gender',text='Gender')

        tv.bind("<ButtonRelease-1>",selectionn)

        versc=Scrollbar(rsidefm,orient='vertical',command=tv.yview)
        versc.place(x=867,y=80,height=386)
        tv.configure(yscrollcommand=versc.set)

    customer()

customer_detail()

###------------------------------------------------- PRODUCT DETAILS -----------------------------------------------------###

def product_detail():
    
    topfm=Frame(producttab,bg=bg3,highlightthickness=2,highlightcolor=bg5,bd=4,relief=relief5)
    topfm.place(x=5,y=5,width=1350,height=95)

    lsidefm=Frame(producttab,bg=bg3,bd=3,relief=relief4)
    lsidefm.place(x=5,y=100,width=450,height=500)

    rsidefm=Frame(producttab,bg=bg3,bd=3,relief=relief4)
    rsidefm.place(x=450,y=100,width=905,height=500)

    lbsidefm=Frame(producttab,bg=bg3,highlightthickness=2,highlightcolor=bg5,bd=3,relief=relief5)
    lbsidefm.place(x=5,y=598,width=450,height=60)

    rbsidefm=Frame(producttab,bg=bg3,highlightthickness=2,highlightcolor=bg5,bd=3,relief=relief5)
    rbsidefm.place(x=450,y=598,width=905,height=60)

    def product():

        def selectionn(self):
            clearr()
            pidet.delete(0,END)
            focus=tv.focus()
            value=tv.item(focus)['values']
            pidet.insert(0,value[0])
            pnameet.insert(0,value[1])
            priseet.insert(0,value[2])
            qtyet.insert(0,value[3])
            

        def clearr():
            pidet.delete(0,END)
            pnameet.delete(0,END)
            priseet.delete(0,END)
            qtyet.delete(0,END)
            cur.execute(" select count(pid)+1 from product")
            res=cur.fetchall()
            pidet.insert(0,res)

        def displayy():
            pidet.delete(0,END)
            pnameet.delete(0,END)
            priseet.delete(0,END)
            qtyet.delete(0,END)
            try:
                cur.execute(" select * from product")
                res=cur.fetchall()
                if len(res)!=0:
                    tv.delete(*tv.get_children())
                    for a in res:
                        tv.insert('',END,value=a)
                        
                cur.execute(" select count(pid) from product")
                res=cur.fetchall()
                tcet.configure(text=res)

                cur.execute(" select count(pid)+1 from product")
                res=cur.fetchall()
                pidet.insert(0,res)
            except:
                return

        def insertt():
            pid=pidet.get()
            pname=pnameet.get()
            prise=priseet.get()
            qty=qtyet.get()

            msg=messagebox.askyesno('insert new record','are you sure to insert new record?')
            if msg==1:
                try:
                    cur.execute("insert into product value({0},'{1}',{2},{3})".format(pid,pname,prise,qty))
                    db.commit()
                    messagebox.showinfo('insert record','new record is successfully inserted')
                    displayy()
                    clearr()
                except:
                    return
            else:
                return

        def deletee():
            msg=messagebox.askyesno('warning about to delete','Are you sure to delete selected record?')
            if msg==1:
                try:
                    cur.execute("delete from product where pid={}".format(pidet.get()))
                    db.commit()
                    displayy()
                    clearr()
                    
                except:
                    return
            else:
                return               

        def updatee():
            pid=pidet.get()
            pname=pnameet.get()
            prise=priseet.get()
            qty=qtyet.get()

            if pidet.get()!='':
                msg=messagebox.askyesno('update record','are you sure to update selected record?')
                if msg==1:
                    try:
                        cur.execute("update product set pname='{0}',prise={1},qty={2} where pid={3}".format(pname,prise,qty,pid))
                        db.commit()
                        messagebox.showinfo('update record','selected record is successfully updated')
                        displayy()
                        clearr()
                    except:
                        return
                else:
                    return
            else:
                messagebox.showerror('error','please insert Product ID')

        def searchh():
            pid=pidet.get()
            if pid!='':
                try:
                    cur.execute(" select * from product where pid={0}".format(pid))
                    res=cur.fetchall()
                    clearr()
                    pidet.delete(0,END)
                    for a in res:
                        pidet.insert(0,a[0])
                        pnameet.insert(0,a[1])
                        priseet.insert(0,a[2])
                        qtyet.insert(0,a[3])
                        
                except:
                    return
            else:
                messagebox.showerror('error in detail','Please insert Product ID')
                
        toplb=Label(topfm,text='Product Management',bg=bg3,fg=fg2,font=font1)
        toplb.place(x=450,y=15)

        pidlb=Label(lsidefm,text='Product ID   :',bg=bg3,font=font44)
        pidlb.place(x=10,y=15)

        pidet=Entry(lsidefm,width=28,bd=1,relief=relief5,highlightcolor=bg1,highlightthickness=1,font=font33)
        pidet.place(x=170,y=15)

        pnamelb=Label(lsidefm,text='Product name :',bg=bg3,font=font44)
        pnamelb.place(x=10,y=55)

        pnameet=Entry(lsidefm,width=28,bd=1,relief=relief5,highlightcolor=bg1,highlightthickness=1,font=font33)
        pnameet.place(x=170,y=55)

        priselb=Label(lsidefm,text='Product prise :',bg=bg3,font=font44)
        priselb.place(x=10,y=95)

        priseet=Entry(lsidefm,width=28,bd=1,relief=relief5,highlightcolor=bg1,highlightthickness=1,font=font33)
        priseet.place(x=170,y=95)

        qtylb=Label(lsidefm,text='Total quantity  :',bg=bg3,font=font44)
        qtylb.place(x=10,y=135)

        qtyet=Entry(lsidefm,width=28,bd=1,relief=relief5,highlightcolor=bg1,highlightthickness=1,font=font33)
        qtyet.place(x=170,y=135)

        addbt=Button(lsidefm,text='Add',width=8,bd=2,relief=relief3,activebackground=bg11,activeforeground=bg5,font=font2,command=insertt)
        addbt.place(x=15,y=360)

        updatebt=Button(lsidefm,text='Update',width=8,bd=2,relief=relief3,activebackground=bg11,activeforeground=bg5,font=font2,command=updatee)
        updatebt.place(x=155,y=360)

        deletebt=Button(lsidefm,text='Delete',width=8,bd=2,relief=relief3,activebackground=bg11,activeforeground=bg5,font=font2,command=deletee)
        deletebt.place(x=295,y=360)

        displaybt=Button(lsidefm,text='Display',width=8,bd=2,relief=relief3,activebackground=bg11,activeforeground=bg5,font=font2,command=displayy)
        displaybt.place(x=15,y=420)

        searchbt=Button(lsidefm,text='Search',width=8,bd=2,relief=relief3,activebackground=bg11,activeforeground=bg5,font=font2,command=searchh)
        searchbt.place(x=155,y=420)

        clearbt=Button(lsidefm,text='Clear',width=8,bd=2,relief=relief3,activebackground=bg11,activeforeground=bg5,font=font2,command=clearr)
        clearbt.place(x=295,y=420)

        tclb=Label(rbsidefm,text='Total product  :',bg=bg3,font=font44)
        tclb.place(x=10,y=10)

        tcet=Label(rbsidefm,text='0',bg=bg3,font=font44)
        tcet.place(x=200,y=10)

        tvlb=Label(rsidefm,text='Product Detail',bg=bg3,font=font8,fg=bg13)
        tvlb.place(x=300,y=20)

        style=ttk.Style()
        style.theme_use('clam')
        style.configure('Treeview',background=bg14,foreground=fg8,rowheight=30,fieldbackground=bg8,font=font9)

        tv=Treeview(rsidefm,column=('pid','pname','prise','qty','**'),show="headings",height=12)
        tv.place(x=15,y=80)

        tv.column('pid',width=100,minwidth=100,anchor='center')
        tv.column('pname',width=200,stretch=True,minwidth=200)
        tv.column('prise',width=200,stretch=True,minwidth=200)
        tv.column('qty',width=200,stretch=True,minwidth=200,anchor='center')
        tv.column('**',width=150,minwidth=150,anchor='center')

        tv.heading('pid',text='Product ID')
        tv.heading('pname',text='Product Name')
        tv.heading('prise',text='Product prise')
        tv.heading('qty',text='Total quantity')
        tv.heading('**',text='**')

        tv.bind("<ButtonRelease-1>",selectionn)

        versc=Scrollbar(rsidefm,orient='vertical',command=tv.yview)
        versc.place(x=867,y=80,height=386)
        tv.configure(yscrollcommand=versc.set)

    product()

product_detail()

###---------------------------------------------------- TRANSACTION DETAILS -----------------------------------------------------###

def transaction():

    topfm=Frame(transtab,bg=bg3,bd=3,relief=relief6)
    topfm.place(x=5,y=5,width=1350,height=80)

    secondfm=Frame(transtab,bg=bg3,bd=2,relief=relief6)
    secondfm.place(x=5,y=90,width=300,height=210)

    secondrfm=Frame(transtab,bg=bg3,bd=2,relief=relief6)
    secondrfm.place(x=310,y=90,width=935,height=265)

    secondrrfm=Frame(transtab,bg=bg3,bd=2,relief=relief6)
    secondrrfm.place(x=1250,y=150,width=105,height=210)

    thirdfm=Frame(transtab,bg=bg3,bd=2,relief=relief6)
    thirdfm.place(x=5,y=360,width=1350,height=300)

    lbsidefm=Frame(transtab,bg=bg3,bd=2,relief=relief6)
    lbsidefm.place(x=5,y=305,width=300,height=50)
    
    def trans():

        #---------------------------- event handling ---------------------------#
        def pnameevent(e):
            pname1et.delete(0,END)
            try:
                cur.execute(" select product.pname from product where product.pid={0}".format(pid1et.get()))
                res=cur.fetchall()
                pname1et.insert(0,res[0])
            except:
                messagebox.showerror('Show error in Product ID','Insert Currect Product ID')

            prise1et.delete(0,END)
            try:
                cur.execute(" select product.prise from product where product.pid={0}".format(pid1et.get()))
                res=cur.fetchall()
                prise1et.insert(0,res[0])
            except:
                messagebox.showerror('Show error in Product ID','Insert Currect Product ID')


        def amountevent(e):
            amount1et.delete(0,END)
            p=float(prise1et.get())
            q=int(qty1et.get())
            d=float(dis1et.get())
            totalamount=((p*q)-(p*d*q/100))
            amount1et.insert(0,totalamount)
            global summ
            summ+=float(amount1et.get())
            talbb.configure(text=round(summ,3))
        
        #-----------------------------------------------------------------------#


        def transaction_entry():
            try:
                cur.execute(" select cid from trans group by cid")
                res=cur.fetchall()
                a=len(res)+1
                tidet.insert(0,a)
                
            except:
                return
               
        def customer_detail():
            cid=cidet.get()
            cnameet.delete(0,END)
            cityet.delete(0,END)
            mobileet.delete(0,END)
            tidet.delete(0,END)
            transaction_entry()
            try:
                cur.execute("select cname,city,mobile from customer where cid={0}".format(cid))
                res=cur.fetchall()
                for a in res:
                    cnameet.insert(0,a[0])
                    cityet.insert(0,a[1])
                    mobileet.insert(0,a[2])
            except:
                return

        def trans_display():
            pass
        
        def trans_clear():
            pid1et.delete(0,END)
            pname1et.delete(0,END)
            prise1et.delete(0,END)
            qty1et.delete(0,END)
            dis1et.delete(0,END)
            amount1et.delete(0,END)
        
        def trans_insert():
            msg=messagebox.askyesno('Warning to insert record','Are you sure to insert new transaction record?')
            if msg==0:
                return
            else:
                addentry()
                p=pid1et.get()
                x=0
                for w in range(len(total)//6):
                    try:
                        cur.execute(" insert into trans(tid,cid,pid,pname,prise,qty,disc,amount) value({0},{1},{2},'{3}',{4},{5},{6},{7})".format(tidet.get(),cidet.get(),total[x+0],total[x+1],total[x+2],total[x+3],total[x+4],total[x+5]))                                     
                        db.commit()
                        x+=6
                    except Exception as ex:
                        print(ex)
                        
                total.clear()
                lst.clear()
                transaction_entry()

        def trans_update():
            return
        
        def addentry():
            global lst,total
            if  amount1et.get()=='':
                messagebox.showerror('Error in entry','Please insert transaction value')
            else:
                try:
                    a=pid1et.get()
                    b=pname1et.get()
                    c=prise1et.get()
                    d=qty1et.get()
                    e=dis1et.get()
                    f=amount1et.get()
                    lst.append(a)
                    lst.append(b)
                    lst.append(c)
                    lst.append(d)
                    lst.append(e)
                    lst.append(f)
                    total.append(a)
                    total.append(b)
                    total.append(c)
                    total.append(d)
                    total.append(e)
                    total.append(f)
                    
                    tvv.insert('',END,value=lst)
                    trans_clear()
                except:
                    pass
                lst.clear()

        def trans_delete():
            msg=messagebox.askyesno('Warning to delete record','Are you sure to delete transaction record?')
            if msg==0:
                return
            else:
                cid=cidet.delete(0,END)
                cnameet.delete(0,END)
                cityet.delete(0,END)
                mobileet.delete(0,END)
                trans_clear()
                lst.clear()
                total.clear()
                #tv.delete()
                transaction_entry()

#----- Top Label -----#
        toplb=Label(topfm,text='Transaction Management',bg=bg3,fg=fg2,font=font1)
        toplb.place(x=400,y=10)
        
#----- Customer Label and Entry -----#
        cidlb=Label(secondfm,text='Customer ID :',bg=bg3,font=font44)
        cidlb.place(x=10,y=5)

        cidet=Entry(secondfm,width=10,bd=1,relief=relief5,highlightcolor=bg1,highlightthickness=1,font=font33)
        cidet.place(x=130,y=5)

        cidbt=Button(secondfm,text='Click',bd=2,relief=relief3,activebackground=bg3,font=font10,bg=bg11,fg=fg2,command=customer_detail)
        cidbt.place(x=230,y=5)

        cnamelb=Label(secondfm,text='Name            :',bg=bg3,font=font44)
        cnamelb.place(x=10,y=45) 

        cnameet=Entry(secondfm,width=15,bd=1,relief=relief5,highlightcolor=bg1,highlightthickness=1,font=font33)
        cnameet.place(x=130,y=45)

        citylb=Label(secondfm,text='City              :',bg=bg3,font=font44)
        citylb.place(x=10,y=85)

        cityet=Entry(secondfm,width=15,bd=1,relief=relief5,highlightcolor=bg1,highlightthickness=1,font=font33)
        cityet.place(x=130,y=85)

        mobilelb=Label(secondfm,text='Mobile          :',bg=bg3,font=font44)
        mobilelb.place(x=10,y=125)

        mobileet=Entry(secondfm,width=15,bd=1,relief=relief5,highlightcolor=bg1,highlightthickness=1,font=font33)
        mobileet.place(x=130,y=125)

        tidlb=Label(secondfm,text='Transaction  :',bg=bg3,font=font44)
        tidlb.place(x=10,y=165)

        tidet=Entry(secondfm,width=15,bd=1,relief=relief5,highlightcolor=bg1,highlightthickness=1,font=font33)
        tidet.place(x=130,y=165)

        talb=Label(lbsidefm,text='Total Amount :',bg=bg3,font=font44)
        talb.place(x=10,y=10)

        talbb=Label(lbsidefm,text='   Total   ',bg=bg3,font=font44)
        talbb.place(x=130,y=10)

#----- Transaction Label -----#
        pidlb=Label(secondrfm,text='Product ID',bg=bg4,font=font33,relief=relief3,width=10)
        pidlb.place(x=20,y=5)

        pnamelb=Label(secondrfm,text='Product name',bg=bg4,font=font33,relief=relief3,width=26)
        pnamelb.place(x=135,y=5)

        priselb=Label(secondrfm,text='Prise',bg=bg4,font=font33,relief=relief3,width=10)
        priselb.place(x=400,y=5)

        qtylb=Label(secondrfm,text='Qty.',bg=bg4,font=font33,relief=relief3,width=10)
        qtylb.place(x=520,y=5)

        dislb=Label(secondrfm,text='Dis.',bg=bg4,font=font33,relief=relief3,width=10)
        dislb.place(x=640,y=5)

        amountlb=Label(secondrfm,text='Amount',bg=bg4,font=font33,relief=relief3,width=15)
        amountlb.place(x=760,y=5)
        
#----- Entry -----#
        pid1et=Entry(secondrfm,width=10,bd=1,relief=relief5,highlightcolor=bg1,highlightthickness=1,font=font33)
        pid1et.place(x=20,y=45)
        pid1et.bind("<FocusOut>",pnameevent)

        pname1et=Entry(secondrfm,width=26,bd=1,relief=relief5,highlightcolor=bg1,highlightthickness=1,font=font33)
        pname1et.place(x=135,y=45)

        prise1et=Entry(secondrfm,width=10,bd=1,relief=relief5,highlightcolor=bg1,highlightthickness=1,font=font33)
        prise1et.place(x=400,y=45)

        qty1et=Entry(secondrfm,width=10,bd=1,relief=relief5,highlightcolor=bg1,highlightthickness=1,font=font33)
        qty1et.place(x=520,y=45)

        dis1et=Entry(secondrfm,width=10,bd=1,relief=relief5,highlightcolor=bg1,highlightthickness=1,font=font33)
        dis1et.place(x=640,y=45)
        dis1et.bind("<FocusOut>",amountevent)

        amount1et=Entry(secondrfm,width=15,bd=1,relief=relief5,highlightcolor=bg1,highlightthickness=1,font=font33)
        amount1et.place(x=760,y=45)        

#----- Buttons------#
        addbt=Button(secondrrfm,text='Add',bd=3,relief=relief3,activebackground=bg3,font=font44,bg=bg15,fg=bg2,width=10,command=addentry)
        addbt.pack(pady=1)
        
        displaybt=Button(secondrrfm,text='Display',bd=3,relief=relief3,activebackground=bg3,font=font44,bg=bg15,fg=bg2,width=10,command=trans_display)
        displaybt.pack()

        Insertbt=Button(secondrrfm,text='Insert',bd=3,relief=relief3,activebackground=bg3,font=font44,bg=bg15,fg=bg2,width=10,command=trans_insert)
        Insertbt.pack()

        Updatebt=Button(secondrrfm,text='Update',bd=3,relief=relief3,activebackground=bg3,font=font44,bg=bg15,fg=bg2,width=10,command=trans_update)
        Updatebt.pack()

        deletebt=Button(secondrrfm,text='Delete',bd=3,relief=relief3,activebackground=bg3,font=font44,bg=bg15,fg=bg2,width=10,command=trans_delete)
        deletebt.pack()

        clearbt=Button(secondrrfm,text='Clear',bd=3,relief=relief3,activebackground=bg3,font=font44,bg=bg15,fg=bg2,width=10,command=trans_clear)
        clearbt.pack()
#--------

        style=ttk.Style()
        style.theme_use('clam')
        style.configure('Treeview',background=bg14,foreground=fg8,rowheight=30,fieldbackground=bg8,font=font9)

        tvv=Treeview(secondrfm,column=('pidd','pnamee','prisee','qtyy','discountt','amountt'),show='headings')
        tvv.place(x=20,y=80,height=170,width=887)

        tvv.column('pidd',width=104,minwidth=104,anchor='center',stretch=0)
        tvv.column('pnamee',width=264,minwidth=264,anchor='center',stretch=0)
        tvv.column('prisee',width=120,minwidth=120,anchor='center',stretch=0)
        tvv.column('qtyy',width=120,minwidth=120,anchor='center',stretch=0)
        tvv.column('discountt',width=120,minwidth=120,anchor='center',stretch=0)
        tvv.column('amountt',width=155,minwidth=155,anchor='center',stretch=0)

        tvv.heading('pidd',text='Product ID')
        tvv.heading('pnamee',text='Product name')
        tvv.heading('prisee',text='Product prise')
        tvv.heading('qtyy',text='Quantity')
        tvv.heading('discountt',text='Discount')
        tvv.heading('amountt',text='Amount')

        verscc=Scrollbar(secondrfm,orient='vertical',command=tvv.yview)
        verscc.place(x=907,y=82,height=168)
        tvv.configure(yscrollcommand=verscc.set)

        tv=Treeview(thirdfm,column=('tid','cid','pid','pname','prise','qty','discount','amount'),show='headings')
        tv.place(x=5,y=10,height=260,width=1315)
                    
        tv.column('tid',width=70,minwidth=50,anchor='center',stretch=1)
        tv.column('cid',width=70,minwidth=50,anchor='center',stretch=1)
        tv.column('pid',width=70,minwidth=50,anchor='center',stretch=1)
        tv.column('pname',width=170,minwidth=100,anchor='e',stretch=False)
        tv.column('prise',width=100,minwidth=70,anchor='center',stretch=1)
        tv.column('qty',width=70,minwidth=50,anchor='center',stretch=1)
        tv.column('discount',width=70,minwidth=50,anchor='center',stretch=1)
        tv.column('amount',width=100,minwidth=70,anchor='center',stretch=0)
 
        tv.heading('tid',text='tid')
        tv.heading('cid',text='cid')
        tv.heading('pid',text='pid')
        tv.heading('pname',text='pname')
        tv.heading('prise',text='prise')
        tv.heading('qty',text='qty')
        tv.heading('discount',text='dis')
        tv.heading('amount',text='amount')

        horscr=Scrollbar(thirdfm,orient='horizontal',command=tv.xview)
        horscr.place(x=5,y=270,width=1320,height=15)
        tv.configure(xscrollcommand=horscr.set)

        versc=Scrollbar(thirdfm,orient='vertical',command=tv.yview)
        versc.place(x=1320,y=10,height=260)
        tv.configure(yscrollcommand=versc.set)

    trans()

transaction()

ob.mainloop()
