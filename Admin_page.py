from tkinter import*
from tkinter import ttk
from PIL import ImageTk # type: ignore
import datetime as dt
from tkinter import messagebox 
import pymysql # type: ignore
root=Tk()
root.geometry('1530x1000')
bgImage=ImageTk.PhotoImage(file="b1.jpg")
bgLable=Label(image=bgImage)
bgLable.place(x=10,y=0)
#-----------------------------------------------Create Class Named As CSE_DEPARTMENT---------------------------------#
class CSE_DEPARTMENT:
#-----------------------------------------------Function Of Add New Train--------------------------------------------#
    def Add_train(self):
        self.be1=Toplevel()
        self.be1.geometry('700x535+280+210')
        self.be1.title("Add New Train")                        
        self.f12=Frame(self.be1,height=535,width=700,bd=10,relief=RIDGE,bg='white')
        self.f12.place(x=0,y=0)
      
        self.f2=Frame(self.f12,height=80,width=680,bd=0,bg='cyan')
        self.f2.place(x=0,y=0)
        self.h1=Label(self.f2,text='FILL OUT THE ALL FIELDS FOR ADD TRAIN ',font=('Arial',16,'bold'),bg='cyan',fg='green')
        self.h1.place(x=140,y=20) 
        self.f3=Frame(self.f12,height=500,width=680,bd=0,bg='pink')
        self.f3.place(x=0,y=80)
        self.Trainno=Label(self.f3,text='Train Number :',font=('Arial',12,'bold'),bg='pink',fg='red')
        self.Trainno.place(x=10,y=10)
        self.TrainnoE=Entry(self.f3,width=25,bd=0,font=('Arial',12,'bold'),bg='white')
        self.TrainnoE.place(x=10,y=40)
        self.Trainname=Label(self.f3,text='Train Name :',font=('Arial',12,'bold'),bg='pink',fg='red')
        self.Trainname.place(x=10,y=70)
        self.TrainnameE=Entry(self.f3,width=25,bd=0,font=('Arial',12,'bold'),bg='white')
        self.TrainnameE.place(x=10,y=100)
        self.Startingpoint=Label(self.f3,text='Enter the starting station Name :',font=('Arial',12,'bold'),bg='pink',fg='red')
        self.Startingpoint.place(x=10,y=130)
        self.StartingpointE=Entry(self.f3,width=25,bd=0,font=('Arial',12,'bold'),bg='white')
        self.StartingpointE.place(x=10,y=160)
        self.Endingpoint=Label(self.f3,text='Enter the Ending station Name :',font=('Arial',12,'bold'),bg='pink',fg='red')
        self.Endingpoint.place(x=10,y=190)
        self.EndingpointE=Entry(self.f3,width=25,bd=0,font=('Arial',12,'bold'),bg='white')
        self.EndingpointE.place(x=10,y=220)
        self.Startingtime=Label(self.f3,text='Enter the starting Time :',font=('Arial',12,'bold'),bg='pink',fg='red')
        self.Startingtime.place(x=10,y=250)
        self.StartingtimeE=Entry(self.f3,width=25,bd=0,font=('Arial',12,'bold'),bg='white')
        self.StartingtimeE.place(x=10,y=280)
        self.Endingtime=Label(self.f3,text='Enter the Ending Time :',font=('Arial',12,'bold'),bg='pink',fg='red')
        self.Endingtime.place(x=10,y=310)
        self.EndingtimeE=Entry(self.f3,width=25,bd=0,font=('Arial',12,'bold'),bg='white')
        self.EndingtimeE.place(x=10,y=340)
        self.Done=Button(self.f3,text='   ADD TRAIN   ',font=('Arial',16,'bold'),bg='blue',fg='white',activebackground='blue',activeforeground='white',command=self.connect_database)
        self.Done.place(x=270,y=380)
    def clear1(self):
        self.TrainnoE.delete(0,END)
        self.TrainnameE.delete(0,END)
        self.StartingpointE.delete(0,END)
        self.EndingpointE.delete(0,END)
        self.StartingtimeE.delete(0,END)
        self.EndingtimeE.delete(0,END) 
           
