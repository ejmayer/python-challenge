#This is main.py in PyBank

import os
import csv

# set path for csv file
Budget = os.path.join("Budget_Data.csv")

# set lists to be used
Date = []
Monthly_Profits_Losses = []
Monthly_Change = []
List_Profit_Loss = []

# open the csv file
with open(Budget, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")

        # skip header in csv file-----------------------------
        csv_header = next(csvreader)

        # set list to 0
        Profits_Losses = 0

        for row in csvreader:
        
                # add months to list
                Date.append(row[0])

                # add profits & losses to list
                Profits_Losses += int(row[1])

                # accumulate list of monthly profits/losses
                List_Profit_Loss.append(row[1])

                

               # Monthly_difference = (x+1)-x

# create dictionary to help determine monthly change in new column
List_Budget_Data = {"Date",
                "Monthly_Profits_Losses",
                "Monthly_Change"}

# lists in dictionary
Date_Dictionary = Date

Monthly_Profits_Losses = Profits_Losses

Monthly_Change = 1   # temp filler for list


# calculate total months
Total_Months = len(Date)

# change variable for Profits from string to int
Total_Profit = int(Profits_Losses)

# calculate average profits per month


# find greatest increase 


# find greatest decrease




#print(Profits_Losses)

# print out data --------------------Need to find months still
print("")
print("Financial Analysis-----------------------------------------")
print("")
print("         Total Number of Months: " + str(Total_Months))
print("         Total Profits: $" + str(Total_Profit))
print("         Average Change: "                   )
print("         Greatest Increase in Profits: "               )
print("         Greatest Decrease in Profits: "              )
print("")
print("")

print(List_Budget_Data)

# variable for the new output file
#requested_data = os.path.join("new_data.csv")

# open the output file
#with open(requested_data, "w", newline="") as datafile:
        #writer = csv.writer(datafile)
                
        # write the csv file header
        #csvwriter.writerow(["Total Months", "Total Profits", 'Greatest Increase", "Greatest Decrease"])

        # imput data into csvfile
        #csvwriter.writerow([Total_Months, Total_Months, MaxProfit, MinProfit])