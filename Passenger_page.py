from tkinter import*
# import tkinter  as tk
from tkinter import ttk
from PIL import ImageTk # type: ignore
import datetime as dt
from tkinter import messagebox 
import pymysql # type: ignore
root=Tk()
root.geometry("1530x1000")
root.resizable(0,0)
root.title("Railaway Reservation System")
#----------------------------------------------------------------------FIRST IMAGE OF OUR PROJECT --------------------------------------------#
bgImage=ImageTk.PhotoImage(file="Main.jpg")
bgLable=Label(root,image=bgImage)
bgLable.place(x=270,y=150)
#------------------------------------------------------------------Create A Class Named As Railway_Reservation_System------------------------#
class Railway_reservation_system:
#-------------------------------------------------------------Function For Create IRCTC ID Of Passeneger ------------------------------------#    
    def create_irctcid(self):
        self.bt1=Toplevel()
        self.bt1.geometry('1260x620+280+210')
        self.h1=Label(self.bt1,text='Account Details',font=('Arial',22,'bold'),fg='red',bg='lime')
        self.h1.place(x=300,y=20)
        self.UID=Label(self.bt1,text='User ID(3-35 char. Only letters and numbers.)',font=('Arial',10,'bold'),fg='gray')
        self.UID.place(x=10,y=100)
        self.UIDE=Entry(self.bt1,width=30,bg='white',fg='black',bd=0,font=('Arial',12,'bold'))
        self.UIDE.place(x=10,y=140)
        self.PASSID=Label(self.bt1,text='Password',font=('Arial',10,'bold'),fg='gray')
        self.PASSID.place(x=10,y=180)
        self.PASSIDE=Entry(self.bt1,width=30,bg='white',fg='black',bd=3,font=('Arial',12,'bold'))
        self.PASSIDE.place(x=10,y=220)
        self.EMAIL=Label(self.bt1,text='Enter Email Id',font=('Arial',10,'bold'),fg='gray')
        self.EMAIL.place(x=10,y=260)
        self.EMAILE=Entry(self.bt1,width=30,bg='white',fg='black',bd=3,font=('Arial',12,'bold'))
        self.EMAILE.place(x=10,y=300)
        self.Mobile=Label(self.bt1,text='Your Mobile Number',font=('Arial',10,'bold'),fg='gray')
        self.Mobile.place(x=10,y=340)
        self.MobileE=Entry(self.bt1,width=30,bg='white',fg='black',bd=3,font=('Arial',12,'bold'))

        self.MobileE.place(x=10,y=380)
        self.CreateIdd=Button(self.bt1,text='Proceed',font=('Arial',18,'bold'),bg='blue',fg='white',activebackground='blue',activeforeground='white',relief='sunken',bd=15,command=self.connect_database)
        self.CreateIdd.place(x=500,y=500)
#------------------------------------------------CONNECT DATABASE FOR IRCTC-----------------------------------------------------
    def connect_database(self):
        if self.UIDE.get()=='' or self.PASSIDE.get()=='' or self.EMAILE.get()=='' or self.MobileE.get()=='':
            messagebox.showerror('Error','All fields are required')  
        elif not '@'in self.EMAILE.get():
            messagebox.showerror('Error','Email Id is not valid')
        elif not 'gmail.com'in self.EMAILE.get():   
            messagebox.showerror('Error','Email Id is not valid')
        elif len(self.MobileE.get())!=10:
            messagebox.showerror('Error','Mobile No. is not valid')        
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
                query='create table IRCTC(id int auto_increment primary key not null,username varchar(30) unique key,password varchar(30),email varchar(30),mobile varchar(10))'
                mycursor.execute(query)
            except:
                mycursor.execute('use train')
            
            
            query='select * from IRCTC where username=%s'
            mycursor.execute(query,(self.UIDE.get())) 
                
            row=mycursor.fetchone()
            if row!=None:
                messagebox.showerror('Error','Username allready exist')
            else:
                query='insert into IRCTC(username,password,email,mobile) values(%s,%s,%s,%s)'
                mycursor.execute(query,(self.UIDE.get(),self.PASSIDE.get(),self.EMAILE.get(),self.MobileE.get()))
                con.commit()
                                    
                messagebox.showinfo('Success','Registration is successfully') 
                self.clear1
            con.close()     
    def clear1(self):
        self.UIDE.delete(0,END)
        self.PASSIDE.delete(0,END)
        self.EMAILE.delete(0,END)
        self.MobileE.delete(0,END)
