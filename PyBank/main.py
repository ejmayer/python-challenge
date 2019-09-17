#This is main.py in PyBank

import os
import csv

# may need to adjust path---------------------------------------
Budget = os.path.join("Budget_Data.csv")

Date = []
Profits_Losses = []

# open the csv file
with open(Budget, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")

# skip header in csv file-----------------------------
csv_header = next(csvreader)

for row in csvreader:
        
        # add months to list
        Date.append(row[1])

        # add profits & losses to list
        Profits_Losses.append(row[2])

        # calculate total months
        TotalMonths = int(row[1]).sum()

        # calcutlate total profits & losses
        TotalProfit = int(row[2]).sum()

        # calculate average profits per month
        Average = TotalProfit / TotalMonths

        # find greatest increase 
        MaxProfit = max(TotalProfit)

        #find greatest decrease
        MinProfit = min(TotalProfit)

        print("Financial Analysis-----------------------------------------")
        print("Total Number of Months: "+ TotalMonths)
        print("Total Profits: " + TotalProfit)
        print("Average Change: " + Average)
        print("Greatest Increase in Profits: " + MaxProfit)
        print("Greatest Decrease in Profits: " + MinProfit)

# variable for the new output file
requested_data = os.path.join("new_data.csv")

# open the output file
with open(requested_data, "w", newline="") as datafile:
        writer = csv.writer(datafile)

        # how to write the new data in????????  (not a newly created list)