#------------------------------------------------------------Connect Databse For Add New Train-----------------------------------------#                      
    def connect_database(self):
        if self.TrainnoE.get()=='' or self.TrainnameE.get()=='' or self.StartingpointE.get()=='' or self.EndingpointE.get()=='' or self.StartingtimeE.get()=='' or self.EndingtimeE.get()=='':
            messagebox.showerror('Error','All fields are required')      
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='Ankit@817raj#',database='train')
                mycursor=con.cursor()
            except:
                messagebox.showerror('Error','Database Connectivity Issue, Please Try Again')    
                return
            try:
                # query='create database train'
                # mycursor.execute(query)
                query='use train'
                mycursor.execute(query)
                query='create table Train_data(id int auto_increment primary key not null,Tno int(5) unique key,Tname varchar(30),Spoint varchar(30),Epoint varchar(30),S_TIME TIME,E_TIME TIME)'
                mycursor.execute(query)
            except:
                mycursor.execute('use train')
        
        
            query='select * from Train_data where Tno=%s'
            mycursor.execute(query,(self.TrainnoE.get())) 
            
            row=mycursor.fetchone()
            if row!=None:
                messagebox.showerror('Error','These Train allready exist')
            else:
                query='insert into Train_data(Tno,Tname,Spoint,Epoint,S_TIME,E_TIME) values(%s,%s,%s,%s,%s,%s)'
                #mycursor.execute(query,())
                #query='insert into travellers(Name,Age,Gender,Nationality,Preference) values(%s,%s,%s,%s,%s)'
                mycursor.execute(query,(self.TrainnoE.get(),self.TrainnameE.get(),self.StartingpointE.get(),self.EndingpointE.get(),self.StartingtimeE.get(),self.EndingtimeE.get()))    
                con.commit()
                con.close()
                messagebox.showinfo('Success','Inserted successfully')  
                self.clear1() 
                
#--------------------------------------------------------Function For Update Train----------------------------------------------------#                
    def Update_train_no(self):
        
        self.f2=Frame(self.be2,height=535,width=680,bd=0,bg='cyan')
        self.f2.place(x=0,y=0)
        self.h1=Label(self.f2,text='FILL OUT THE ALL FIELDS FOR UPDATE TRAIN ',font=('Arial',16,'bold'),bg='cyan',fg='green')
        self.h1.place(x=140,y=20) 
        self.f3=Frame(self.f2,height=535,width=680,bd=0,bg='pink')
        self.f3.place(x=0,y=80)
        self.Trainid=Label(self.f3,text='Train ID :',font=('Arial',12,'bold'),bg='pink',fg='red')
        self.Trainid.place(x=30,y=10)
        self.TrainidE=Entry(self.f3,width=25,bd=0,font=('Arial',12,'bold'),bg='white')
        self.TrainidE.place(x=30,y=40)
        self.UTrainno=Label(self.f3,text='Train Number :',font=('Arial',12,'bold'),bg='pink',fg='red')
        self.UTrainno.place(x=30,y=70)
        self.UTrainnoE=Entry(self.f3,width=25,bd=0,font=('Arial',12,'bold'),bg='white')
        self.UTrainnoE.place(x=30,y=100)
        self.CUTrainno=Label(self.f3,text='Confirm Train Number :',font=('Arial',12,'bold'),bg='pink',fg='red')
        self.CUTrainno.place(x=30,y=130)
        self.CUTrainnoE=Entry(self.f3,width=25,bd=0,font=('Arial',12,'bold'),bg='white')
        self.CUTrainnoE.place(x=30,y=160)
        self.Updatetrainno=Button(self.f3,text="Update Train Number",font=('Arial',14,'bold'),bg='red',fg='blue',width=30,command=self.uptrnno)
        self.Updatetrainno.place(x=130,y=250)
#-------------------------------------------------------Function For Update Train Number-----------------------------------------------#    
    def uptrnno(self):
        if self.TrainidE.get()=='' or self.UTrainnoE.get()=='' or self.CUTrainnoE.get()=='':
            messagebox.showerror('Error','All fields are required')
        elif self.UTrainnoE.get()!=self.CUTrainnoE.get():
            messagebox.showerror('Error','Does not match Train No.')
        else:
            con1=pymysql.connect(host='localhost',user='root',password='Ankit@817raj#',database='train')
            mycursor=con1.cursor()
            query='select * from Train_data where id=%s'
            mycursor.execute(query,(self.TrainidE.get()))
            row1=mycursor.fetchone()
        if row1==None:
            messagebox.showerror('Error','Incorrect ID No.')
        else:
            query='update Train_data set Tno=%s where id=%s'
            mycursor.execute(query,(self.UTrainnoE.get(),self.TrainidE.get()))
            con1.commit()
            con1.close()
            messagebox.showinfo('success','Train No. has been changed')   
            