#-----------------------------------------------------------------Function For Forget Irctc Password------------------------------------------------#

    def forgot_irctc_password(self):
        self.f1=Frame(self.bt,height=250,width=500,bg='pink',bd=2,relief='ridge')
        self.f1.place(x=180,y=100)
        
        self.backb=Button(self.f1,text='X',bg='pink',fg='black',font=('Arial',12,'bold'),command=self.f1.destroy,activebackground='pink',activeforeground='black',bd=0)
        self.backb.place(x=480,y=0)
        self.FUID=Label(self.f1,text='User ID(3-35 char. Only letters and numbers.)',font=('Arial',10,'bold'),bg='pink',fg='gray')
        self.FUID.place(x=5,y=4)
        self.FUIDE=Entry(self.f1,width=30,bg='white',fg='black',bd=0,font=('Arial',12,'bold'))
        self.FUIDE.place(x=5,y=30)
        self.FPASSID=Label(self.f1,text='Password',font=('Arial',10,'bold'),bg='pink',fg='gray')
        self.FPASSID.place(x=5,y=56)
        self.FPASSIDE=Entry(self.f1,width=30,bg='white',fg='black',bd=0,font=('Arial',12,'bold'))
        self.FPASSIDE.place(x=5,y=82)
        self.FCPASSID=Label(self.f1,text='Confirm Password',font=('Arial',10,'bold'),bg='pink',fg='gray')
        self.FCPASSID.place(x=5,y=108)
        self.FCPASSIDE=Entry(self.f1,width=30,bg='white',fg='black',bd=0,font=('Arial',12,'bold'))
        self.FCPASSIDE.place(x=5,y=134) 
        self.FChangepass=Button(self.f1,text='Change Password',font=('Arial',16,'bold'),bg='blue',fg='white',activebackground='blue',activeforeground='white',command=self.change_pass)
        self.FChangepass.place(x=80,y=170)    
    def change_pass(self):
        if self.FUIDE.get()=='' or self.FPASSIDE.get()=='' or  self.FCPASSIDE.get()=='':
            messagebox.showerror('Error','All fields are required')
        elif self.FPASSIDE.get()!=self.FCPASSIDE.get():
            messagebox.showerror('Error','Does not match password')
        else:
            con1=pymysql.connect(host='localhost',user='root',password='Ankit@817raj#',database='train')
        mycursor=con1.cursor()
        query='select * from irctc where username=%s'
        mycursor.execute(query,(self.FUIDE.get()))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror('Error','Incorrect Username')
        else:
            query='update irctc set password=%s where username=%s'
            mycursor.execute(query,(self.FPASSIDE.get(),self.FUIDE.get()))
            con1.commit()
            con1.close()
            messagebox.showinfo('success','Password has been changed')    

