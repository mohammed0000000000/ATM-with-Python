import tkinter
import sqlite3
from tkinter import *
from tkinter import messagebox
import os


master = Tk()
master.title('Banking App')

########### Data Field

def BankData():
    con = sqlite3.connect('Bank.db')
    cursor = con.cursor()
    cursor.execute("""  create table IF NOT EXISTS Bank(
            CodeNO INT PRIMARY KEY NOT NULL,
            fname TEXT,
            mname TEXT,
            lname TEXT,
            age   INT,
            gender  TEXT,
            address TEXT,
            mobile  TEXT,
            password Text,
            cash INT 
            ) """)
    con.commit()
    con.close()
def showAllUsers():
    conn = sqlite3.connect('Bank.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM Bank')
    data = cur.fetchall()
    print(data)
    conn.close()

########### method

def check_age(age):
    temp_age = str(age)
    if temp_age[0] == '0':
        return False
    for x in temp_age:
        if x.isalpha():
            return False
    return True

def check_code(code):
    conn = sqlite3.connect("Bank.db")
    cur = conn.cursor()
    cur.execute("select CodeNo from Bank")
    contain = cur.fetchall()
    #print(AllCode)
    for x in contain:
        if x[0] == code:
            conn.close()
            return False
    conn.close()
    return True

def check_password(pass1,codee):
    temp_code = str(codee)
    temp_pass = str(pass1)
    conn = sqlite3.connect("Bank.db")
    cur = conn.cursor()
    cur.execute('SELECT password FROM Bank WHERE CodeNo LIKE ?', (f'%{temp_code}%',))
    AllCode = cur.fetchall()
    if temp_pass == AllCode[0][0]:
        return True
        conn.close()
    else:
        return False
        conn.close()

def codeIsExist(code):
    conn = sqlite3.connect("Bank.db")
    cur = conn.cursor()
    cur.execute("select CodeNo from Bank")
    contant = cur.fetchall()
    for x in contant:
        if str(x[0]) == code:
            conn.close()
            return True
    conn.close()
    return False

def check_cash(ccash):
    temp_cash = str(ccash)
    if temp_cash[0] == '0':
        return False
    for i in temp_cash:
        if i.isalpha():
            return False
    return True

def get_cash(code):
    conn = sqlite3.connect("Bank.db")
    cur = conn.cursor()
    cur.execute('SELECT cash FROM Bank WHERE CodeNo LIKE ?', (f'%{code}%',))
    contant = cur.fetchall()
    money = contant[0][0]
    conn.close()
    return money



#######  Register Field

def addClient(CodeNo,fname,mname,lname,age,gender,address,phone,password,cash=0):
    con = sqlite3.connect('Bank.db')
    cursor = con.cursor()
    cursor.execute('insert into Bank values (?,?,?,?,?,?,?,?,?,?)',(CodeNo,fname,mname,lname,age,gender,address,phone,password,cash))
    con.commit()
    con.close()

def finish_reg():
    fname = str(FirstName.get())
    mname = str(MiddleName.get())
    lname = str(LastName.get())
    code = str(CodeNo.get())
    pass1 = str(Password1.get())
    pass2 = str(Password2.get())
    phone = str(Phone.get())
    age = str(Age.get())
    gender = str(Gender.get())
    address = str(Address.get())
    cash = 0

    ageFlag = check_age(str(age))
    codeFlag = check_code(code)

    if len(fname) == 0 or len(mname) == 0 or len(lname) == 0 or len(code) == 0 or \
            len(pass1) == 0 or len(pass2) == 0 or len(phone) == 0 or len(str(age)) == 0 or len(gender) == 0 or \
            len(address) == 0:
        messagebox.showerror(title='Error',message="Please !! Complete all Fields .")
    elif ageFlag == False:
        messagebox.showerror(title='Error',message="Age should be only digit .")
    elif len(code) <= 6:
        messagebox.showerror(title='Error',message="The code should be at least 6 digits (:")
    elif codeFlag == False:
        messagebox.showerror(title='Error',message="This code use before Try a new code !!")
    elif len(pass1) <= 9:
        messagebox.showerror(title='Error',message="Password should be at least 10 digits (:")
    elif pass1 != pass2:
        messagebox.showerror(title='Error',message="Two password are different .")
    else:
        addClient(code,fname,mname,lname,age,gender,address,phone,pass1,cash)
        messagebox.showinfo(title='Message',message="Congratulation !!. Successful Login.")

