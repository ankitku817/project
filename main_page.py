from tkinter import*
from PIL import ImageTk # type: ignore
import datetime as dt
root=Tk()
root.geometry("1530x1000")
# root.resizable(0,0)
#-----------------------------------------------Frist Image Of Our Project-------------------------------------------------------#
root.title("Railaway Reservation System")
headImage=ImageTk.PhotoImage(file="bg1.jpg")
headLable=Label(root,image=headImage)
headLable.place(x=0,y=0)
#-----------------------------------------------Create Class Named As Railway_Reservation_System---------------------------------#
class Railway_reservation_system:
    def travellers(self):
        root.destroy()
        import Passenger_Login_file
    def employee(self):
        root.destroy()
        import Employeee    
    def __init__(self):
        date=dt.datetime.now()
        self.currentlable=Label(root,text=f"{date:%A\n%B-%d-%Y}",font=("calibiri",20),bg='white',fg='blue')
        self.currentlable.place(x=10,y=45)
        self.user=Button(root,text="Travellers",font=('Arial',23,'bold'),bg='pink',fg='blue',width=10,relief='raised',bd=15,command=self.travellers)
        self.user.place(x=1200,y=400)
        self.emp=Button(root,text="Employee",font=('Arial',23,'bold'),bg='orange',fg='blue',width=10,relief='raised',bd=15,command=self.employee)
        self.emp.place(x=1200,y=500)                         
project=Railway_reservation_system()        
root.mainloop()