#------------------------------------------------------Function For Update Train Name---------------------------------------------------#            
    def Update_train_name(self):
        self.f221=Frame(self.be2,height=535,width=680,bd=0,bg='cyan')
        self.f221.place(x=0,y=0)
        self.h1=Label(self.f221,text='FILL OUT THE ALL FIELDS FOR UPDATE TRAIN ',font=('Arial',16,'bold'),bg='cyan',fg='green')
        self.h1.place(x=140,y=20) 
        self.f22=Frame(self.f221,height=535,width=680,bd=0,bg='pink')
        self.f22.place(x=0,y=80)
        self.backb=Button(self.f221,text='X',bg='pink',fg='black',font=('Arial',12,'bold'),command=self.f221.destroy,activebackground='pink',activeforeground='black',bd=0)
        self.backb.place(x=660,y=0)
        self.f3=Frame(self.f22,height=500,width=680,bd=0,bg='pink')
        self.f3.place(x=0,y=80)
        self.Trainno=Label(self.f22,text='Train Number :',font=('Arial',12,'bold'),bg='pink',fg='red')
        self.Trainno.place(x=30,y=10)
        self.TrainnoE=Entry(self.f22,width=25,bd=0,font=('Arial',12,'bold'),bg='white')
        self.TrainnoE.place(x=30,y=40)
        self.UTrainname=Label(self.f22,text='Train Name :',font=('Arial',12,'bold'),bg='pink',fg='red')
        self.UTrainname.place(x=30,y=70)
        self.UTrainnameE=Entry(self.f22,width=25,bd=0,font=('Arial',12,'bold'),bg='white')
        self.UTrainnameE.place(x=30,y=100)
        self.CUTrainname=Label(self.f22,text='Confirm Train Name :',font=('Arial',12,'bold'),bg='pink',fg='red')
        self.CUTrainname.place(x=30,y=130)
        self.CUTrainnameE=Entry(self.f22,width=25,bd=0,font=('Arial',12,'bold'),bg='white')
        self.CUTrainnameE.place(x=30,y=160)
        self.Updatetrainname=Button(self.f22,text="Update Train Name",font=('Arial',14,'bold'),bg='red',fg='blue',width=30,command=self.uptrnname)
        self.Updatetrainname.place(x=130,y=250)                        
    def uptrnname(self):
        if self.TrainnoE.get()=='' or self.UTrainnameE.get()=='' or self.CUTrainnameE.get()=='':
            messagebox.showerror('Error','All fields are required')
        elif self.UTrainnameE.get()!=self.CUTrainnameE.get():
            messagebox.showerror('Error','Does not match Train Name.')
        else:
            con1=pymysql.connect(host='localhost',user='root',password='Ankit@817raj#',database='train')
            mycursor=con1.cursor()
            query='select * from Train_data where Tno=%s'
            mycursor.execute(query,(self.TrainnoE.get()))
            row3=mycursor.fetchone()
        if row3==None:
            messagebox.showerror('Error','Incorrect Train No.')
        else:
            query='update Train_data set Tname=%s where tno=%s'
            mycursor.execute(query,(self.UTrainnameE.get(),self.TrainnoE.get()))
            con1.commit()
            con1.close()
            messagebox.showinfo('success','Train No. has been changed') 

