import os
import csv

#file = open('C:\Users\chadi\Documents\GitHub\Python_Challenge\PyBank\Resources\budget_data.csv')
#csvfile = csv.reader(file)

csvpath = os.path.join(os.path.expanduser('~'),'Documents','GitHub', 'Python_Challenge','PyBank','Resources','budget_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)