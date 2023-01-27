import pandas as pd
writer = pd.ExcelWriter('demo.xlsx', engine='xlsxwriter')
writer.save()
