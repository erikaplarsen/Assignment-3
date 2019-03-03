

import os
import csv
import numpy

BankCsvPath = os.path.join("desktop", "Assignment-3", "PyBank", "budget_data.csv")

months = 0
ProfitLoss = 0
previous = 0 
change = 0
ChangeList = []
AverageChange = 0

with open(BankCsvPath, newline="") as csvfile:
  csv_reader = csv.reader(csvfile, delimiter=",")
  csv_header = next(csvfile)

  for row in csv_reader:
  
    ProfitLoss += int(row[1])
    months += 1

    change = float(row[1]) - previous
    previous = float(int(row[1]))
    ChangeList = ChangeList + [change]
    
  
  
  AverageChange = (sum(ChangeList))/(len(ChangeList))


print (f"Total revenue over {months} months = {ProfitLoss}")
print (f"Average change = {AverageChange}")
