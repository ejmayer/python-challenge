#This is main.py in PyBank

import os
import csv

Budget_Data_path = os.path.join("Budget_Data.csv")


with open(Budget_Data_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    print(csvreader)

    csv_header = next(csvreader)

    for row in csvreader:
        print(row)
        

    date = int(row[1])
    profits_losses = int(row[2])


    print("Financial Analysis_____________________")

    months = 0

    for row in csv_reader
    months += date

    print("Total Number of Months: "+ months)

    Total_Profits += profits_losses

    print("Total Profits: " + Total_Profits)
    
    Average = Total_Profits / months

    print("Average Change: " + Average)

    MaxProfit, MinProfit = [],[]
    
    for row in csv_reader:
        MaxProfit.append