def Register():
    # Vars
    global FirstName
    global MiddleName
    global LastName
    global CodeNo
    global Password1
    global Password2
    global Phone
    global Age
    global Gender
    global Address
    global Cash

    FirstName = StringVar()
    MiddleName = StringVar()
    LastName = StringVar()
    CodeNo = StringVar()
    Password1 = StringVar()
    Password2 = StringVar()
    Phone = StringVar()
    Age = StringVar()
    Gender = StringVar()
    Address = StringVar()
    Cash = IntVar()
    # MainWindow.destroy()
    window = Toplevel(master)
    window.title("Register From")
    window.config(background='#006666')
    Label(window, text="   Create Account ::   ", fg="#FFEEBB", bg='#006666',
          font=("Comic Sans MS", 30, "bold"), padx=15, pady=15, bd=10).grid(row=0, column=0, columnspan=8)

    Label(window, text="First Name :", fg="#FFEEBB", bg='#006666',
          font=("Comic Sans MS", 15, "bold"), padx=3, pady=3, bd=10).grid(row=1, column=0)

    Entry(window, font=("Arial", 15), fg="black", bg="white", textvariable=FirstName).grid(row=1, column=1)

    Label(window, text="Middle Name :", fg="#FFEEBB", bg='#006666',
          font=("Comic Sans MS", 15, "bold"), padx=3, pady=3, bd=10).grid(row=2, column=0)
    Entry(window, font=("Arial", 15), fg="black", bg="white", textvariable=MiddleName).grid(row=2, column=1)

    Label(window, text="Last Name :", fg="#FFEEBB", bg='#006666',
          font=("Comic Sans MS", 15, "bold"), padx=3, pady=3, bd=10).grid(row=3, column=0)
    Entry(window, font=("Arial", 15), fg="black", bg="white", textvariable=LastName).grid(row=3, column=1)

    Label(window, text="Phone :", fg="#FFEEBB", bg='#006666',
          font=("Comic Sans MS", 15, "bold"), padx=3, pady=3, bd=10).grid(row=4, column=0)
    Entry(window, font=("Arial", 15), fg="black", bg="white", textvariable=Phone).grid(row=4, column=1)

    Label(window, text="Address :", fg="#FFEEBB", bg='#006666',
          font=("Comic Sans MS", 15, "bold"), padx=3, pady=3, bd=10).grid(row=5, column=0)
    Entry(window, font=("Arial", 15), fg="black", bg="white", textvariable=Address).grid(row=5, column=1)

    Label(window, text="Age    :", fg="#FFEEBB", bg='#006666',
          font=("Comic Sans MS", 15, "bold"), padx=3, pady=3, bd=10).grid(row=6, column=0)
    Entry(window, font=("Arial", 15), fg="black", bg="white", textvariable=Age).grid(row=6, column=1)

    Label(window, text="Gender :", fg="#FFEEBB", bg='#006666',
          font=("Comic Sans MS", 15, "bold"), padx=3, pady=3, bd=10).grid(row=7, column=0)
    Radiobutton(window, text='Male', variable=Gender, value='male', fg='white', bg='#006666',
                font=("Comic Sans MS", 15, "bold"),
                padx=3, pady=3, bd=10, activeforeground='white', activebackground='#006666').grid(sticky=NW, row=7,
                                                                                                  column=1)

    Radiobutton(window, text='Female', variable=Gender, value='female', fg='white', bg='#006666',
                font=("Comic Sans MS", 15, "bold")
                , padx=3, pady=3, bd=10, activeforeground='white', activebackground='#006666').grid(sticky=NE, row=7,
                                                                                                    column=1)

    Label(window, text='Code No : ', fg="#FFEEBB", bg='#006666', font=("Comic Sans MS", 15, "bold"),
          padx=3, pady=3, bd=10).grid(row=8, column=0)
    Entry(window, font=("Arial", 15), fg="black", bg="white", textvariable=CodeNo).grid(row=8, column=1)

    Label(window, text='Password : ', fg="#FFEEBB", bg='#006666', font=("Comic Sans MS", 15, "bold"),
          padx=3, pady=3, bd=10).grid(row=9, column=0)
    Entry(window, font=("Arial", 15), fg="black", bg="white", textvariable=Password1, show='*').grid(row=9, column=1)

    Label(window, text='confirm Password : ', fg="#FFEEBB", bg='#006666', font=("Comic Sans MS", 15, "bold"),
          padx=3, pady=3, bd=10).grid(row=10, column=0)
    Entry(window, font=("Arial", 15), fg="black", bg="white", show='*', textvariable=Password2).grid(row=10, column=1)

    def Quite():
        window.destroy()
    Button(window, text="Register", command=finish_reg, font=('Comic Sans MS', 15,'bold'),fg='white',bg='#00FF00').grid(row=11,column=1,sticky=EW,pady=10)
    Button(window, text="Cancel", command=Quite, font=('Comic Sans MS', 15,'bold'),fg='white',bg='red').grid(row=12,column=1,sticky=EW,pady=10)



