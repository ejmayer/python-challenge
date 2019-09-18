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
                Date.append(row[0])

                # add profits & losses to list
                Profits_Losses.append(row[1])

                # calculate total months
                Total_Months = len(row[1])

                # change variable for Profits from string to int
                Monthly_Profit = int(Profits_Losses)
                
                # calcutlate total profits & losses
                Total_Profits = sum(Monthly_Profit)

                # calculate average profits per month
                Average = Total_Profits / Total_Months

                # find greatest increase 
                MaxProfit = max(Monthly_Profit)

                # find greatest decrease
                MinProfit = min(Monthly_Profit)

                # print out data --------------------Need to find months still
                print("Financial Analysis-----------------------------------------")
                print("Total Number of Months: "+ Total_Months)
                print("Total Profits: " + Total_Profits)
                print("Average Change: " + Average)
                print("Greatest Increase in Profits: " + MaxProfit)
                print("Greatest Decrease in Profits: " + MinProfit)

        # variable for the new output file
        requested_data = os.path.join("new_data.csv")

        # open the output file
        with open(requested_data, "w", newline="") as datafile:
                writer = csv.writer(datafile)
                
                # write the csv file header
                csvwriter.writerow(["Total Months", "Total Profits", 'Greatest Increase", "Greatest Decrease"])

                # imput data into csvfile
                csvwriter.writerow([Total_Months, Total_Months, MaxProfit, MinProfit])