#---------------------------------------------------------Function For Update Train Deprature Time--------------------------------------------------#            
            
    def Update_train_Stime(self):
        self.f231=Frame(self.be2,height=535,width=680,bd=0,bg='cyan')
        self.f231.place(x=0,y=0)
        self.h1=Label(self.f231,text='FILL OUT THE ALL FIELDS FOR UPDATE TRAIN ',font=('Arial',16,'bold'),bg='cyan',fg='green')
        self.h1.place(x=140,y=20) 
        self.f23=Frame(self.f231,height=535,width=680,bd=0,bg='pink')
        self.f23.place(x=0,y=80)
        self.backb=Button(self.f231,text='X',bg='pink',fg='black',font=('Arial',12,'bold'),command=self.f231.destroy,activebackground='pink',activeforeground='black',bd=0)
        self.backb.place(x=660,y=0)
        self.Trainno=Label(self.f23,text='Train Number :',font=('Arial',12,'bold'),bg='pink',fg='red')
        self.Trainno.place(x=30,y=10)
        self.TrainnoE=Entry(self.f23,width=25,bd=0,font=('Arial',12,'bold'),bg='white')
        self.TrainnoE.place(x=30,y=40)
        self.UTrainsp=Label(self.f23,text='Starting Time of Train :',font=('Arial',12,'bold'),bg='pink',fg='red')
        self.UTrainsp.place(x=30,y=70)
        self.UTrainstE=Entry(self.f23,width=25,bd=0,font=('Arial',12,'bold'),bg='white')
        self.UTrainstE.place(x=30,y=100)
        self.CUTrainst=Label(self.f23,text='Confirm Starting Time of Train:',font=('Arial',12,'bold'),bg='pink',fg='red')
        self.CUTrainst.place(x=30,y=130)
        self.CUTrainstE=Entry(self.f23,width=25,bd=0,font=('Arial',12,'bold'),bg='white')
        self.CUTrainstE.place(x=30,y=160)
        self.Updatetrainst=Button(self.f23,text="Update Train Starting Time",font=('Arial',14,'bold'),bg='red',fg='blue',width=30,command=self.uptrste)
        self.Updatetrainst.place(x=130,y=250)
        
    def uptrste(self):
        if self.TrainnoE.get()=='' or self.UTrainstE.get()=='' or self.CUTrainstE.get()=='':
            messagebox.showerror('Error','All fields are required')
        elif self.UTrainstE.get()!=self.CUTrainstE.get():
            messagebox.showerror('Error','Does not match Starting Time of train.')
        else:
            con1=pymysql.connect(host='localhost',user='root',password='Ankit@817raj#',database='train')
            mycursor=con1.cursor()
            query='select * from Train_data where Tno=%s'
            mycursor.execute(query,(self.TrainnoE.get()))
            row4=mycursor.fetchone()
        if row4==None:
            messagebox.showerror('Error','Incorrect Train No.')
        else:
            query='update Train_data set S_time=%s where tno=%s'
            mycursor.execute(query,(self.UTrainstE.get(),self.TrainnoE.get()))
            con1.commit()
            con1.close()
            messagebox.showinfo('success','Train Starting time has been changed')    
        
#-----------------------------------------------------------Function For Update Train Arrival Time-------------------------------------------------#    
    
    def Update_train_Etime(self):
        self.f234=Frame(self.be2,height=535,width=680,bd=0,bg='cyan')
        self.f234.place(x=0,y=0)
        self.h1=Label(self.f234,text='FILL OUT THE ALL FIELDS FOR UPDATE TRAIN ',font=('Arial',16,'bold'),bg='cyan',fg='green')
        self.h1.place(x=140,y=20) 
        self.f23=Frame(self.f234,height=535,width=680,bd=0,bg='pink')
        self.f23.place(x=0,y=80)
        self.backb=Button(self.f234,text='X',bg='pink',fg='black',font=('Arial',12,'bold'),command=self.f234.destroy,activebackground='pink',activeforeground='black',bd=0)
        self.backb.place(x=660,y=0)
        self.Trainno=Label(self.f23,text='Train Number :',font=('Arial',12,'bold'),bg='pink',fg='red')
        self.Trainno.place(x=30,y=10)
        self.TrainnoE=Entry(self.f23,width=25,bd=0,font=('Arial',12,'bold'),bg='white')
        self.TrainnoE.place(x=30,y=40)
        self.UTrainsp=Label(self.f23,text='Starting Time of Train :',font=('Arial',12,'bold'),bg='pink',fg='red')
        self.UTrainsp.place(x=30,y=70)
        self.UTrainetE=Entry(self.f23,width=25,bd=0,font=('Arial',12,'bold'),bg='white')
        self.UTrainetE.place(x=30,y=100)
        self.CUTrainet=Label(self.f23,text='Confirm Starting Time of Train:',font=('Arial',12,'bold'),bg='pink',fg='red')
        self.CUTrainet.place(x=30,y=130)
        self.CUTrainetE=Entry(self.f23,width=25,bd=0,font=('Arial',12,'bold'),bg='white')
        self.CUTrainetE.place(x=30,y=160)
        self.Updatetrainet=Button(self.f23,text="Update Train Starting Time",font=('Arial',14,'bold'),bg='red',fg='blue',width=30,command=self.uptrete)
        self.Updatetrainet.place(x=130,y=250)
        
    def uptrete(self):
        if self.TrainnoE.get()=='' or self.UTrainetE.get()=='' or self.CUTrainetE.get()=='':
            messagebox.showerror('Error','All fields are required')
        elif self.UTrainstE.get()!=self.CUTrainstE.get():
            messagebox.showerror('Error','Does not match Starting Time of train.')
        else:
            con1=pymysql.connect(host='localhost',user='root',password='Ankit@817raj#',database='train')
            mycursor=con1.cursor()
            query='select * from Train_data where Tno=%s'
            mycursor.execute(query,(self.TrainnoE.get()))
            row5=mycursor.fetchone()
        if row5==None:
            messagebox.showerror('Error','Incorrect Train No.')
        else:
            query='update Train_data set E_time=%s where tno=%s'
            mycursor.execute(query,(self.UTrainetE.get(),self.TrainnoE.get()))
            con1.commit()
            con1.close()
            messagebox.showinfo('success','Train Starting time has been changed')   
                         