#----------------------------------------------------------Function For Book Ticket -----------------------------------------------------------#
    
    def book_ticket(self):
        def source(event):
            if self.fromse.get()=='Enter the source location':
                self.fromse.delete(0,END)
        def to(event):
            if self.toe.get()=='Enter the destination location':
                self.toe.delete(0,END)
     
        def on_enter(event):
            if self.Ed1.get()=='YYYY-MM-DD': 
                self.Ed1.delete(0,END)
                
            
        self.bt=Toplevel()
        self.bt.geometry('1250x620+280+210')
        self.bt.title('Reservation Of Ticket')
        self.f1=Frame(self.bt,height=700,width=1250,bd=10,relief=RIDGE,bg='white')
        self.f1.place(x=0,y=0)
        
        self.b=ImageTk.PhotoImage(file="img.jpg")
        self.b=Label(self.f1,image=self.b,bd=10,relief='solid')
        self.b.place(x=1020,y=0)
        
        self.f2=Frame(self.f1,height=80,width=1020,bd=0,bg='cyan')
        self.f2.place(x=0,y=0)
        self.h1=Label(self.f1,text='FILL OUT THE ALL FIELDS FOR BOOK TICKET',font=('Arial',16,'bold'),bg='cyan',fg='green')
        self.h1.place(x=140,y=20) 
        self.IrctcId=Label(self.f1,text='Your IRCTC ID',font=('Arial',14,'bold'),bg='white')
        self.IrctcId.place(x=10,y=90) 
        self.Irctc=Entry(self.f1,widt=20,bg='white',bd=0,font=('arial',10,'bold'),border=5)
        self.Irctc.place(x=200,y=90)
        self.CreateId=Button(self.f1,text='Create Id',font=('Arial',12,'bold'),bg='white',fg='blue',bd=0,activebackground='pink',activeforeground='blue',border=5,relief='raised',command=self.create_irctcid)
        self.CreateId.place(x=400,y=85)
        self.Iforgot_pass=Button(self.f1,text='Forgot Password?',font=('Arial',12,'bold'),bg='gainsboro',fg='blue',bd=0,activebackground='gainsboro',activeforeground='blue',border=5,relief='raised',command=self.forgot_irctc_password)
        self.Iforgot_pass.place(x=600,y=85)
        self.f4=Frame(self.f1,height=50,width=900,bd=0,bg='gainsboro')
        self.f4.place(x=0,y=130)
        self.IrctcId1=Label(self.f4,text='your IRCTC ID will be required to complete this booking.',font=('Arial',12),bg='gainsboro')
        self.IrctcId1.place(x=0,y=10)
        self.Tname=Label(self.f1,text='Full name (As per Govt. ID):',font=('Arial',10,'bold'),fg='gray')
        self.Tname.place(x=5,y=190)
        self.TnameE=Entry(self.f1,width=30,bg='white',fg='black',bd=3,font=('Arial',12,'bold'))
        self.TnameE.place(x=200,y=190)
        self.TAge=Label(self.f1,text='Age (As per Govt. ID):',font=('Arial',10,'bold'),fg='gray')
        self.TAge.place(x=5,y=220)
        self.TageE=Entry(self.f1,width=15,bg='white',fg='black',bd=3,font=('Arial',12,'bold'))
        self.TageE.place(x=200,y=220)
        self.TGender=Label(self.f1,text='Gender:',font=('Arial',10,'bold'),fg='gray')
        self.TGender.place(x=490,y=190)
        sex=['Male','Female','Transgender']
        self.TGenderE=ttk.Combobox(self.f1,width=30,values=sex)
        self.TGenderE.set('Male')
        self.TGenderE.place(x=620,y=190)
    
        self.TNationality=Label(self.f1,text='Nationality:',font=('Arial',10,'bold'),fg='gray')
        self.TNationality.place(x=5,y=250)
        self.TNationalityE=Entry(self.f1,width=15,bg='white',fg='black',bd=3,font=('Arial',12,'bold'))
        self.TNationalityE.place(x=200,y=250)
        self.seetl=Label(self.f1,text='Berth Preference',font=('Arial',10,'bold'),fg='gray')
        self.seetl.place(x=490,y=220)
        self.preference=['No preference','Lower','Uper','Side Lower','Side Uper']
        self.seet=ttk.Combobox(self.f1,values=self.preference,width=30)
        self.seet.set('No preference')
        self.seet.place(x=620,y=220)
        
        self.l=Label(self.f1,text='Note : No cencession are allowed in this train',font=('Arial',10,'bold'),fg='gray')
        self.l.place(x=490,y=250)
        
        self.froms=Label(self.f1,text='From     :   ',font=('Arial',10,'bold'),fg='grey')
        self.froms.place(x=5,y=300)
        self.fromse=Entry(self.f1,width=30,bg='white',fg='black',bd=3,font=('Arial',12,'bold'))
        self.fromse.place(x=190,y=300)
        self.fromse.insert(0,'Enter the source location')
        self.fromse.bind('<FocusIn>',source)
        self.tos=Label(self.f1,text='To          :   ',font=('Arial',10,'bold'),fg='gray')
        self.tos.place(x=490,y=300)
    
        self.toe=Entry(self.f1,width=30,bg='white',fg='black',bd=3,font=('Arial',12,'bold'))
        self.toe.place(x=620,y=300)
        self.toe.insert(0,'Enter the destination location')
        self.toe.bind('<FocusIn>',to)
  
        self.d1=Label(self.f1,text="Date  :",font=('Jumble',10,'bold'),fg='grey',bd=1)
        self.d1.place(x=490,y=360)
        self.Ed1=Entry(self.f1,width=13,fg='red',font=('arial',12,'bold'),bd=3)
        self.Ed1.place(x=620,y=360)
        self.Ed1.insert(0,'YYYY-MM-DD')
        self.Ed1.bind('<FocusIn>',on_enter)
        
        self.trainno=Label(self.f1,text='Train No',font=('Arial',10,'bold'),fg='gray')
        self.trainno.place(x=5,y=330)
        self.trainnoE=Entry(self.f1,width=25,bd=3,font=('Arial',12,'bold'),bg='white')
        self.trainnoE.place(x=190,y=330)
        
        self.urid=Label(self.f1,text='Your IDNO:',font=('Arial',10,'bold'),fg='gray')
        self.urid.place(x=490,y=330)
        self.uridE=Entry(self.f1,width=25,bd=3,font=('Arial',12,'bold'),bg='white')
        self.uridE.place(x=620,y=330)

        self.Classl=Label(self.f1,text='Seet Class',font=('Arial',10,'bold'),fg='gray')
        self.Classl.place(x=5,y=360)
        self.seetd=['Sleeper','1AC','2AC','3AC','General']
        self.seetd=ttk.Combobox(self.f1,values=self.seetd,width=30)
        self.seetd.set('General')
        self.seetd.place(x=190,y=360)
        
        self.h2=Label(self.f1,text="Cantact Details",font=('Jumble',12,'bold'),fg='Black',bd=2)
        self.h2.place(x=5,y=390)
        self.Phoneno=Label(self.f1,text='Mobile Number:',font=('Arial',10,'bold'),fg='gray')
        self.Phoneno.place(x=5,y=420)
        C=Label(self.f1,text='+91 ',font=('Arial',12,'bold'),bg='white',fg='black',bd=3,relief='ridge')
        C.place(x=190,y=420)
        self.PhonenoE=Entry(self.f1,width=15,bd=3,font=('Arial',12,'bold'),bg='white')
        self.PhonenoE.place(x=230,y=420)
        self.Emailid=Label(self.f1,text='Email Id:',font=('Arial',10,'bold'),fg='gray')
        self.Emailid.place(x=490,y=420)
        self.EmailidE=Entry(self.f1,width=25,bd=3,font=('Arial',12,'bold'),bg='white')
        self.EmailidE.place(x=620,y=420)
        
        self.l1=Label(self.f1,text='Note :',fg='gray',font=('Arial',12,'bold'))
        self.l1.place(x=5,y=450)
        
        self.l1=Label(self.f1,text='By Clicking on Proceed to Pay , I confirm that I have read, understood and agree with the ',bg='white',fg='gray',font=('Arial',11,'bold'))
        self.l1.place(x=5,y=480)
        self.l12=Label(self.f1,text='Cancellation & Refund Policy, Privacy Policy and Terms of use',fg='blue',font=('Arial',11,'bold'),bg='white')
        self.l12.place(x=5,y=510)
    
        Done=Button(self.f1,text='Proceed To Pay',font=('Arial',16,'bold'),bg='blue',fg='white',activebackground='blue',activeforeground='white',command=self.connect_database1)
        Done.place(x=400,y=550)
    
    
    def connect_database1(self):
        if self.Irctc.get()==''or self.TnameE.get()=='' or self.TageE.get()=='' or self.TGenderE.get()=='' or self.TNationalityE.get()=='' or self.seet.get()=='' or self.fromse.get()=='' or self.toe.get()=='' or self.PhonenoE.get()=='' or self.EmailidE.get()=='' or self.Ed1.get()==''or self.seetd.get()==''or self.uridE.get()==''or self.trainnoE.get()=='':
            messagebox.showerror('Error','All fields are required') 
        elif not '@'in self.EmailidE.get():
            messagebox.showerror('Error','Email Id is not valid')
        elif not 'gmail.com'in self.EmailidE.get():   
            messagebox.showerror('Error','Email Id is not valid')
        elif len(self.PhonenoE.get())!=10:
            messagebox.showerror('Error','Mobile No. is not valid')        
        try:
            con=pymysql.connect(host='localhost',user='root',password='Ankit@817raj#',database='train')
            mycursor=con.cursor()
        except:
                messagebox.showerror('Error','Database Connectivity Issue, Please Try Again')    
                return                    
        try:
            query='use train'
            mycursor.execute(query)
            query='create table book_ticket(Ticketno int unique key auto_increment,irctcid varchar(30),name varchar(50),age int,gender varchar(20),preferences varchar(25),nationality varchar(20),frome varchar(30),toe varchar(30),Tno int(5),yourid int(5),class varchar(20),datee date,mobile varchar(10),email varchar(50))'
            
            mycursor.execute(query)
        except:
            mycursor.execute('use train')
            
            
        query='select * from irctc where username=%s'
        mycursor.execute(query,(self.Irctc.get())) 
        
        row=mycursor.fetchone()
        
        query1='select * from train_data where Spoint=%s and Epoint=%s'
        mycursor.execute(query1,(self.fromse.get(),self.toe.get()))
        
        row1=mycursor.fetchone()
        
        query2='select * from book_ticket where yourid=%s'
        mycursor.execute(query2,(self.uridE.get())) 
        
        row2=mycursor.fetchone()
        
        query3='select * from  train_data where Tno=%s'
        mycursor.execute(query3,(self.trainnoE.get())) 
        row3=mycursor.fetchone()
        
        
        if row==None:
            messagebox.showerror('Error','Invalid IrctcId')        
            
        
        elif row1==None:
            messagebox.showerror('Error','No valid Satation')
        
        
        elif row2!=None:
            messagebox.showerror('Error','Yourid allready exist')     
        
        elif row3==None:
            messagebox.showerror('Error','This Train is not available')       
           
        else:    
            query='insert into book_ticket(irctcid,name,age,gender,preferences,nationality,frome,toe,Tno,yourid,class,datee,mobile,email) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(query,(self.Irctc.get(),self.TnameE.get(),self.TageE.get(),self.TGenderE.get(),self.seet.get(),self.TNationalityE.get(),self.fromse.get(),self.toe.get(),self.trainnoE.get(),self.uridE.get(),self.seetd.get(),self.Ed1.get(),self.PhonenoE.get(),self.EmailidE.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Congratulation!!','Your Ticket has been created successfully')  
            self.clear()
    def clear(self):
        self.Irctc.delete(0,END)
        self.TnameE.delete(0,END)
        self.TageE.delete(0,END)
        self.TGenderE.delete(0,END)
        self.seet.delete(0,END)
        self.TNationalityE.delete(0,END)
        self.fromse.delete(0,END)
        self.toe.delete(0,END)
        self.trainnoE.delete(0,END)
        self.uridE.delete(0,END)
        self.seetd.delete(0,END)
        self.Ed1.delete(0,END)
        self.PhonenoE.delete(0,END)
        self.EmailidE.delete(0,END)
        
