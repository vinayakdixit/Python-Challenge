# Required Output
#   """ Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)
#    ----------------"""

# First open ad read the file from the location
# set the file path
import os
import csv
csvpath = os.path.join("Resources","budget_data.csv")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader)
# """ with open(csvpath, newline="") as csvfile:
#     csvreader = csv.reader(csvfile, delimiter=",") """

# create a loop to go through all the rows and pring total number of rows
    totalrows =0
    # for row in csvreader:
    #     totalrows.append(row)
    #totalrows = [row for row in csvreader]
    #print(f'Total Months: {len(totalrows)-1}')

    list_gain =[]
    currentelement = 0
    list_delta=[]
    list_month=[]


    for row in csvreader:
        totalrows += 1
        list_gain.append(float(row[1]))
        list_month.append(str(row[0]))
        
    totalgain = sum(list_gain)
    # for i in range(len(list_gain)):
    #     if i < len(list_gain):
    #         currentelement = list_gain[i]
    #         nextelement = list_gain[i+1]
    #         delta = currentelement - nextelement
    #         list_delta.append(delta)

    print (f'Total Monnths = {totalrows}')
    print(f'Total Profit/(Loss) = {totalgain}')
    # print (list_delta)
for x in range(len(list_gain)):
    if x < len(list_gain)-1:
        #print(list_gain[x])
        currentelement = list_gain[x]
        nextelement = list_gain[x+1]
        delta = nextelement - currentelement
        list_delta.append(delta)

maxgain = max(list_delta)
# print(maxgain)
delta_month=list_month.pop(0)
# for y in range (len(delta_month)):
#     print(delta_month[y])
#print(list_month)

maxgainindex = list_delta.index(max(list_delta))
# print(maxgainindex)
print(f'Greatest increase in profits: {list_month[maxgainindex]}  {maxgain}')

# Alternative Methos
print("Alternative Method")
answerkey=[]
answerkey = [(list_month[i], list_delta[i]) for i in range (0,len(list_month))]
# print(answerkey)
print(answerkey[maxgainindex])