#-----------------------------------------------------------------Function For Cancel Train--------------------------------------------------------#    
    def cancel_train(self):
        self.be3=Toplevel()
        self.be3.geometry('700x535+280+210')
        self.be3.title('Cancel Train')
                                
        self.f12=Frame(self.be3,height=535,width=700,bd=10,relief=RIDGE,bg='white')
        self.f12.place(x=0,y=0)
      
        self.f2=Frame(self.f12,height=80,width=680,bd=0,bg='cyan')
        self.f2.place(x=0,y=0)
        self.h1=Label(self.f2,text='FILL OUT THE ALL FIELDS FOR CANCEL TRAIN ',font=('Arial',16,'bold'),bg='cyan',fg='green')
        self.h1.place(x=140,y=20) 
        self.f3=Frame(self.f12,height=500,width=680,bd=0,bg='pink')
        self.f3.place(x=0,y=80)
        self.Trainno=Label(self.f3,text='Train Number :',font=('Arial',15,'bold'),bg='pink',fg='green')
        self.Trainno.place(x=80,y=50)
        self.TrainnoE=Entry(self.f3,width=25,bd=5,font=('Arial',14,'bold'),bg='white',relief='raised')
        self.TrainnoE.place(x=80,y=80)
        self.Updatetrainet=Button(self.f3,text="DELETE TRAIN",font=('Arial',14,'bold'),bg='blue',fg='cyan',width=20,command=self.cancelt)
        self.Updatetrainet.place(x=130,y=250)
        
    def cancelt(self):
        if self.TrainnoE.get()=='':
            messagebox.showerror('Error','Please Enter Train No.')
        else:
            con1=pymysql.connect(host='localhost',user='root',password='Ankit@817raj#',database='train')
            mycursor=con1.cursor()
            query='select * from Train_data where Tno=%s'
            mycursor.execute(query,(self.TrainnoE.get()))
            row6=mycursor.fetchone()
        if row6==None:
            messagebox.showerror('Error','Incorrect Train No.')
        else:
            query='DELETE FROM Train_data where tno=%s'
            mycursor.execute(query,(self.TrainnoE.get()))
            con1.commit()
            con1.close()
            messagebox.showinfo('success','Deleted Successfully!!!!')
             
#-------------------------------------------------------------Function For Update Menu------------------------------------------------------#                           
                
    def update_train_details(self):
        self.be2=Toplevel()
        self.be2.geometry('700x535+280+210')
        self.be2.title('Upadate train deetails')
        
        self.f1=Frame(self.be2,height=535,width=700,bd=10,relief=RIDGE,bg='blue')
        self.f1.place(x=0,y=0)
      
        self.f2=Frame(self.f1,height=80,width=680,bd=0,bg='cyan')
        self.f2.place(x=0,y=0)
        self.h1=Label(self.f2,text='FILL OUT THE ALL FIELDS FOR UPDATE TRAIN ',font=('Arial',16,'bold'),bg='cyan',fg='green')
        self.h1.place(x=140,y=20) 
        self.f3=Frame(self.f1,height=500,width=680,bd=10,bg='pink')
        self.f3.place(x=0,y=80)
        self.h1=Label(self.f3,text=' UPDATE MENU',font=("Arial",20,'bold'),fg="spring green",bg='gold',bd=7,relief='groove')
        self.h1.place(x=200,y=10)
        self.Updatetraino=Button(self.f3,text="Update Train Number",font=('Arial',14,'bold'),bg='white',fg='blue',width=25,command=self.Update_train_no,relief='raised',bd=10)
        self.Updatetraino.place(x=0,y=80)
        self.Updatetrainame=Button(self.f3,text="Update Train Name",font=('Arial',14,'bold'),bg='white',fg='blue',width=25,command=self.Update_train_name,relief='raised',bd=10)
        self.Updatetrainame.place(x=0,y=140)
        self.Updatetrainstime=Button(self.f3,text="Update Train Departure Time ",font=('Arial',14,'bold'),bg='white',fg='blue',width=25,command=self.Update_train_Stime,relief='raised',bd=10)
        self.Updatetrainstime.place(x=0,y=200)
        self.Updatetrainetime=Button(self.f3,text="Update Train Arrival Time ",font=('Arial',14,'bold'),bg='white',fg='blue',width=25,command=self.Update_train_Etime,relief='raised',bd=10)
        self.Updatetrainetime.place(x=0,y=260) 
        
