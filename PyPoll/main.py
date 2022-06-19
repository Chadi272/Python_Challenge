#Importing modules
import os
import csv
#Path to files
csvpath = os.path.join(os.path.expanduser('~'),'Documents','GitHub', 'Python_Challenge','PyPoll','Resources','election_data.csv')
textpath = os.path.join(os.path.expanduser('~'),'Documents','GitHub', 'Python_Challenge','PyPoll','Analysis','Analysis.txt')
#create text file
f = open(textpath, "w")
#Read file to work with data
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #Start variables
    rowcount = 0
    charles = 0
    diana = 0
    raymon = 0
    #Skip headers
    next(csvreader)
    #Starting the loop through the rows
    for row in csvreader:
        #Total votes
        rowcount += 1
        #Count votes for diana
        if row[2] == "Diana DeGette":
            diana += 1
        #Count votes for charles
        if row[2] == "Charles Casper Stockham":
            charles += 1
        #Count votes for raymon
        if row[2] == "Raymon Anthony Doane":
            raymon += 1
        #Format values
        charlesp = '{:.3f}%'.format((charles/rowcount)*100)
        dianap = '{:.3f}%'.format((diana/rowcount)*100)
        raymonp = '{:.3f}%'.format((raymon/rowcount)*100)
        charlesv = '{:,}'.format(charles)
        dianav = '{:,}'.format(diana)
        raymonv = '{:,}'.format(raymon)
        rowcountv = '{:,}'.format(rowcount)
        #List of votes for candidates
        Candidates = [diana, charles, raymon]
        #Max votes between the candidates
        maxvotes = max(Candidates)
        #Condition to determine the winner
        if maxvotes == diana:
            winner = "Diana DeGette"
        elif maxvotes == charles:
            winner = "Charles Casper Stockham"
        elif maxvotes == raymon:
            winner = "Raymon Anthony Doane"

    print("Election results")
    print("--------------------------")
    print("Total votes:", rowcountv)
    print("--------------------------")
    print(f'Charles Casper Stockham: {charlesp} ({charlesv})')
    print(f'Diana DeGette: {dianap} ({dianav})')
    print(f'Raymon Anthony Doane: {raymonp} ({raymonv})')
    print("--------------------------")
    print(f'Winner: {winner}')
    print("--------------------------")

f.write("Election results")
f.write('\n')
f.write("--------------------------")
f.write('\n')
f.write(f'Total votes: {rowcountv}')
f.write('\n')
f.write("--------------------------")
f.write('\n')
f.write(f'Charles Casper Stockham: {charlesp} ({charlesv})')
f.write('\n')
f.write(f'Diana DeGette: {dianap} ({dianav})')
f.write('\n')
f.write(f'Raymon Anthony Doane: {raymonp} ({raymonv})')
f.write('\n')
f.write("--------------------------")
f.write('\n')
f.write(f'Winner: {winner}')
f.write('\n')
f.write("--------------------------")
