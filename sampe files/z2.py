""" 
Python program to automatically join the online zoom classes 
based on the given input in the Excel sheet List.xlsx
the input should be in the given format

Time : dd-mm-yyyy hh:mm AM/PM
Meeting ID : 123456123 (string)
Meeting Password : 1234 (string)

IMP - If you want to change the program path jump to line 40

Disclaimer:
I am not responsible for any troubles caused to you
if the program does not function as intended, or if it is misused,
please make sure to test it before executing

Modules used:

pyautogui - https://pyautogui.readthedocs.io/en/latest/
openpyxl - https://openpyxl.readthedocs.io/en/stable/
PIL - https://pillow.readthedocs.io/en/stable/
"""

import shutil, os
from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
from tkinter import filedialog
from tkinter import messagebox as ms
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle
#zoom_list_file='List.xlsx'


stud_zoom_class_window=Tk()
stud_zoom_class_window.title("Staff Home Page")

                             
stud_zoom_class_window.geometry('1280x700')
stud_zoom_class_window.iconbitmap('face5.ico')
stud_zoom_class_window.resizable(False, False)
stud_zoom_class_window.configure(background='gray')
stud_zoom_class_window.grid_rowconfigure(0, weight=1)
stud_zoom_class_window.grid_columnconfigure(0, weight=1)
load = Image.open('face6.jpg')
render = ImageTk.PhotoImage(load)
img = Label(stud_zoom_class_window, image=render)
img.place(x=0, y=0, relwidth=1, relheight=1)
stud_zoom_label = tk.Label(stud_zoom_class_window, text="Choose the subject" ,bg="lightblue"  ,fg="black"  ,width=45  ,height=1,font=('calibri', 40, 'bold')) 
stud_zoom_label.pack(side=TOP)

def zoom_class_deploy(zoom_list_file):
     try:
          import  datetime, time, subprocess, csv, os, webbrowser

          try:
              import pyautogui
              import openpyxl
              from PIL import Image
          except ModuleNotFoundError as err:
              print("not installed modules please go through the read me files, press anything to exit")
              input()
          #enabling mouse fail safe

          
          pyautogui.FAILSAFE = True

          #copying data from excel sheet to the program
          meetings = []
          wb = openpyxl.load_workbook(zoom_list_file)
          sheet = wb['Sheet1']

          for i in sheet.iter_rows(values_only = True):
              if i[0] != None:   
                  meetings.append(i)
          meetings.pop(0)
          meetings.sort()


          #function to manualy join if no link is provided
          def manualjoin(id, password = ""):
              
              time.sleep(3)

              #locating the zoom app
              while True:
                  var = pyautogui.locateOnScreen('Datas/zoom_meeting_items/zoom_src_images/final.png', confidence=0.9)
                  if var != None:
                      pyautogui.click(var)
                      break
                  elif (time.time() - cur) >= 120:
                      print("App Not opened")
                      break
                  #check every 30 secs
                  time.sleep(30)

              time.sleep(3)

              #entering the meeting id
              pyautogui.typewrite(id)

              #disabling video source
              var = pyautogui.locateOnScreen('Datas/zoom_meeting_items/zoom_src_images/videooff.png', confidence=0.9)
              pyautogui.click(var)

              #clicking the join button
              var = pyautogui.locateOnScreen('Datas/zoom_meeting_items/zoom_src_images/join.png', confidence=0.9)
              join = (var[0] + 75, var[1] + 10, var[2], var[3])
              pyautogui.moveTo(pyautogui.center(join))
              pyautogui.click(join)

              time.sleep(3)

              #checking and entering if meeting password is enabled
              if pyautogui.locateOnScreen('Datas/zoom_meeting_items/zoom_src_images/password.png', confidence=0.9) != None :
                  pyautogui.typewrite(password)
                  var = pyautogui.locateOnScreen('Datas/zoom_meeting_items/zoom_src_images/joinmeeting.png', confidence=0.9)
                  pyautogui.click(var)

              return



          def linkjoin(link):
              #open the given link in web browser
              webbrowser.open(link)
              start = time.time()
              time.sleep(3)
              


          #Iterating through the meeting list to jointate the specified time
          for i in range(len(meetings)):
              curmeeting = meetings[i]

              #Setting the meeting Times
              cur = round(time.time(), 0)
              temp = curmeeting[0].timestamp()

              #join a minute early for later scheduled class
              if(cur < temp - 60):
                  print("next class in ", end ="")
                  print(datetime.timedelta(seconds = (temp - cur) - 60))
                  time.sleep(temp - cur - 60)
              #if more than 5 minutes have passed already
              elif (cur - temp) > 300:
                  print("skipped meeting " + str(i + 1))
                  continue
                  
              var = os.system("taskkill /f /im Zoom.exe")
              
              
              #check if link is provided
              if curmeeting[1] != None:
                  linkjoin(str(curmeeting[1]))
              #check if 
              if curmeeting[2] != None:
                  subfolders = [ f.path for f in os.scandir("C:\\Users") if f.is_dir() ]
                  #opening the zoom app, if you are running on a different OS or the path is different
                  #change the path here 
                  for i in subfolders:
                      if os.path.isfile(i + "\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"):
                          subprocess.Popen(i + "\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe")  
                  manualjoin(str(curmeeting[2]), str(curmeeting[3]))
              
              else:
                  print("data insufficient, press anything to exit")
                  input()
                  exit()

              time.sleep(5)
              
          
          ms.showinfo('Thank you!','Meeting has ended')
          var = os.system("taskkill /f /im Zoom.exe")
          
          
          
     except:
          ms.showerror('Error!','Something went Wrong Try Again.')
          stud_zoom_class_window.destroy()
