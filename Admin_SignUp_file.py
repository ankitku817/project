from tkinter import *
from tkinter import messagebox
from PIL import ImageTk # type: ignore
import pymysql # type: ignore


root=Tk()
root.geometry('1530x1000')
root.resizable(0,0)
root.title('LogIn Page')
bgImage=ImageTk.PhotoImage(file="bg.jpg")
bgLable=Label(image=bgImage)
bgLable.place(x=10,y=0)

#---------------------------------------------------------Create A Class Named As sign_up_page-------------------------------------------
class sign_up_page:
    def clear(self):
        self.emailEntry.delete(0,END)
        self.userEntry.delete(0,END)
        self.passEntry.delete(0,END)
        self.cpassEntry.delete(0,END)
        self.check.set(0)
        
    
    def sign_up_database(self):  
        if self.emailEntry.get() ==''or self.userEntry.get()=='' or self.cpassEntry.get()=='':
            messagebox.showerror('Error','All fields are required') 
        elif self.passEntry.get()!=self.cpassEntry.get():
            messagebox.showerror('Error','Does not match password')
        elif self.check.get()==0:
            messagebox.showerror('Error','Select the button of agree the terms & conditions') 
        elif not '@'in self.emailEntry.get():
            messagebox.showerror('Error','Email Id is not valid')
        elif not 'gmail.com'in self.emailEntry.get():
            messagebox.showerror('Error','Email Id is not valid')
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='Ankit@817raj#',database='train')
                mycursor=con.cursor()
            except:
                messagebox.showerror('Error','Database Connectivity Issue, Please Try Again')    
                return
            try:
                query='use train'
                mycursor.execute(query)
                query='create table data1(id int auto_increment primary key not null,email varchar(30) unique key,username varchar(30),password varchar(30))'
                mycursor.execute(query)
            except:
                mycursor.execute('use train')
            
            
            query='select * from data1 where username=%s'
            mycursor.execute(query,(self.userEntry.get())) 
        
            row=mycursor.fetchone()
            if row!=None:
                messagebox.showerror('Error','Username allready exist')
            else:
                query='insert into data1(email,username,password) values(%s,%s,%s)'
                mycursor.execute(query,(self.emailEntry.get(),self.userEntry.get(),self.passEntry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success','Registration is successfully')  
                self.clear()  
                root.destroy()
                import Passenger_Login_file
           
    def login_page(self):
        root.destroy()
        import Passenger_Login_file
            
#------------------------------------------------------------------Function For Signup_page----------------------------------------------------
    def singnup___page(self):
       
        self.f2=Frame(root,height=405,width=520,bg="chocolate")
        self.f2.place(x=530,y=200)
        self.heading=Label(self.f2,text='CREATE AN ACCOUNT',font=('fantasty',22,'bold'),bg='chocolate',fg='blue')
        self.heading.place(x=100,y=10)
        self.f3=Frame(self.f2,height=5,width=520)
        self.f3.place(x=0,y=60)
        self.emailLabel=Label(self.f2,text="Enter Your Email:",font=('Arial',14,'bold'),bg='chocolate',fg='white')
        self.emailLabel.place(x=10,y=90)
        self.emailEntry=Entry(self.f2,width=26,font=('fantasty',14,'bold'),bg='white',bd=3)
        self.emailEntry.place(x=200,y=90)
        self.userLabel=Label(self.f2,text="Username:",font=('Arial',14,'bold'),bg='chocolate',fg='white')
        self.userLabel.place(x=10,y=130)   
        self.userEntry=Entry(self.f2,width=26,font=('fantasty',14,'bold'),bg='white',bd=3)
        self.userEntry.place(x=200,y=130)
        self.passLabel=Label(self.f2,text="Password:",font=('Arial',14,'bold'),bg='chocolate',fg='white')
        self.passLabel.place(x=10,y=170)

        self.passEntry=Entry(self.f2,width=26,font=('fantasty',14,'bold'),bg='white',bd=3)
        self.passEntry.place(x=200,y=170)

        self.cpassLabel=Label(self.f2,text="Confirm Password:",font=('Arial',14,'bold'),bg='chocolate',fg='white')
        self.cpassLabel.place(x=10,y=210)

        self.cpassEntry=Entry(self.f2,width=26,font=('fantasty',14,'bold'),bg='white',bd=3)
        self.cpassEntry.place(x=200,y=210)
        
        self.check=IntVar()
        self.terms=Checkbutton(self.f2,text="I agree to the Terms & conditions",font=('Arial',13,'bold'),bg='chocolate',fg='blue',activebackground='white',activeforeground='blue',variable=self.check)
        self.terms.place(x=200,y=250)
        
        self.signupButton=Button(self.f2,text='Signup',width=19,font=('Open sans',18,'bold'),bg='blue',fg='white',bd=0,activebackground='firebrick1',activeforeground='white',cursor='hand2',command=self.sign_up_database)
        self.signupButton.place(x=200,y=290)
        
        self.alreadyaccount=Label(self.f2,text='I have allready an account?',font=('fantasty',13,'bold'),bg='chocolate',fg='white')
        self.alreadyaccount.place(x=200,y=350)
        
        self.newaccountButton=Button(self.f2,text='Login',font=('Open sans',14,'bold'),bg='chocolate',fg='blue',bd=0,activebackground='chocolate',activeforeground='blue',cursor='hand2',command=self.login_page)
        self.newaccountButton.place(x=430,y=348)
        
obj=sign_up_page()
obj.singnup___page()

root.mainloop()
