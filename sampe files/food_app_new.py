import numpy as np
import cv2
import keras 
import random
import matplotlib.pyplot as plt
from keras.models import load_model
import cv2
from sklearn.preprocessing import LabelBinarizer
from keras.preprocessing import image
from keras.preprocessing.image import img_to_array
from tkinter import *
from PIL import Image,ImageTk
from tkinter import filedialog
import cv2
import sqlite3

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
#from tensorflow import keras
load_model = keras.models.load_model('cnn_model.h5')
EPOCHS = 25
INIT_LR = 1e-3
BS = 32
default_image_size = tuple((256, 256))
directory_root = 'food/'

image_size = 0
width=256
height=256
depth=3

dbase=sqlite3.connect("orphanagedata.db")
dbase.execute('''CREATE TABLE IF NOT EXISTS
                ORGDATA(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                ORGNAME TEXT,
                ORGTYPE TEXT,
                FOODTYPE TEXT,
                FOODCOUNT INT,
                PLACE TEXT,
                PHONE TEXT,
                EMAIL TEXT)''')

dbase.commit()
dbase.close()



def convert_image_to_array(image_dir):
    try:
        image = cv2.imread(image_dir)
        if image is not None:
            image = cv2.resize(image, default_image_size) 
            
            return img_to_array(image)
        else :
            return np.array([])
    except Exception as e:
        print("Error in Image : {}".format(e))
        return None
    
label_list=['burger' ,'butter_naan' ,'chai', 'chapati', 'chole_bhature', 'dal_makhani',
 'dhokla', 'fried_rice', 'idli', 'jalebi', 'kaathi_rolls', 'kadai_paneer',
 'kulfi', 'masala_dosa', 'momos', 'paani_puri', 'pakode', 'pav_bhaji', 'pizza',
 'samosa']
    
labelbinarizer = LabelBinarizer()
labelbinarizer.fit_transform(label_list)


meals=[  'chole_bhature', 'dal_makhani',  'fried_rice',  'kaathi_rolls', 'kadai_paneer' ]
tiffin=['burger' ,'butter_naan' , 'idli','pav_bhaji', 'pizza','masala_dosa','chapati','momos']
snacks=['chai','jalebi','kulfi', 'pakode','samosa','paani_puri','dhokla',]

root = Tk()

root.title('Food Prediction')
root.geometry('1200x700')
root.resizable(False,False)
rval=StringVar()
ent1=IntVar()
food_type=''
orgnamew=StringVar()
orgtypew=StringVar()
foodtypew=StringVar()
foodcountw=IntVar()
placew=StringVar()
phnow=StringVar()
emailw=StringVar()

def add_org():

    def add_data():

        orgnamew1=orgnamew.get()
        orgtypew1=orgtypew.get()
        foodtypew1=foodtypew.get()
        foodcountw1=foodcountw.get()
        placew1=placew.get()
        phnow1=phnow.get()
        emailw1=emailw.get()

        
        
        dbase2=sqlite3.connect("orphanagedata.db")
        dbase2.execute('''CREATE TABLE IF NOT EXISTS
                    ORGDATA(
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    ORGNAME TEXT,
                    ORGTYPE TEXT,
                    FOODTYPE TEXT,
                    FOODCOUNT INT,
                    PLACE TEXT,
                    PHONE TEXT,
                    EMAIL TEXT)''')

        dbase2.commit()
        dbase2.execute("INSERT INTO ORGDATA(ORGNAME,ORGTYPE,FOODTYPE,FOODCOUNT,PLACE,PHONE,EMAIL) VALUES(?,?,?,?,?,?,?)",
                       (orgnamew1,orgtypew1,foodtypew1,foodcountw1,placew1,phnow1,emailw1))
        dbase2.commit()

        print("saved")
        dbase2.close()

    addwindow=Toplevel(root)
    addwindow.title("Add Organisation")
    addwindow.geometry('800x650')
    addwindow.resizable(False,False)
    lbw1 = Label(addwindow,text = 'Food Prediction And Sharing',font=('calibri',25,'bold'), bg='grey',fg='white')
    lbw1.pack()

   

    

    lbw3 = Label(addwindow,text = 'Organisation Name : ',font = ('calibri',18,'bold'))
    lbw3.place(x=100,y=150)

    txw3=Entry(addwindow,textvariable=orgnamew,font = ('calibri',18,'bold'),bg='lightblue',fg='black')
    txw3.place(x=400,y=150)

    lbw4 = Label(addwindow,text = 'Organisation Type : ',font = ('calibri',18,'bold'))
    lbw4.place(x=100,y=200)

    txw4=Entry(addwindow,textvariable=orgtypew,font = ('calibri',18,'bold'),bg='lightblue',fg='black')
    txw4.place(x=400,y=200)

    lbw5 = Label(addwindow,text = 'Food Type',font = ('calibri',18,'bold'))
    lbw5.place(x=100,y=250)

    txw5=Entry(addwindow,textvariable=foodtypew,font = ('calibri',18,'bold'),bg='lightblue',fg='black')
    txw5.place(x=400,y=250)

    

    lbw6 = Label(addwindow,text = 'Food Count',font = ('calibri',18,'bold'))
    lbw6.place(x=100,y=300)

    txw6=Spinbox(addwindow,textvariable=foodcountw,font=('calibri',18),bg='lightblue',fg='black',from_=1, to=10000,width=19)
    txw6.place(x=400,y=300)

    lbw7 = Label(addwindow,text = 'Location',font = ('calibri',18,'bold'))
    lbw7.place(x=100,y=350)

    txw7=Entry(addwindow,textvariable=placew,font = ('calibri',18,'bold'),bg='lightblue',fg='black')
    txw7.place(x=400,y=350)

    lbw8 = Label(addwindow,text = 'Phno',font = ('calibri',18,'bold'))
    lbw8.place(x=100,y=400)

    txw8=Entry(addwindow,textvariable=phnow,font = ('calibri',18,'bold'),bg='lightblue',fg='black')
    txw8.place(x=400,y=400)

    lbw9 = Label(addwindow,text = 'email',font = ('calibri',18,'bold'))
    lbw9.place(x=100,y=450)

    txw9=Entry(addwindow,textvariable=emailw,font = ('calibri',18,'bold'),bg='lightblue',fg='black')
    txw9.place(x=400,y=450)

    btn4 = Button(addwindow,text='ADD ORGANISATION DATA',bg='#768fe8',fg='white',font=('calibri',14,'bold'),
              activebackground='#4d4d4d',activeforeground='white',
              width=20,height=1,command=add_data) 
    btn4.place(x=300,y=550)

    
    
    addwindow.mainloop()
    
    

def openfilename():
  
    # open file dialog box to select image
    # The dialogue box has a title "Open"
    filename = filedialog.askopenfilename(title ="Select Image")
    return filename

def open_img():
    # Select the Imagename  from a folder 
    x = openfilename()
  
    # opens the image
    img = Image.open(x,'r')
      
    # resize the image and apply a high-quality down sampling filter
    img = img.resize((353, 310), Image.ANTIALIAS)
  
    # PhotoImage class is used to add image to widgets, icons etc
    img = ImageTk.PhotoImage(img)
   
    # create a label
    panel = Label(root, image = img)
      
    # set the image as img 
    panel.image = img
    panel.place(x=70,y=100)
    
    return x


def pred_food():

    global image_directory
    
    
    image_directory = open_img()
    print(image_directory)
    if image_directory.endswith(".jpg") == True or image_directory.endswith(".JPG") == True or image_directory.endswith(".png") == True:
        img3 = image_directory
        img5 = cv2.imread(img3)
       
        
        imar = convert_image_to_array(img3)
        img4 = cv2.imread(img3)
        hsv = cv2.cvtColor(img4, cv2.COLOR_BGR2HSV)
        lower_range = np.array([10, 100, 20])
        upper_range = np.array([20, 255, 200])
        mask = cv2.inRange(hsv, lower_range, upper_range)
       

        npimagelist = np.array([imar], dtype=np.float16) / 225.
        PREDICTEDCLASSES2 = load_model.predict_classes(npimagelist)
        pr=labelbinarizer.classes_[PREDICTEDCLASSES2]
        
        print(pr)
        msg1.config(text=pr[0])
        global food_type
        if pr[0] in meals:
            
            food_type='Meals'
            msg2.config(text=str("Meals"))
            
        elif pr[0] in tiffin:
            food_type='Tiffin'
            msg2.config(text=str("Tiffin"))
            
        elif pr[0] in snacks:
            food_type='Snack'
            msg2.config(text=str("Snacks"))
        else:
            food_type=''
            msg2.config(text=str("Unknown"))
           
def search_org():

    global qval
    qval=ent1.get()
    print(qval)
    import numpy as np
    with sqlite3.connect("orphanagedata.db") as dbase:
        cur=dbase.cursor()

    con3=cur.execute("SELECT * FROM ORGDATA WHERE FOODTYPE=?  ",(food_type,))

    val4=con3.fetchall()

    val5={}

    for  x in val4:
        val5.update({x[4]:x[0]})
    print(val5)                 

    val5list=list(val5.keys())
    print(val5list)
    def closest(lst, K):
            
            lst = np.asarray(lst)
            idx = (np.abs(lst - K)).argmin()
            return lst[idx]
            
    # Driver code

    K = qval

    keyv=closest(val5list, K)

    v=val5[keyv]
    print(v)

    con4=cur.execute("SELECT * FROM ORGDATA WHERE ID=?  ",(v,))

    val6=con4.fetchall()

    cur.close()

    
    if val6!=[]:
        print(val6[0])
        (id1,orgname1,orgtype1,foodtype1,foodcount1,place1,phno1,email1)=val6[0]
        print(id1,orgname1,orgtype1,foodtype1,foodcount1,place1,phno1,email1)

        msg3.configure(text=orgname1)

        msg4.configure(text=orgtype1)

        msg5.configure(text=foodcount1)

        msg6.configure(text=foodtype1)

        msg7.configure(text=place1)

        msg8.configure(text=phno1)

        msg9.configure(text=email1)

        def send_the_mail():
          
            fromaddr = "tfriends513@gmail.com"
            toaddr = email1

            # instance of MIMEMultipart
            msg = MIMEMultipart()

            # storing the senders email address
            msg['From'] = fromaddr

            # storing the receivers email address
            msg['To'] = toaddr

            # storing the subject
            msg['Subject'] = "Requesting for collecting the food"

            # string to store the body of the mail
            body = "Hi there, \n          we have {} {} kindly pick the food as soon as possible".format(qval,foodtype1)

            # attach the body with the msg instance
            msg.attach(MIMEText(body, 'plain'))

            # open the file to be sent
            filename = "food.jpg"
            attachment = open(image_directory, "rb")

            # instance of MIMEBase and named as p
            p = MIMEBase('application', 'octet-stream')

            # To change the payload into encoded form
            p.set_payload((attachment).read())

            # encode into base64
            encoders.encode_base64(p)

            p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

            # attach the instance 'p' to instance 'msg'
            msg.attach(p)

            # creates SMTP session
            s = smtplib.SMTP('smtp.gmail.com', 587)

            # start TLS for security
            s.starttls()

            # Authentication
            s.login(fromaddr, "tree@143")

            # Converts the Multipart msg into a string
            text = msg.as_string()

            # sending the mail
            s.sendmail(fromaddr, toaddr, text)

            # terminating the session
            s.quit()



        


        btn4 = Button(root,text='SEND EMAIL',bg='#768fe8',fg='white',font=('calibri',14,'bold'),
              activebackground='#4d4d4d',activeforeground='white',
              width=20,height=1,command=send_the_mail) 
        btn4.place(x=800,y=610)

        

    
    
    
    
    
