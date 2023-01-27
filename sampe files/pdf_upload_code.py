import shutil, os
from tkinter import *
from PIL import Image,ImageTk
from tkinter import filedialog
from tkinter import messagebox as ms
import os
stf_study_materials_window = Tk()
stf_study_materials_window.title("study materials")

stf_study_materials_window.geometry("600x400")
stf_study_materials_window.iconbitmap('face5.ico')
stf_study_materials_window.resizable(False, False)
stf_study_materials_window.configure(background='gray')
pdf_upload_photo = PhotoImage(file = r"Datas/src_images/upload_pdf_logo.png") 
scroll_bar = Scrollbar(stf_study_materials_window)

scroll_bar.pack( side = RIGHT,fill = Y )

mylist = Listbox(stf_study_materials_window,font = "40",background='gray',yscrollcommand = scroll_bar.set )

pdf_files=os.listdir('Datas/study_materials')

for linenum,line in enumerate(pdf_files):
	mylist.insert(END,str(linenum+1)+'. '+str(line))
	mylist.insert(END,'\n')


def openfile_up_pdf():
     filename = filedialog.askopenfilename(title ="Select pdf")
     
     if filename:
          uppdffile=filename.split('/')
          if uppdffile[-1] in pdf_files:
               ms.showerror('Error!','file Already exists')
               
          elif filename.endswith('.pdf'):
               shutil.copy(filename, 'Datas/study_materials')
               cr_pdf_files=os.listdir('Datas/study_materials')
               
               
               ms.showinfo('Success!',uppdffile[-1]+' Upload Successfully!')
               mylist.insert(END,str(len(cr_pdf_files))+'. '+str(uppdffile[-1]))
               mylist.insert(END,'\n')
          else:
               ms.showerror('Error!','Selected file is not pdf file \nMake sure it is pdf.')



mylist.pack( side = TOP, fill = BOTH ,expand=True )
scroll_bar.config( command = mylist.yview )

rc_btn1=Button(stf_study_materials_window,image=pdf_upload_photo,command=openfile_up_pdf)
rc_btn1.place(x=480,y=300)


stf_study_materials_window.mainloop()
