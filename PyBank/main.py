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


# lists in dictionary
#Date_Dictionary = Date
#Monthly_Profits_Losses = Profits_Losses
#Monthly_Change = 1   # temp filler for list





# calculate total months
Total_Months = len(Date)

# change variable for Profits from string to int
Total_Profit = int(Profits_Losses)

Monthly_Change = [int(List_Profit_Loss[i + 1]) - int(List_Profit_Loss[i]) for i in range(len(List_Profit_Loss)-1)]

print(Monthly_Change)

average_change = '${:,.2f}'.format(sum(Monthly_Change)/(Total_Months - 1))

print(average_change)


# zip months and monthly change into one dictionary
Budget_dict = dict(zip(Date, Monthly_Change))
print(Budget_dict)
#import operator

# create dictionary to help determine monthly change in new column
#List_Budget_Data = {Date : Monthly_Change}
#Greatest_increase = max(Budget_dict.values(), key=operator.itemgetter(1))[0]

Greatest_increase = max(Budget_dict.items(), key = lambda x: x[0])


#Greatest_increase = max(dict.items(), key=operator.itemgetter(1))[0]

print(Greatest_increase)


# find greatest increase 


# find greatest decrease




#print(Profits_Losses)

# print out data --------------------Need to find months still
print("")
print("Financial Analysis-----------------------------------------")
print("")
print("         Total Number of Months: " + str(Total_Months))
print("         Total Profits: $" + str(Total_Profit))
print("         Average Change: " + str(average_change))
print("         Greatest Increase in Profits: "               )
print("         Greatest Decrease in Profits: "              )
print("")
print("")

#print(List_Budget_Data)

# variable for the new output file
#requested_data = os.path.join("new_data.csv")

# open the output file
#with open(requested_data, "w", newline="") as datafile:
        #writer = csv.writer(datafile)
                
        # write the csv file header
        #csvwriter.writerow(["Total Months", "Total Profits", 'Greatest Increase", "Greatest Decrease"])

        # imput data into csvfile
        #csvwriter.writerow([Total_Months, Total_Months, MaxProfit, MinProfit])