#zoom_class_deploy('Datas/zoom_meeting_items/zoom_meet_xlfiles/List.xlsx')

     
def Java_func():
     zoom_class_deploy('Datas/zoom_meeting_items/zoom_meet_xlfiles/Java_meet.xlsx')
     

def Web_Technology_func():
     zoom_class_deploy('Datas/zoom_meeting_items/zoom_meet_xlfiles/Web_Technology_meet.xlsx')

def Software_testing_func():
     
     zoom_class_deploy('Datas/zoom_meeting_items/zoom_meet_xlfiles/Software testing_meet.xlsx')

def Mobile_app_development_func():
     zoom_class_deploy('Datas/zoom_meeting_items/zoom_meet_xlfiles/Mobile_app_development_meet.xlsx')

def Fundamentals_of_datascience_func():
     zoom_class_deploy('Datas/zoom_meeting_items/zoom_meet_xlfiles/Fundamentals_of_datascience_meet.xlsx')

def Data_Structures_func():
     zoom_class_deploy('Datas/zoom_meeting_items/zoom_meet_xlfiles/Data_Structures_meet.xlsx')
     
stud_sub_zoom_btn1 = tk.Button(stud_zoom_class_window,command=Java_func, text="Java"  ,fg="black"  ,bg="lightblue"  ,width=15  ,height=1, activebackground = "#002266",activeforeground="#80b3ff" ,font=('calibri', 24, ' bold '))
stud_sub_zoom_btn1.place(x=20, y=100)

stud_sub_zoom_btn2 = tk.Button(stud_zoom_class_window,command=Web_Technology_func, text="Web Technology"  ,fg="black"  ,bg="lightblue"  ,width=15  ,height=1, activebackground = "#002266",activeforeground="#80b3ff" ,font=('calibri', 24, ' bold '))
stud_sub_zoom_btn2.place(x=20, y=200)

stud_sub_zoom_btn3 = tk.Button(stud_zoom_class_window,command=Software_testing_func, text="Software testing"  ,fg="black"  ,bg="lightblue"  ,width=15  ,height=1, activebackground = "#002266",activeforeground="#80b3ff" ,font=('calibri', 24, ' bold '))
stud_sub_zoom_btn3.place(x=20, y=300)

stud_sub_zoom_btn4 = tk.Button(stud_zoom_class_window,command=Mobile_app_development_func, text="Mobile app development"  ,fg="black"  ,bg="lightblue"  ,width=25  ,height=1, activebackground = "#002266",activeforeground="#80b3ff" ,font=('calibri', 24, ' bold '))
stud_sub_zoom_btn4.place(x=20, y=400)

stud_sub_zoom_btn5 = tk.Button(stud_zoom_class_window,command=Fundamentals_of_datascience_func, text="Fundamentals of datascience"  ,fg="black"  ,bg="lightblue"  ,width=25  ,height=1, activebackground = "#002266",activeforeground="#80b3ff" ,font=('calibri', 24, ' bold '))
stud_sub_zoom_btn5.place(x=20, y=500)

stud_sub_zoom_btn6 = tk.Button(stud_zoom_class_window,command=Data_Structures_func, text="Data Structures"  ,fg="black"  ,bg="lightblue"  ,width=15  ,height=1, activebackground = "#002266",activeforeground="#80b3ff" ,font=('calibri', 24, ' bold '))
stud_sub_zoom_btn6.place(x=20, y=600)               
                
stud_zoom_class_window.mainloop()

var = os.system("taskkill /f /im Zoom.exe")