######### Deposit Filed

def depositMoney(DPmoney,DPcode):
    conn = sqlite3.connect("Bank.db")
    cur = conn.cursor()
    temp_code = str(DPcode.get())
    temp_money = int(DPmoney.get())
    cur.execute('SELECT cash FROM Bank WHERE CodeNo LIKE ?', (f'%{temp_code}%',))
    AllCode = cur.fetchall()

    money = AllCode[0][0] + temp_money
    cur.execute('UPDATE Bank SET cash = ? WHERE CodeNo = ?', (money, temp_code))
    conn.commit()
    conn.close()

def deposit():
    dcode = str(codee.get())
    dpassword = str(passwordd.get())
    dcash = int(cash.get())

    if len(dcode) == 0 or len(dpassword) == 0 or dcash == 0:
        messagebox.showerror(title='Error', message='Please Enter Your data')
    elif codeIsExist(dcode) == False:
        messagebox.showerror(title='Error', message='Invalid Account')
    elif check_password(dpassword, dcode) == False:
        messagebox.showerror(title='Error', message='Wrong Password')
    elif check_age(str(dcash)) == False:
        messagebox.showerror(title='Error', message='Amount of Money Must be Integer or only Digit')
    else:
        depositMoney(cash, codee)
        messagebox.showinfo(title='Message', message="Congratulation !!. Successful Deposit.")

def Deposit():
    global codee
    global passwordd
    global cash

    codee = StringVar()
    passwordd = StringVar()
    cash = IntVar()


    Dwindow = Toplevel()
    Dwindow.title("Deposit")
    Dwindow.config(background='#006666')

    Label(Dwindow,text='Deposit Money ::    ', fg="#FFEEBB", bg='#006666',
                   font=("Comic Sans MS", 30, "bold"), padx=15, pady=15, bd=10).grid(row=0,column=0,columnspan=8)
    Label(Dwindow,text='Code No : ', fg="#FFEEBB", bg='#006666',font=("Comic Sans MS", 15, "bold"),
          padx=3, pady=3, bd=10).grid(row=1,column=0)
    Entry(Dwindow,font=("Arial",15),fg="black",bg="white",textvariable=codee).grid(row=1,column=1)

    Label(Dwindow, text='Password : ', fg="#FFEEBB", bg='#006666', font=("Comic Sans MS", 15, "bold"),
          padx=3, pady=3, bd=10).grid(row=2, column=0)
    Entry(Dwindow, font=("Arial", 15), fg="black", bg="white",show='*',textvariable=passwordd).grid(row=2, column=1)

    Label(Dwindow, text='Cash : ', fg="#FFEEBB", bg='#006666', font=("Comic Sans MS", 15, "bold"),
          padx=3, pady=3, bd=10).grid(row=3, column=0)
    Entry(Dwindow, font=("Arial", 15), fg="black", bg="white",textvariable=cash).grid(row=3, column=1)

    def Quite():
        Dwindow.destroy()
    Button(Dwindow,text='Deposit',font=("Comic Sans MS", 15, "bold"),fg="white",bg="#00FF00",command=deposit).grid(sticky=EW,row=5,column=1,padx=20,pady=15)
    Button(Dwindow,text='Cancel',font=("Comic Sans MS", 15, "bold"),fg="white",bg="red",command=Quite).grid(sticky=EW,row=6,column=1,padx=20,pady=15)



