from tkinter import *
from tkinter import messagebox
from PIL import ImageTk # type: ignore
import pymysql # type: ignore
root=Tk()
root.geometry('1530x1000')
root.resizable(0,0)
root.title('LogIn Page')
bgImage=ImageTk.PhotoImage(file="login.jpg")
bgLable=Label(image=bgImage)
bgLable.place(x=0,y=0)
gImage=ImageTk.PhotoImage(file="emp.jpg")
gLable=Label(image=gImage,bd=0,background='green')
gLable.place(x=0,y=550)
g1Image=ImageTk.PhotoImage(file="emp1.jpg")
g1Lable=Label(image=g1Image,bd=0,background='green')
g1Lable.place(x=500,y=550)
g2Image=ImageTk.PhotoImage(file="emp2.jpg")
g2Lable=Label(image=g2Image,bd=0,background='green')
g2Lable.place(x=1000,y=550)

#---------------------------------------------------Create Class Named As Sign_in_Page--------------------------------------------------#

class Sign_in_page:

#--------------------------------------------------------------Function For Chenge Password ----------------------------------------------------#    
    
    
    def change_pass(self):
        if self.userEntry.get()=='' or self.passEntry.get()=='' or  self.cpassEntry.get()=='':
             messagebox.showerror('Error','All fields are required',parent=self.window)
        elif self.passEntry.get()!=self.cpassEntry.get():
            messagebox.showerror('Error','Does not match password',parent=self.window)
        else:
            con=pymysql.connect(host='localhost',user='root',password='Ankit@817raj#',database='train')
            mycursor=con.cursor()
            query='select * from data1 where self.username=%s'
            mycursor.execute(query,(self.userEntry.get()))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror('Error','Incorrect self.username',parent=self.window)
            else:
                query='update data1 set password=%s where self.username=%s'
                mycursor.execute(query,(self.passEntry.get(),self.userEntry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('success','Password has been changed',parent=self.window)
                self.window.destroy()
                
                    
    def forget_pass(self):
        self.window=Toplevel()
        self.window.title('Change Password')
        self.window.geometry("790x512+10+10")
        self.bgPic=ImageTk.PhotoImage(file="background.jpg")
        self.bgLable=Label(self.window,image=self.bgPic)
        self.heading=Label(self.window,text='RESET PASSWORD',font=('arial',18,'bold'),bg='white',fg='magenta2')
        self.heading.place(x=480,y=60)
        self.userLabel=Label(self.window,text="Username:",font=('arial',12,'bold'),bg='white',fg='orchid1')
        self.userLabel.place(x=470,y=130)
        
        self.userEntry=Entry(self.window,width=25,fg='magenta2',font=('arial',11,'bold'),bd=2)
        self.userEntry.place(x=470,y=160)
    
        self.passLabel=Label(self.window,text="New Password:",font=('arial',12,'bold'),bg='white',fg='orchid1')
        self.passLabel.place(x=470,y=190)
    
        self.passEntry=Entry(self.window,width=25,fg='magenta2',font=('arial',11,'bold'),bd=2)
        self.passEntry.place(x=470,y=220)
    
        self.cpassLabel=Label(self.window,text="Confirm Password:",font=('arial',12,'bold'),bg='white',fg='orchid1')
        self.cpassLabel.place(x=470,y=250)
    
        self.cpassEntry=Entry(self.window,width=25,fg='magenta2',font=('arial',11,'bold'),bd=2)
        self.cpassEntry.place(x=470,y=280)
        
    
        self.submitButton=Button(self.window,text='Submit',width=19,font=('Open sans',16,'bold'),bg='magenta2',fg='white',bd=0,activebackground='magenta2',activeforeground='white',cursor='hand2',command=self.change_pass)
        self.submitButton.place(x=470,y=390)    
    
    
    
    
        self.bgLable.grid()
    
        self.window.mainloop()

    def signin_user(self):
        if self.username.get()=='' or self.userpass.get()=='':
               messagebox.showerror('Error','All fields are required') 
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='Ankit@817raj#',database='train')
                mycursor=con.cursor()
            except:
                messagebox.showerror('Error','Database Connectivity Issue, Please Try Again')    
                return
            query='use train'
            mycursor.execute(query)
            query='select * from data1 where username=%s and password=%s'
            mycursor.execute(query,(self.username.get(),self.userpass.get()))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror('Error','Invalid username or Password')
            else:
                messagebox.showinfo('Welcome','Login Successful')
                root.destroy()
                import Admin_page

            
                             
    def signup_page(self):
        root.destroy()
        import Admin_SignUp_file

    def on_enter(self,event):
        if self.username.get()=='Username':
            self.username.delete(0,END)
    def on_passwordenter(self,event):
        if(self.userpass.get()=='Password'):
            self.userpass.delete(0,END)
    def hide(self): 
        self.userpass.config(show='*')  
        self.eyeButton.config(command=self.show); 
    def show(self): 
        self.userpass.config(show='')  
        self.eyeButton.config(command=self.hide);    
        
#------------------------------------------------------------Function Of Main Login Page -----------------------------------------------------        

    def Log__in_page(self):
        self.f1=Frame(root,height=410,width=400,bg="blue")
        self.f1.place(x=550,y=150)
        self.heading=Label(self.f1,text='USER LOGIN',font=('fantasty',25,'bold'),bg='blue',fg='white')
        self.heading.place(x=100,y=10)
    
        self.username=Entry(self.f1,width=31,font=('Arial',14,'bold'),bd=0,fg='blue')
        self.username.place(x=20,y=90)
        self.username.insert(0,'Username')
        self.username.bind('<FocusIn>',self.on_enter)

        self.f3=Frame(self.f1,width=400,height=5,bg='firebrick1').place(x=0,y=70)

        self.userpass=Entry(self.f1,width=31,font=('Arial',14,'bold',),bd=0,fg='blue')
        self.userpass.place(x=20,y=130)
        self.userpass.insert(0,'Password')
        self.userpass.bind('<FocusIn>',self.on_passwordenter)

        self.openeye=ImageTk.PhotoImage(file="openeye.png")
        self.eyeButton=Button(self.f1,image=self.openeye,bg='white',bd=0,activebackground='white',cursor='hand2',command=self.hide)
        self.eyeButton.place(x=337,y=129)

        self.forgotButton=Button(self.f1,text='Forgot Password?',font=('Arial',13,'bold'),bg='blue',fg='white',bd=0,activebackground='white',activeforeground='blue',cursor='hand2',command=self.forget_pass)
        self.forgotButton.place(x=215,y=157)

        self.loginButton=Button(self.f1,text='Login',width=20,font=('Open sans',18,'bold'),bg='firebrick1',fg='white',bd=0,activebackground='firebrick1',activeforeground='white',cursor='hand2',command=self.signin_user)
        self.loginButton.place(x=45,y=200)

        self.onLabel=Label(self.f1,text='--------------------------OR---------------------------',font=('Open Sans',16,'bold'),fg='firebrick1',bg='blue')
        self.onLabel.place(x=0,y=260)

        self.facebook_logo=ImageTk.PhotoImage(file="facebook.png")
        self.facebook=Button(self.f1,image=self.facebook_logo,cursor='hand2',bd=0,bg="white",activebackground='white',background='blue')
        self.facebook.place(x=100,y=310)

        self.google_logo=ImageTk.PhotoImage(file="google.png")
        self.google=Button(self.f1,image=self.google_logo,cursor='hand2',bd=0,bg="white",activebackground='white',background='blue')
        self.google.place(x=200,y=310)

        self.twiter_logo=ImageTk.PhotoImage(file="twitter.png")
        self.twiter=Button(self.f1,image=self.twiter_logo,cursor='hand2',bd=0,bg="white",activebackground='white',background='blue')
        self.twiter.place(x=300,y=310)

       
        self.newaccountButton=Button(self.f1,text='Create new account',font=('Open sans',14,'bold'),bg='blue',fg='white',bd=4,activebackground='blue',activeforeground='white',cursor='hand2',command=self.signup_page)
        self.newaccountButton.place(x=100,y=358)

obj=Sign_in_page()
obj.Log__in_page()
root.mainloop()