#--------------------------------------------------------------------Function For Cancel Ticket -----------------------------------------------------------#        
    def cancel_ticket(self):
        def ticket(event):
            if self.TicketnoE.get()=='Enter Your Id here': 
                self.TicketnoE.delete(0,END)
        self.bt2=Toplevel()
        self.bt2.geometry('1250x620+280+210')
        self.bt2.title('Cancel Ticket')
        bg2Image=ImageTk.PhotoImage(file="Main.jpg")
        bg2Lable=Label(self.bt2,image=bg2Image)
        bg2Lable.place(x=0,y=0)
        
        self.Ticketno=Label(self.bt2,text='Enter The Your Id :',font=('Arial',12,'bold'),fg='red',bd=5)
        self.Ticketno.place(x=20,y=10)
        self.TicketnoE=Entry(self.bt2,width=25,bd=3,font=('Arial',12,'bold'),bg='white')
        self.TicketnoE.place(x=200,y=10)
        self.TicketnoE.insert(0,'Enter Your Id here')
        self.TicketnoE.bind('<FocusIn>',ticket)
        self.cancelti=Button(self.bt2,text="Cancel Your Ticket ",font=('Arial',14,'bold'),fg='blue',bd=5,command=self.cancelt)
        self.cancelti.place(x=500,y=10)
        # bgLable.grid()    
      
    def cancelt(self):
        
        if self.TicketnoE.get()=='':
            messagebox.showerror('Error','Please Enter the Train no.')
        else:
            con1=pymysql.connect(host='localhost',user='root',password='Ankit@817raj#',database='train')
            mycursor=con1.cursor()
            query='select * from book_ticket where yourid=%s'
            mycursor.execute(query,(self.TicketnoE.get()))
            row=mycursor.fetchone()
        if row==None:
                messagebox.showerror('Error','Incorrect Your Id No.')
        else:
            query='DELETE FROM book_ticket WHERE yourid=%s'
            mycursor.execute(query,(self.TicketnoE.get()))
            con1.commit()
            con1.close()
            messagebox.showinfo('success','Your Trip Cancellation Sucessfully!!!!!')  
            