#---------------------------------------------------------------Function For Add Price Of Specific Train-----------------------------------------------#        
    def price(self):
        self.be4=Toplevel()
        self.be4.geometry('700x535+280+210')
        self.be4.title('Price page')
        self.f1=Frame(self.be4,height=535,width=700,bd=10,relief=RIDGE,bg='white')
        self.f1.place(x=0,y=0)
      
        self.f2=Frame(self.f1,height=80,width=680,bd=0,bg='cyan')
        self.f2.place(x=0,y=0)
        self.h1=Label(self.f2,text='FILL OUT THE ALL FIELDS FOR INPUT THE PRICE ',font=('Arial',16,'bold'),bg='cyan',fg='green')
        self.h1.place(x=140,y=20) 
        self.f3=Frame(self.f1,height=437,width=680,bd=0,bg='pink')
        self.f3.place(x=0,y=80) 
        self.Trainno=Label(self.f3,text='Enter The Train Number :',font=('Arial',12,'bold'),bg='pink',fg='red')
        self.Trainno.place(x=10,y=10)
        self.Trainno1E=Entry(self.f3,width=25,bd=0,font=('Arial',12,'bold'),bg='white')
        self.Trainno1E.place(x=10,y=40)
        self.pricesl=Label(self.f3,text='Enter The Price for Sleeper :',font=('Arial',12,'bold'),bg='pink',fg='red')
        self.pricesl.place(x=10,y=70)
        self.priceslE=Entry(self.f3,width=25,bd=0,font=('Arial',12,'bold'),bg='white')
        self.priceslE.place(x=10,y=100)
        self.price1A=Label(self.f3,text='Enter The Price for 1A :',font=('Arial',12,'bold'),bg='pink',fg='red')
        self.price1A.place(x=10,y=130)
        self.price1AE=Entry(self.f3,width=25,bd=0,font=('Arial',12,'bold'),bg='white')
        self.price1AE.place(x=10,y=160)
        self.price2A=Label(self.f3,text='Enter The Price for 2A :',font=('Arial',12,'bold'),bg='pink',fg='red')
        self.price2A.place(x=10,y=190)
        self.price2AE=Entry(self.f3,width=25,bd=0,font=('Arial',12,'bold'),bg='white')
        self.price2AE.place(x=10,y=210)
        self.price3A=Label(self.f3,text='Enter The Price for 3A :',font=('Arial',12,'bold'),bg='pink',fg='red')
        self.price3A.place(x=10,y=240)
        self.price3AE=Entry(self.f3,width=25,bd=0,font=('Arial',12,'bold'),bg='white')
        self.price3AE.place(x=10,y=270)
        self.priceGn=Label(self.f3,text='Enter The Price For General :',font=('Arial',12,'bold'),bg='pink',fg='red')
        self.priceGn.place(x=10,y=300)
        self.priceGnE=Entry(self.f3,font=('Arial',14,'bold'))
        self.priceGnE.place(x=10,y=330)
        self.done=Button(self.f3,text="Continue",font=('Arial',14,'bold'),bg='red',fg='blue',width=30,command=self.connect_database1)
        self.done.place(x=130,y=390)
        
    def clear2(self):
        self.Trainno1E.delete(0,END)
        self.priceslE.delete(0,END)
        self.price1AE.delete(0,END)
        self.price2AE.delete(0,END)
        self.price3AE.delete(0,END)
        self.priceGnE.delete(0,END)    
    
    def connect_database1(self):
        if self.Trainno1E.get()=='' or self.priceGnE.get()=='' or self.price1AE.get()=='' or self.price2AE.get()=='' or self.price3AE.get()=='' or self.priceslE.get()=='':
            messagebox.showerror('Error','All fields are required')      
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='Ankit@817raj#',database='train')
                mycursor=con.cursor()
            except:
                messagebox.showerror('Error','Database Connectivity Issue, Please Try Again')    
                return
            try:
                # query='create database train'
                # mycursor.execute(query)
                query='use train'
                mycursor.execute(query)
                query='create table train_price(id int auto_increment unique key not null,pricesl int,price1A int,price2A int,price3A int,pricegn int,Tno int(5))'
                mycursor.execute(query)
            except: 
                mycursor.execute('use train')
            
            
                query='select * from Train_data where Tno=%s'
                mycursor.execute(query,(self.Trainno1E.get())) 
                
                row6=mycursor.fetchone()
                query1='select * from train_price where Tno=%s'
                mycursor.execute(query1,(self.Trainno1E.get()))
                row7=mycursor.fetchone()
                if row6==None:
                    messagebox.showerror('Error','These Train doesnot exist')
                elif row7!=None:
                    query2='update train_price set pricesl=%s,price1A=%s,price2A=%s,price3A=%s,pricegn=%s where Tno=%s' 
                    mycursor.execute(query2,(self.priceslE.get(),self.price1AE.get(),self.price2AE.get(),self.price3AE.get(),self.priceGnE.get(),self.Trainno1E.get())) 
                    # con.commit()
                    messagebox.showinfo('Success','Ticket Price has been updated successfully!!!!')
                    con.commit()
                    con.close()
                       
                else:
                    query='insert into train_price(pricesl,price1A,price2A,price3A,pricegn,Tno) values(%s,%s,%s,%s,%s,%s)'
                    #mycursor.execute(query,())
                    #query='insert into travellers(Name,Age,Gender,Nationality,Preference) values(%s,%s,%s,%s,%s)'
                    mycursor.execute(query,(self.priceslE.get(),self.price1AE.get(),self.price2AE.get(),self.price3AE.get(),self.priceGnE.get(),self.Trainno1E.get()))
                    
                    con.commit()
                    con.close()
                    messagebox.showinfo('Success','Inserted successfully')  
                    self.clear2()     
 
 #-------------------------------------------------------------Function For Show All Train-----------------------------------------------------------------#                   
                    
    def show_train(self):
        self.be5=Toplevel()
        self.be5.geometry('1520x600+5+210')
        self.be5.resizable(0,0)
        self.be5.title("All Trains In Our Project")
        self.show=Frame(self.be5,relief='raised',background="blue",border=10)
        self.show.place(x=0,y=0,width=1520,height=650)
        self.a=["id","Tno","Tname","Spoint","Epoint","S_TIME","E_TIME","price1A","price2A","price3A","pricesl","pricegn"]
        self.b=["SL No.","Train No.","Train Name","From","To","D Time","A Time","1AC Price","2AC Price","3AC Price","Sleeper Price","General Price"]
        self.show_treeview=ttk.Treeview(self.show,columns=("id","Tno","Tname","Spoint","Epoint","S_TIME","E_TIME","price1A","price2A","price3A","pricesl","pricegn"))
        self.show_treeview.place(x=0,y=0,width=1500,height=700)
        for i in range(len(self.a)):
            self.show_treeview.heading(self.a[i],text=self.b[i])
            self.show_treeview.column(self.a[i],width=125)
        self.show_treeview["show"]="headings"
        self.s=ttk.Style(self.be5)
        self.s.theme_use('clam')
        self.s.configure('.',font=('Arial',15,'bold'),background='cyan',foreground='blue')
        self.s.configure('Treeview.Heading',foreground='red',font=('Arial',14,'bold'),background="cyan")
        self.fetch_train()
    
    def fetch_train(self):
        con=pymysql.connect(host='localhost',user='root',password='Ankit@817raj#',database='train')
        mycursor=con.cursor()
        mycursor.execute('select train_data.id,train_data.Tno,Tname,Spoint,Epoint,S_TIME,E_TIME,price1A,price2A,price3A,pricesl,pricegn from train_data,train_price') 
        row8=mycursor.fetchall()
        if len(row8)!=0:
            self.show_treeview.delete(*self.show_treeview.get_children())
            for i in row8:
                self.show_treeview.insert("",END,values=i)
                con.commit()
        con.close() 
        
