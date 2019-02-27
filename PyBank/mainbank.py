

import os
import csv

BankCsvPath = os.path.join("budget_data.csv")


date = []
ProfitLoss = []

with open(BankCsvPath, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    for row in csv_reader:
       months.append(row[0])
       ''' gainloss = sum(gainloss)
        print(row)
      for col in gainloss
            total += int(col)
        print total'''