# ------------------------------------------------------------Function For Search Train-----------------------------------------------------------#            
    def search_train(self):
        self.bt3=Toplevel()
        self.bt3.geometry('1250x620+280+210')
        self.bt3.title('Search train')
        
        g1Image=ImageTk.PhotoImage(file="first.jpg")
        g1Lable=Label(self.bt3,image=bgImage)
        g1Lable.place(x=0,y=0)
         
        self.Froml=Label(self.bt3,text='From :',font=('Arial',14,'bold'),fg='blue')
        self.Froml.place(x=5,y=5)
        self.FromlE=Entry(self.bt3,width=25,bd=3,font=('Arial',12,'bold'),bg='white')
        self.FromlE.place(x=100,y=5)
        self.Tol=Label(self.bt3,text='To :',font=('Arial',14,'bold'),fg='blue')
        self.Tol.place(x=380,y=5)
        self.TolE=Entry(self.bt3,width=25,bd=3,font=('Arial',12,'bold'),bg='white')
        self.TolE.place(x=465,y=5)
        self.Search=Button(self.bt3,text='Search Train',bd=0,bg='blue',fg='white',activebackground='blue',activeforeground='white',font=('Arial',12,'bold'),command=self.search__train)
        self.Search.place(x=800,y=2)
        self.f1=Frame(self.bt3,height=600,width=1250,bg="red") 
        self.f1.place(x=0,y=620)
        
    def search__train(self):
        self.Serch=Frame(self.bt3,relief='sunken',bd=8,width=1250,height=620)
        self.Serch.place(x=10,y=50)
        self.dumy=["id","Tno","Tname","Spoint","Epoint","S_TIME","E_TIME"]
        self.real=["SL.NO","Train No","Train Name","From","To","Departure Time","Arrival Time"]
        self.Serch_treeview=ttk.Treeview(self.Serch,columns=("id","Tno","Tname","Spoint","Epoint","S_TIME","E_TIME"))
        self.Serch_treeview.place(x=5,y=5,width=1250,height=620)
        for i in range(len(self.dumy)):
            self.Serch_treeview.heading(self.dumy[i],text=self.real[i])
            self.Serch_treeview.column(self.dumy[i],width=140)
        self.Serch_treeview["show"]="headings"
        self.s=ttk.Style(self.bt3)
        self.s.theme_use('clam')
        self.s.configure('.',font=('Arial',15,'bold'),background='cyan',foreground='blue')
        self.s.configure('Treeview.Heading',foreground='red',font=('Arial',14,'bold'),background="cyan")
        self.fetch_searchtrain()
        
    def fetch_searchtrain(self):
        if self.FromlE.get()=='' or self.TolE.get()=='':
             messagebox.showerror('Error','Please Input the data')
        else:
            try:
                con1=pymysql.connect(host='localhost',user='root',password='Ankit@817raj#',database='train')
                mycursor=con1.cursor()
            except:
                messagebox.showerror("Error","Database Connectivity Issue")
                return
            query=('select * from train_data where Spoint=%s and Epoint=%s')
            mycursor.execute(query,(self.FromlE.get(),self.TolE.get()))
            row=mycursor.fetchone()
        if row==None:
            messagebox.showerror("Error","There is no train!!!!!!")
            messagebox.showwarning("Warning","Please enter the valid station Name...")
        else:
            query1=('select * from train_data where Spoint=%s and Epoint=%s')
            mycursor.execute(query1,(self.FromlE.get(),self.TolE.get()))
            row1=mycursor.fetchall()
        if len(row1)!=0:
            self.Serch_treeview.delete(*self.Serch_treeview.get_children())
            for i in row1:
                self.Serch_treeview.insert("",END,values=i)
                con1.commit()
        con1.close()  
        