#-------------------------------------------------------------Function For Show All Passenger------------------------------------------------------------#        
        
    def show_passenger(self):
        self.be6=Toplevel()
        self.be6.geometry('1520x600+5+210')
        self.be6.resizable(0,0)
        self.be6.title("All Passenger Details")
        self.show=Frame(self.be6,relief='raised',background="blue",border=10)
        self.show.place(x=0,y=0,width=1520,height=650)
        self.a=["Tno","Ticketno","name","age","Gender","nationality","frome","toe","class","datee","mobile",'email']
        self.b=["Train No.","Ticket No.","Name","Age","Sex","Nationality","From","To","Class","Date","Mobile No.",'Email Id']
        self.show_treeview=ttk.Treeview(self.show,columns=("Tno","Ticketno","name","age","Gender","nationality","frome","toe","class","datee","mobile",'email'))
        self.show_treeview.place(x=0,y=0,width=1500,height=700)
        for i in range(len(self.a)):
            self.show_treeview.heading(self.a[i],text=self.b[i])
            self.show_treeview.column(self.a[i],width=125)
        self.show_treeview["show"]="headings"
        self.s=ttk.Style(self.be6)
        self.s.theme_use('clam')
        self.s.configure('.',font=('Arial',15,'bold'),background='cyan',foreground='blue')
        self.s.configure('Treeview.Heading',foreground='red',font=('Arial',14,'bold'),background="cyan")
        self.fetch_details()
    
    def fetch_details(self):
        con=pymysql.connect(host='localhost',user='root',password='Ankit@817raj#',database='train')
        mycursor=con.cursor()
        mycursor.execute('select Tno,Ticketno,name,age,gender,nationality,frome,toe,class,datee,mobile,email from book_ticket') 
        row8=mycursor.fetchall()
        if len(row8)!=0:
            self.show_treeview.delete(*self.show_treeview.get_children())
            for i in row8:
                self.show_treeview.insert("",END,values=i)
                con.commit()
        con.close()    
        
