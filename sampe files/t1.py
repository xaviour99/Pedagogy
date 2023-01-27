import pandas as pd
import os
import datetime
import csv
from openpyxl import load_workbook
f1=pd.read_excel(
     ("Datas/zoom_meeting_items/zoom_meet_xlfiles/List.xlsx"),
     engine='openpyxl',)



# new dataframe with same columns
df = pd.DataFrame({'Time(in format: dd-mm-yyyy hh:mm AM/PM)':['05-06-2021  6:47:00 PM'],
    'link':['https://zoom.us/j/94004671830?pwd=UjVqWVV6VUVjMFJ6aDFIcmR5cGhGdz09']})
writer = pd.ExcelWriter("Datas/zoom_meeting_items/zoom_meet_xlfiles/List.xlsx", engine='openpyxl')
# try to open an existing workbook
writer.book = load_workbook("Datas/zoom_meeting_items/zoom_meet_xlfiles/List.xlsx")
# copy existing sheets
writer.sheets = dict((ws.title, ws) for ws in writer.book.worksheets)
# read existing file
reader = pd.read_excel(r"Datas/zoom_meeting_items/zoom_meet_xlfiles/List.xlsx")
# write out the new sheet
df.to_excel(writer,index=False,header=False,startrow=len(reader)+1)

writer.close()