#-----------------------------------------------------------Function For Show Ticket --------------------------------------------------#        
    def show_ticket(self):
        self.bt4=Toplevel()
        self.bt4.geometry('1250x620+280+210')
        self.bt4.title('Show Ticket')
         
        self.yourid=Label(self.bt4,text='Enter Your ID No.:',font=('Arial',14,'bold'),fg='blue')
        self.yourid.place(x=5,y=5)
        self.youridE=Entry(self.bt4,width=25,bd=3,font=('Arial',12,'bold'),bg='white')
        self.youridE.place(x=180,y=5)
        self.Search=Button(self.bt4,text='Continue',bd=0,bg='blue',fg='white',activebackground='blue',activeforeground='white',font=('Arial',12,'bold'),command=self.show__ticket)
        self.Search.place(x=550,y=2)  
    
    def show__ticket(self):
        self.show=Frame(self.bt4,relief='sunken',bd=8,bg='blue')
        self.show.place(x=10,y=50,width=1250,height=620)
        self.dumy=['Tno','yourid','Tname','Name','frome','toe','datee','S_TIME','E_TIME','Ticketno','seet','Preferences','price']
        self.real=["Train.NO","YourId","Train Name","Name","From","To","Date","Departure Time","Arrival Time","Ticket No","Class","Berth","Fare"]
        self.show_treeview=ttk.Treeview(self.show,columns=('Tno','yourid','Tname','Name','frome','toe','datee','S_TIME','E_TIME','Ticketno','seet','Preferences','price'))
        self.show_treeview.place(x=5,y=5,width=1250,height=620)
        for i in range(len(self.dumy)):
            self.show_treeview.heading(self.dumy[i],text=self.real[i])
            self.show_treeview.column(self.dumy[i],width=100)
        self.show_treeview["show"]="headings"
        self.s=ttk.Style(self.bt4)
        self.s.theme_use('clam')
        self.s.configure('.',font=('Arial',12,'bold'),background='cyan',foreground='blue')
        self.s.configure('Treeview.Heading',foreground='red',font=('Arial',12,'bold'),background="cyan")
    
        self.fetch_showticket()
        
    def fetch_showticket(self):
        if self.youridE.get()=='':
             messagebox.showerror('Error','Please Enter Your Id No.')
        else:
            try:
                con1=pymysql.connect(host='localhost',user='root',password='Ankit@817raj#',database='train')
                mycursor=con1.cursor()
            except:
                messagebox.showerror("Error","Database Connectivity Issue")
                return
            query=('select * from book_ticket where yourid=%s')
            mycursor.execute(query,(self.youridE.get()))
            row=mycursor.fetchone()
        if row==None:
            messagebox.showwarning("Warning","Invalid Your Id No.!!!")
        else:
            query1='select * from book_ticket,train_data where book_ticket.yourid=%s and book_ticket.class="1AC" and book_ticket.Tno=train_data.Tno'
            mycursor.execute(query1,(self.youridE.get()))
            row1=mycursor.fetchone()
            
            query2='select * from book_ticket,train_data where book_ticket.yourid=%s and book_ticket.class="2AC" and book_ticket.Tno=train_data.Tno'
            mycursor.execute(query2,(self.youridE.get()))
            row2=mycursor.fetchone()
            
            query3='select * from book_ticket,train_data where book_ticket.yourid=%s and book_ticket.class="3AC" and book_ticket.Tno=train_data.Tno'
            mycursor.execute(query3,(self.youridE.get()))
            row3=mycursor.fetchone()
            
            
            query4='select * from book_ticket,train_data where book_ticket.yourid=%s and book_ticket.class="Sleeper" and book_ticket.Tno=train_data.Tno'
            mycursor.execute(query4,(self.youridE.get()))
            row4=mycursor.fetchone()
            
            query5='select * from book_ticket,train_data where book_ticket.yourid=%s and book_ticket.class="General" and book_ticket.Tno=train_data.Tno'
            mycursor.execute(query5,(self.youridE.get()))
            row5=mycursor.fetchone()
            
            
            
            if row1!=None:
                query6=('select book_ticket.Tno,book_ticket.yourid,train_data.Tname,book_ticket.Name,book_ticket.frome,book_ticket.toe,book_ticket.datee,train_data.S_TIME,train_data.E_TIME,book_ticket.Ticketno,book_ticket.class,book_ticket.Preferences,train_price.price1A from book_ticket,train_data,train_price where book_ticket.yourid=%s and train_data.Tno=book_ticket.Tno and train_price.Tno=book_ticket.tno')
                mycursor.execute(query6,(self.youridE.get()))
                row6=mycursor.fetchall()
                if len(row6)!=0:
                    self.show_treeview.delete(*self.show_treeview.get_children())
                    for i in row6:
                        self.show_treeview.insert("",END,values=i)
                        con1.commit() 
                con1.close()        
                    
            elif row2!=None:
                query7=('select book_ticket.Tno,book_ticket.yourid,train_data.Tname,book_ticket.Name,book_ticket.frome,book_ticket.toe,book_ticket.datee,train_data.S_TIME,train_data.E_TIME,book_ticket.Ticketno,book_ticket.class,book_ticket.Preferences,train_price.price2A from book_ticket,train_data,train_price where book_ticket.yourid=%s and train_data.Tno=book_ticket.Tno and train_price.Tno=book_ticket.tno')
                mycursor.execute(query7,(self.youridE.get()))
                row7=mycursor.fetchall()
                if len(row7)!=0:
                    self.show_treeview.delete(*self.show_treeview.get_children())
                    for i in row7:
                        self.show_treeview.insert("",END,values=i)
                        con1.commit()
                con1.close()  
                           
        
            elif row3!=None:
                query8=('select book_ticket.Tno,book_ticket.yourid,train_data.Tname,book_ticket.Name,book_ticket.frome,book_ticket.toe,book_ticket.datee,train_data.S_TIME,train_data.E_TIME,book_ticket.Ticketno,book_ticket.class,book_ticket.Preferences,train_price.price3A from book_ticket,train_data,train_price where book_ticket.yourid=%s and train_data.Tno=book_ticket.Tno and train_price.Tno=book_ticket.tno')
                mycursor.execute(query8,(self.youridE.get()))
                row8=mycursor.fetchall()
                if len(row8)!=0:
                    self.show_treeview.delete(*self.show_treeview.get_children())
                    for i in row8:
                        self.show_treeview.insert("",END,values=i)
                        con1.commit()
                con1.close()        
            
            elif row4!=None:
                query9=('select book_ticket.Tno,book_ticket.yourid,train_data.Tname,book_ticket.Name,book_ticket.frome,book_ticket.toe,book_ticket.datee,train_data.S_TIME,train_data.E_TIME,book_ticket.Ticketno,book_ticket.class,book_ticket.Preferences,train_price.pricesl from book_ticket,train_data,train_price where book_ticket.yourid=%s and train_data.Tno=book_ticket.Tno and train_price.Tno=book_ticket.tno')
                mycursor.execute(query9,(self.youridE.get()))
                row9=mycursor.fetchall()
                if len(row9)!=0:
                    self.show_treeview.delete(*self.show_treeview.get_children())
                    for i in row9:
                        self.show_treeview.insert("",END,values=i)
                        con1.commit() 
                con1.close()     
                
            elif row5!=None:
                query10=('select book_ticket.Tno,book_ticket.yourid,train_data.Tname,book_ticket.Name,book_ticket.frome,book_ticket.toe,book_ticket.datee,train_data.S_TIME,train_data.E_TIME,book_ticket.Ticketno,book_ticket.class,book_ticket.Preferences,train_price.pricegn from book_ticket,train_data,train_price where book_ticket.yourid=%s and train_data.Tno=book_ticket.Tno and train_price.Tno=book_ticket.tno')
                mycursor.execute(query10,(self.youridE.get()))
                row10=mycursor.fetchall()  
                if len(row10)!=0:
                    self.show_treeview.delete(*self.show_treeview.get_children())
                    for i in row10:
                        self.show_treeview.insert("",END,values=i)
                        con1.commit()           
                con1.close()        
            
