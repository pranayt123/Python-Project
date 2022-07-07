from tkinter import *  
from tkinter import Label
import twilio
import random 
parent = Tk()  
parent.geometry("300x250")
e1 = Label(parent,text = "mobile number: ").grid(row = 0, column = 0)  
e1 = Entry(parent).grid(row = 0, column = 1)  
OTP=random.randint(100000,999999)
from twilio.rest import Client
account_sid ='AC4490d9081aea564bcbe43519a3aa9317'
auth_token ='b5b9cbb285b454b90510ecc6dc98be3a'
client = Client(account_sid, auth_token)
message = client.messages.create(
                     body="Your OTP is ::"+str(OTP),
                     from_='+16265087584',
                     to='+917796292167',
                )
print("------------------------")
print("------------------------")
print("Successfully sent")
password = Label(parent,text = "your OTP is: ").grid(row = 1, column = 0)  
e2 = Entry(parent).grid(row = 1, column = 1) 
def submit1():
    if e2==str(OTP):
     print("verified")
     print("------------------------")
     print("------------------------")
     lab1= Label(text='Please Enter Valid OTP')
     lab1.place(x=60,y=90)
    else:
     lab2=Label(parent,text="Successfull!!")
     lab2.place(x=100,y=110)
     print("------------------------")
     print("------------------------")
submit = Button(parent, text = "Submit",command=submit1).grid(row = 4, column = 0)  
parent.mainloop()