################  Withdrawal Field

def Withdrawal_money(codee,cash):
    conn = sqlite3.connect("Bank.db")
    cur = conn.cursor()
    cur.execute('SELECT cash FROM Bank WHERE CodeNo LIKE ?', (f'%{codee}%',))
    contant = cur.fetchall()
    money = contant[0][0] - cash
    if money < 0:
        conn.close()
        return (False)
    else:
        cur.execute('UPDATE Bank SET cash = ? WHERE CodeNo = ?', (money, codee))
        conn.commit()
        conn.close()
        return (True)

def withdrawal():
    Wcode = str(wcode.get())
    Wpass = str(wpassword.get())
    Wcash = str(wcash.get())
    if len(str(Wcash)) == 0 or len(Wpass) == 0 or len(Wcode) == 0:
        messagebox.showerror(title='Error',message='Complete All Fields')
    elif codeIsExist(Wcode) == False:
        messagebox.showerror(title='Error',message='Invalid Account')
    elif check_password(Wpass,Wcode) == False :
        messagebox.showerror(title='Error',message='Invalid Password')
    elif check_cash(Wcash) == False:
        messagebox.showerror(title='Error',message='Cash should by only Digit')
    else:
        if(Withdrawal_money(Wcode,int(Wcash))):
            messagebox.showinfo(title='Message',message='Congratulations !! Successful Withdrawal')
            return
        else:
            messagebox.showerror(title='Error',message="You Don't have enough money .")

def Withdrawal():
    global wcode
    global wpassword
    global wcash

    wcode = StringVar()
    wpassword = StringVar()
    wcash = StringVar()

    Dwindow = Toplevel(master)
    Dwindow.title("Withdrawal")
    window = Frame(Dwindow,background='#006666')
    window.pack()
    Label(window,text='Withdrawal Money ::    ', fg="#FFEEBB", bg='#006666',
                   font=("Comic Sans MS", 30, "bold"), padx=15, pady=15, bd=10).grid(row=0,column=0,columnspan=8)
    Label(window,text='Code No : ', fg="#FFEEBB", bg='#006666',font=("Comic Sans MS", 15, "bold"),
          padx=3, pady=3, bd=10).grid(row=1,column=0)
    Entry(window,font=("Arial",15),fg="black",bg="white",textvariable=wcode).grid(row=1,column=1)

    Label(window, text='Password : ', fg="#FFEEBB", bg='#006666', font=("Comic Sans MS", 15, "bold"),
          padx=3, pady=3, bd=10).grid(row=2, column=0)
    Entry(window, font=("Arial", 15), fg="black", bg="white",textvariable=wpassword).grid(row=2, column=1)

    Label(window, text='cash : ', fg="#FFEEBB", bg='#006666', font=("Comic Sans MS", 15, "bold"),
          padx=3, pady=3, bd=10).grid(row=3, column=0)
    Entry(window, font=("Arial", 15), fg="black", bg="white",textvariable=wcash).grid(row=3, column=1)

    def Quit():
        Dwindow.destroy()

    Button(window,text='Withdrawal',font=("Arial",18,'bold'),fg="white",bg="#00FF00",command=withdrawal).grid(sticky=NW,row=4,column=1,padx=20,pady=10)
    Button(window,text='    Cancel   ',font=("Arial",18,'bold'),fg="white",bg="red",command=Quit).grid(sticky=NW,row=5,column=1,padx=20,pady=10)