#---------------------------------------------------------------------Function For LogOut----------------------------------------------------------#            
    def log__out(self):
        root.destroy()
        import main_page
        
#--------------------------------------------------------------------Function For Delete Our Account-----------------------------------------------#        
    def log_out(self):
        self.bt5=Toplevel()
        self.bt5.geometry('1250x620+280+210')
        self.bt5.title('Delete Your Account')
        if self.passlE.get()=='' or  self.cpasslE.get()=='':
            messagebox.showerror('Error','All fields are required')
        elif self.passlE.get()!=self.cpasslE.get():
            messagebox.showerror('Error','Does not match password')
        else:
            con=pymysql.connect(host='localhost',user='root',password='Ankit@817raj#',database='train')
            mycursor=con.cursor()
            query='select * from data where password=%s'
            mycursor.execute(query,(self.passlE.get()))
            row=mycursor.fetchone()
        if row==None:
            messagebox.showerror('Error','Incorrect Password')
        else:
            query='delete from data where password=%s'
            mycursor.execute(query,(self.passlE.get()))
            con.commit()
            con.close()
            messagebox.showinfo('success','Your Account has been Deleted')
            root.destroy()
        self.passl=Label(self.bt5,text='Enter Your Password :',font=('Arial',12,'bold'),bg='pink',fg='red')
        self.passl.place(x=200,y=100)
        self.passlE=Entry(self.bt5,width=25,bd=0,font=('Arial',12,'bold'),bg='white')
        self.passlE.place(x=200,y=140)
        self.cpassl=Label(self.bt5,text='Confirm Your Password :',font=('Arial',12,'bold'),bg='pink',fg='red')
        self.cpassl.place(x=200,y=180)
        self.cpasslE=Entry(self.bt5,width=25,bd=0,font=('Arial',12,'bold'),bg='white')
        self.cpasslE.place(x=200,y=220)
        self.cancelt=Button(self.bt5,text="Continue ",font=('Arial',14,'bold'),bg='red',fg='blue',width=30,command=self.log_out)
        self.cancelt.place(x=130,y=350)                          
            
                     
