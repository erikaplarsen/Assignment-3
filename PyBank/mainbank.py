

import os
import csv


BankCsvPath = os.path.join("desktop", "Assignment-3", "PyBank", "budget_data.csv")

Months = 0
ProfitLoss = 0
ChangeList = []
MonthlyChange=[]
AverageChange = 0



with open(BankCsvPath, newline="") as csvfile:
  csv_reader = csv.reader(csvfile, delimiter=",")
  csv_header = next(csvfile)

  for row in csv_reader:
  
    ProfitLoss += int(row[1])
    Months += 1

    ChangeList.append(int(row[1]))
    
  for i in range(len(ChangeList)-1):
    MonthlyChange.append(ChangeList[i+1]-ChangeList[i])
  
GreatestIncrease = max(MonthlyChange)
GreatestDecrease = min(MonthlyChange)
 
AverageChange = (sum(MonthlyChange))/(len(MonthlyChange))



print ("FINANCIAL ANALYSIS")
print (f"Total revenue over {Months} months = {ProfitLoss}")
print (f"Average change = {AverageChange}")
print(f"Greatest increase in profits = {GreatestIncrease}")
print(f"Greatest decrease in profits = {GreatestDecrease}")

file = open('bankpy.txt',"w")

file.write ("FINANCIAL ANALYSIS")
file.write (f"Total revenue over {Months} months = {ProfitLoss}")
file.write (f"Average change = {AverageChange}")
file.write (f"Greatest increase in profits = {GreatestIncrease}")
file.write (f"Greatest decrease in profits = {GreatestDecrease}")
file.close()