############ Equire Field

def enquire():

    Ecode = str(ecode.get())
    Epassword = str(epassword.get())


    if len(Ecode) == 0 or len(Epassword) == 0:
        messagebox.showerror(title='Error',message='Complete All Fields')
    elif codeIsExist(Ecode) == False :
        messagebox.showerror(title='Error',message='Your Account does not exist')
    elif check_password(Epassword,Ecode) == False :
        messagebox.showerror(title='Error',message='Invalid Password')
    else:
        cash = get_cash(Ecode)
        messagebox.showinfo(title='Message',message=f"Your current money = {cash}")
        return

def Enquire():
    global ecode
    global epassword

    ecode = StringVar()
    epassword = StringVar()

    window = Toplevel(master)
    window.title("Enquire")
    window.config(background='#006666')
    Label(window,text='Enquire about Money :: ', fg="#FFEEBB", bg='#006666',
                   font=("Comic Sans MS", 30, "bold"), padx=15, pady=15, bd=10).grid(row=0,column=0,columnspan=8)
    Label(window,text='Code No : ', fg="#FFEEBB", bg='#006666',font=("Comic Sans MS", 15, "bold"),
          padx=3, pady=3, bd=10).grid(row=1,column=0)
    Entry(window,font=("Arial",15),fg="black",bg="white",textvariable=ecode).grid(row=1,column=1)

    Label(window, text='Password : ', fg="#FFEEBB", bg='#006666', font=("Comic Sans MS", 15, "bold"),
          padx=3, pady=3, bd=10).grid(row=2, column=0)
    Entry(window, font=("Arial", 15), fg="black", bg="white",show='*',textvariable=epassword).grid(row=2, column=1)

    def Quit():
        window.destroy()
    Button(window,text='Enquire',font=("Comic Sans MS", 15, "bold"),bg='#33CCFF',fg='black',command=enquire).grid(sticky=EW,row=4,column=1,padx=5,pady=5)
    Button(window,text='Cancel',font=("Comic Sans MS", 15, "bold"),fg="black",bg="red",command=Quit).grid(sticky=EW,row=5,column=1,padx=5,pady=10)




########### Transfer Feild

def transfer():
    Tcode1 = str(tcode1.get())
    Tcode2 = str(tcode2.get())
    Tpassword = str(tpassword.get())
    Tcash = int(tcash.get())

    if len(Tcode1) == 0 or len(Tcode2) == 0 or len(Tpassword) == 0 or len(str(Tcash)) == 0:
        messagebox.showerror(title='Error',message='Complete All Fields .')
    elif codeIsExist(Tcode1) == False :
        messagebox.showerror(title='Error',message='Invalid Sender Account.')
    elif check_password(Tpassword,Tcode1) == False :
        messagebox.showerror(title='Error',message='Invalid Password.')
    elif check_code(str(Tcash)) == False :
        messagebox.showerror(title='Error',message='Cash must be Integer or only Digit.')
    elif codeIsExist(Tcode2) == False :
        messagebox.showerror(title='Error',message='Invalid Receiver Account.')
    else :
        if Withdrawal_money(Tcode1,Tcash) == False :
            messagebox.showerror(title='You do not have enough money in Your Account')
        else:
            depositMoney(tcash,tcode2)
            messagebox.showinfo(title='Message',message='Congratulation Successful Transfer .(')
            return

