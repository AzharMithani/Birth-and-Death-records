# # Convert xlsx files to csv

'''
'filename' to the name of the excel sheet 
'sheetname' to name of the sheet in excel file
'output_filename' to the name of the output_file
'''

import pandas as pd
import sys

def convert(filename, sheetname,output_filename):
    data_xls = pd.read_excel(filename, sheetname,header = 3, dtype = {'Date Of Event':object}, index_col=None)
    data_xls = data_xls[4:]
    data_xls['Sr. No.'] = data_xls['Sr. No.'] - 4

    new_dates = []
    for row in data_xls['Date Of Event']:
        row = str(row)
        if len(row) > 10:
            new = row.split(' ')[0]
            news = new.split('-')
            news[0], news[1], news[2] = news[1], news[2], news[0]
            new_dates.append('/'.join(news))
        else:
            new_dates.append(row)
    data_xls['Date Of Event'] = new_dates

    data_xls.to_csv(output_filename, encoding='utf-8', index=None)
    print("Succesfully converted!")
	

inputs = sys.argv
filename = inputs[1]
sheetname = inputs[2]
output_filename = inputs[3]
convert(filename,sheetname,output_filename)