#--------------------------------------------------------------------Function For LogOut------------------------------------------------#         
    def log_out(self):
       
        root.destroy()
        import main_page              
            
                                                
#---------------------------------------------------------------Function For Main Menu Of Employee--------------------------------------#    
    def fourth_sem(self,mainwindow):
        self.mainwindow=mainwindow
        self.un=Label(self.mainwindow,text="Railway Reservation \n System",font=("Algerian",27),bg="red",fg="white",width="1000",height="2",bd=15,relief=RIDGE)
        self.un.pack()
        date=dt.datetime.now()
        self.currentlable=Label(self.mainwindow,text=f"{date:%A-%B-%d-%Y}",font=("calibiri",15),bg='red',fg='blue')
        self.currentlable.place(x=20,y=40)
        self.log_out=Button(self.mainwindow,text='Logout',font=('Arial',14,'bold'),bd=5,relief='flat',bg='red',fg='white',command=self.log_out)
        self.log_out.place(x=1400,y=30)
        self.f2=Frame(self.mainwindow,width=1526,height=70,bg='cyan',bd=9,relief=RIDGE)
        self.f2.place(x=0,y=110)
        self.f3=Button(self.f2,text="Passenger Details",font=('Arial',14,'bold'),bg='cyan',fg='blue',width=20,command=self.show_passenger)
        self.f3.place(x=8,y=10)
        self.f3=Button(self.f2,text="Add Train",font=('Arial',14,'bold'),bg='cyan',fg='blue',width=20,command=self.Add_train)
        self.f3.place(x=257,y=10)
        self.Updatetrain=Button(self.f2,text="Update Train",font=('Arial',14,'bold'),bg='cyan',fg='blue',width=20,command=self.update_train_details)
        self.Updatetrain.place(x=506,y=10)
        self.Showtrain=Button(self.f2,text="Show Train",font=('Arial',14,'bold'),bg='cyan',fg='blue',width=20,command=self.show_train)
        self.Showtrain.place(x=756,y=10)
        self.Canceltrain=Button(self.f2,text="Cancel Train",font=('Arial',14,'bold'),bg='cyan',fg='blue',width=20,command=self.cancel_train)
        self.Canceltrain.place(x=1005,y=10)
        self.priceb=Button(self.f2,text="Price",font=('Arial',14,'bold'),bg='cyan',fg='blue',width=20,command=self.price)
        self.priceb.place(x=1255,y=10)
        

CSE_FIRST=CSE_DEPARTMENT()
CSE_FIRST.fourth_sem(root)        
root.mainloop()
# xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxEnd Of Admin Page xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx 