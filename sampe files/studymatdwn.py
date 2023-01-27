import shutil, os
from tkinter import *
from PIL import Image,ImageTk
from tkinter import filedialog
from tkinter import messagebox as ms
import os


stud_study_mat_down_window = Tk()
stud_study_mat_down_window.title("Students study materials Download")

stud_study_mat_down_window.geometry("600x450")
stud_study_mat_down_window.iconbitmap('face5.ico')
stud_study_mat_down_window.resizable(False, False)
stud_study_mat_down_window.configure(background='gray')
Download_logo_photo = PhotoImage(file = r"Datas/src_images/download-logo-12.png")

scroll_bar = Scrollbar(stud_study_mat_down_window)
scroll_bar.pack( side = RIGHT,fill = Y )
mylist = Listbox(stud_study_mat_down_window,font = ('calibri', 22, ' bold '),background='gray',yscrollcommand = scroll_bar.set )



study_mat_down_files=os.listdir('Datas/study_materials')
for linenum,line in enumerate(study_mat_down_files):
	mylist.insert(END,str(linenum+1)+'. '+str(line))
	mylist.insert(END,'\n')
mylist.pack( side = TOP, fill = BOTH ,expand=True )
scroll_bar.config( command = mylist.yview )
frame = Frame(stud_study_mat_down_window)
frame.pack(fill=X,side=BOTTOM)
lbt1=Label(frame,text="Click here-->",font = ('calibri', 22, ' bold '))
lbt1.pack(fill = X,side=LEFT)


def download_study_materials_file():
     filename = filedialog.asksaveasfilename(title ="Select Image")
     if filename:
          if filename.endswith('.pdf'):
              shutil.copy('Datas/study_materials/'+clicked.get(),filename)
              ms.showinfo('Success!','File Downloaded')
          elif filename:
               fullfilename=filename+'.pdf'
               shutil.copy('Datas/study_materials/'+clicked.get(),fullfilename)
               ms.showinfo('Success!','File Downloaded')
          else:
               ms.showerror('Error!','Selected file is not video file \nMake sure it is mp4 or mkv file.')

stasgnup_btn1=Button(frame,image=Download_logo_photo,command=download_study_materials_file)
stasgnup_btn1.pack(side=LEFT)
clicked = StringVar()
clicked.set( study_mat_down_files[-1] )
drop_study_mat = OptionMenu( frame , clicked , *study_mat_down_files )
drop_study_mat.config( font=('calibri', 20, ' bold '))
drop_study_mat.pack(fill = X,side=LEFT)
stud_study_mat_down_window.mainloop()
 