lb1 = Label(root,text = 'Food Prediction And Sharing',font=('calibri',25,'bold'), bg='grey',fg='white')
lb1.pack()

lb2 = Label(root,text = 'Predicted Food',font = ('calibri',18,'bold'))
lb2.place(x=450,y=100)

lb3 = Label(root,text = 'Food type',font = ('calibri',18,'bold'))
lb3.place(x=500,y=190)



msg1 = Label(root,text='',font=('calibri',20),bg='lightblue',fg='black',width=18)
msg1.place(x=610,y=100)

msg2 = Label(root,text='',font=('calibri',20),bg='lightblue',fg='black',width=18)

msg2.place(x=610,y=190)






lb = Label(root,text='',bg='white',width=50,height=20)
lb.place(x=70,y=100)

lb4 = Label(root,text = 'Quantity',font = ('calibri',18,'bold'))
lb4.place(x=500,y=290)

txt1=Spinbox(root,textvariable=ent1,font=('calibri',20),bg='lightblue',fg='black',from_=1, to=10000,width=17)
txt1.place(x=610,y=290)

lb5 = Label(root,text = 'Organisation Name: ',font = ('calibri',18,'bold'))
lb5.place(x=430,y=440)

msg3 = Label(root,text='',font=('calibri',20),bg='lightblue',fg='black',width=26)
msg3.place(x=650,y=440)

lb6 = Label(root,text = 'Organisation Type ',font = ('calibri',18,'bold'))
lb6.place(x=120,y=500)

msg4 = Label(root,text='',font=('calibri',22),bg='lightblue',fg='black',width=20)
msg4.place(x=70,y=540)

lb7 = Label(root,text = 'Food Needed',font = ('calibri',18,'bold'))
lb7.place(x=450,y=500)

msg5 = Label(root,text='',font=('calibri',22),bg='lightblue',fg='black',width=4)
msg5.place(x=420,y=540)

msg6 = Label(root,text='',font=('calibri',22),bg='lightblue',fg='black',width=8)
msg6.place(x=510,y=540)

lb8 = Label(root,text = 'Location',font = ('calibri',18,'bold'))
lb8.place(x=800,y=500)

msg7 = Label(root,text='',font=('calibri',22),bg='lightblue',fg='black',width=20)
msg7.place(x=700,y=540)

lb9 = Label(root,text = 'Ph.no:',font = ('calibri',18,'bold'))
lb9.place(x=70,y=610)

msg8 = Label(root,text='',font=('calibri',18),bg='lightblue',fg='black',width=12)
msg8.place(x=150,y=610)

lb10 = Label(root,text = 'email:',font = ('calibri',18,'bold'))
lb10.place(x=350,y=610)

msg9 = Label(root,text='',font=('calibri',18),bg='lightblue',fg='black',width=25)
msg9.place(x=420,y=610)



btn1 = Button(root,text='UPLOAD',bg='#768fe8',fg='white',font=('calibri',10,'bold'),
              activebackground='#4d4d4d',activeforeground='white',
              width=12,height=2,command=pred_food) 
btn1.place(x=200,y=420)

btn2 = Button(root,text='SEARCH ORPHANAGE',bg='#768fe8',fg='white',font=('calibri',14,'bold'),
              activebackground='#4d4d4d',activeforeground='white',
              width=20,height=1,command=search_org) 
btn2.place(x=500,y=366)

btn3 = Button(root,text='ADD ORPHANAGE',bg='#768fe8',fg='white',font=('calibri',14,'bold'),
              activebackground='#4d4d4d',activeforeground='white',
              width=20,height=1,command=add_org) 
btn3.place(x=800,y=366)




root.mainloop()
