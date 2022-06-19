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
    totalchange = 0
    #Define list
    Monthlist = []
    Mylist = []
    list1 = []
    test = []
    #Skip headers
    next(csvreader)
    #Starting the loop through the rows
    for row in csvreader:
        #Total months
        months = row[0]
        Monthlist += [months]
        rowcount = len(Monthlist)
        #Total P/L
        totalv += int(row[1])
        #Change

        list1 += [totalv]
        for i in list1:
            value1 = i
            value2 = i+1
            change = value2 - value1
            test += [change]
            #totalchange += change
        #Set the column values as integer
        rowv = int(row[1])
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
    print(test)


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