#----------------------------------------------------------------Fucntion For Main Menu Of Travellers-----------------------------------------------------------#
    def main_menu(self,mainwindow):
        self.mainwindow=mainwindow
        self.un=Label(self.mainwindow,text="Railway Reservation \n System",font=("Algerian",25),bg="red",fg="white",width="1000",height="2",bd=15,relief=RIDGE)
        self.un.pack() 

        date=dt.datetime.now()
        self.currentlable=Label(self.mainwindow,text=f"{date:%A-%B-%d-%Y}",font=("calibiri",15),bg='red',fg='blue')
        self.currentlable.place(x=1270,y=45)
        self.f1=Frame(self.mainwindow,width=1530,height=68,bg='blue',bd=15,relief=RIDGE).place(x=0,y=105)
        self.label=Label(self.f1,text='IRCTC TRAIN',font=('Arial',19,'bold'),bg='blue',fg='white')
        self.label.place(x=230,y=120)
        self.label1=Label(self.mainwindow,text='PLAN YOU TRIP ON INDIAN RAILWAY TRAINS',font=('Arial',19,'bold'),bg='blue',fg='white')
        self.label1.place(x=550,y=120)
        self.f2=Frame(self.mainwindow,width=270,height=700,bg='red',bd=8,relief=RIDGE)
        self.f2.place(x=0,y=175)
        self.h1=Label(self.f2,text='MENU',font=("Arial",18,'bold'),fg="white",bg='red',bd=9,relief='sunken')
        self.h1.place(x=80,y=4)
        self.f3=Frame(self.f2,width=254,height=5,bg='black')
        self.f3.place(x=0,y=55)
        self.Bookticket=Button(self.f2,text="Book Ticket",font=('Arial',16,'bold'),bg='white',fg='blue',width=17,relief='raised',bd=9,command=self.book_ticket)
        self.Bookticket.place(x=5,y=80)
        self.Searchticket=Button(self.f2,text="Search Train",font=('Arial',16,'bold'),bg='white',fg='blue',width=17,relief='raised',bd=9,command=self.search_train)
        self.Searchticket.place(x=5,y=140)
        self.Showticket=Button(self.f2,text="Show Ticket",font=('Arial',16,'bold'),bg='white',fg='blue',width=17,relief='raised',bd=9,command=self.show_ticket)
        self.Showticket.place(x=5,y=200)
        self.Cancelticket=Button(self.f2,text="Cancel Ticket",font=('Arial',16,'bold'),bg='white',fg='blue',width=17,relief='raised',bd=9,command=self.cancel_ticket)
        self.Cancelticket.place(x=5,y=260)
        self.showtravellers=Button(self.f2,text="Logout",font=('Arial',16,'bold'),bg='white',fg='blue',width=17,relief='raised',bd=9,command=self.log__out)
        self.showtravellers.place(x=5,y=320)
        self.Logout=Button(self.f2,text="Delete Account",font=('Arial',16,'bold'),bg='white',fg='blue',width=17,relief='raised',bd=9,command=self.log_out)
        self.Logout.place(x=5,y=380)
        
        
        
project=Railway_reservation_system()
project.main_menu(root)        
root.mainloop()