def Transfer():
    global tcode1
    global tpassword
    global tcash
    global tcode2

    tcode1 = StringVar()
    tcode2 = StringVar()
    tpassword = StringVar()
    tcash = IntVar()

    window = tkinter.Toplevel()
    window.title("Transfer")
    window.config(background='#006666')
    Label(window,text='Transfer Money ::    ', fg="#FFEEBB", bg='#006666',
                   font=("Comic Sans MS", 30, "bold"), padx=15, pady=15, bd=10).grid(row=0,column=0,columnspan=8)
    Label(window,text='Code No : ', fg="#FFEEBB", bg='#006666',font=("Comic Sans MS", 15, "bold"),
          padx=3, pady=3, bd=10).grid(row=1,column=0)
    Entry(window,font=("Arial",15),fg="black",bg="white",textvariable=tcode1).grid(row=1,column=1)

    Label(window, text='Password : ', fg="#FFEEBB", bg='#006666', font=("Comic Sans MS", 15, "bold"),
          padx=3, pady=3, bd=10).grid(row=2, column=0)
    Entry(window, font=("Arial", 15,'bold'), fg="black", bg="white",show='*',textvariable=tpassword).grid(row=2, column=1)

    Label(window, text='cash : ', fg="#FFEEBB", bg='#006666', font=("Comic Sans MS", 15, "bold"),
          padx=3, pady=3, bd=10).grid(row=3, column=0)
    Entry(window, font=("Arial", 15), fg="black", bg="white",textvariable=tcash).grid(row=3, column=1)

    Label(window, text='S Code NO : ', fg="#FFEEBB", bg='#006666', font=("Comic Sans MS", 15, "bold"),
          padx=3, pady=3, bd=10).grid(row=4, column=0)
    Entry(window, font=("Arial", 15), fg="black", bg="white",textvariable=tcode2).grid(row=4, column=1)

    def Quit():
        window.destroy()
    Button(window,text='Transfer',font=("Comic Sans MS", 15, "bold"),fg="black",bg="yellow",command=transfer).grid(sticky=EW,row=5,column=1,padx=20,pady=20)
    Button(window,text='Cancel',font=("Comic Sans MS", 15, "bold"),fg="white",bg="red",command=Quit).grid(sticky=EW,row=6,column=1,padx=20,pady=20)

######### Main Page

BankData()


master.config(background='#006666')
Label(master,text="<< Welcome to i-Bank >>",fg="#FFEEBB",bg='#006666',font=("Comic Sans MS",30,"bold"),padx=3,pady=3,relief=RAISED,bd=10).grid(row=0,column=0,columnspan=3)

Label(master,text='Choose Operation ::',font=('slant',20,'bold'),bg='#006666',fg='#FFEEBB',padx=10,pady=10,relief=GROOVE,bd=10).grid(sticky=NW,column=0,row=1,padx=35)

Button(master,text='Create-Acount',command=Register,font=('slant',20,'bold'),bg='#00FFFF',fg='black',relief=RAISED,bd=7).grid(sticky=NW,column=0,row=2,padx=35)

Button(master,text='    Deposit       ',command=Deposit,font=('slant',20,'bold'),bg='#00FF00',fg='black',relief=RAISED,bd=7).grid(sticky=NW,column=0,row=3,padx=35)

Button(master,text='    Withdrawal ',command=Withdrawal,font=('slant',20,'bold'),bg='#FF0000',fg='black',relief=RAISED,bd=7).grid(sticky=NW,column=0,row=4,padx=35)

Button(master,text='      Enquire     ',command=Enquire,font=('slant',20,'bold'),bg='#33CCFF',fg='black',relief=RAISED,bd=7).grid(sticky=NW,column=0,row=5,padx=35)

Button(master,text='     Transfer     ',command=Transfer,font=('slant',20,'bold'),bg='#FFFF00',fg='black',relief=RAISED,bd=7).grid(sticky=NW,column=0,row=6,padx=35)

Label(master,text='',font=('slant',20,'bold'),bg='#006666',fg='#FFEEBB',padx=10,pady=10).grid(sticky=NW,column=0,row=7)

master.mainloop()