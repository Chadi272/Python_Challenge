#Importing modules
import os
import csv
#Path to Excel csv file
csvpath = os.path.join(os.path.expanduser('~'),'Documents','GitHub', 'Python_Challenge','PyBank','Resources','budget_data.csv')
textpath = os.path.join(os.path.expanduser('~'),'Documents','GitHub', 'Python_Challenge','PyBank','Analysis','Analysis.txt')
#create text file
f = open(textpath, "w")
#Read file to work with data
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #Start variables
    totalv = 0
    rowcount = 0
    maxm = 0
    #Define list
    Mylist = []
    Mynlist = []
    Changepermonthlist = []
    #Skip headers
    next(csvreader)
    #Starting the loop through the rows
    for row in csvreader:
        #Total months
        rowcount += 1
        #Total P/L
        totalv += int(row[1])
        #Set the column values as integer
        rowv = int(row[1])
        #Define lists
        Mynlist += [rowv]
        Mynlist.pop(0)
        #Change in Profit/Loss
        zip_object = zip(Mylist, Mynlist)
        changelist = []
        for Mylist, Mynlist in zip_object:
            changelist.append(Mynlist-Mylist)
        change = sum(changelist)
        #Add values in Profit/Loss to the list
        Mylist += [rowv]
        #Max value in the list
        maxv = max(Mylist)
        #Min value in the list
        minv = min(Mylist)
        #Find month for max value
        if maxv == int(row[1]):
            maxm = row[0]
        #Find month for min value
        if minv == int(row[1]):
            minm = row[0]
        #Format values
        maxvl = '{:,}'.format(maxv)
        minvl = '{:,}'.format(minv)

    print("Financial Analysis")
    print("---------------------------")
    print(f'Total Months: {int(rowcount)}')
    print(f'Total: ${"{:,}".format(totalv)}')
    print(f'Greatest Increase in Profits: {maxm} (${maxvl})')
    print(f'Greatest Decrease in Profits: {minm} (${minvl})')
    print(change)

f.write("Financial Analysis")
f.write('\n')
f.write("---------------------------")
f.write('\n')
f.write(f'Total Months: {int(rowcount)}')
f.write('\n')
f.write(f'Total: ${"{:,}".format(totalv)}')
f.write('\n')
f.write(f'Greatest Increase in Profits: {maxm} (${maxvl})')
f.write('\n')
f.write(f'Greatest Decrease in Profits: {minm} (${minvl})')

