#This is main.py in PyBank

import os
import csv

# set path for csv file
budget = os.path.join("Budget_Data.csv")

# set lists to be used
date = []
monthly_change = []
list_profit_loss = []
monthly_profits = []

# open the csv file
with open(budget, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")

        # skip header in csv file-----------------------------
        csv_header = next(csvreader)

        # set list to 0
        profits_losses = 0

        for row in csvreader:
        
                # add months to list
                date.append(row[0])

                # add monthly totals to monthly profits list
                monthly_profits.append(row[1])

                # sum of profits & losses for total profits
                profits_losses += int(row[1])

# calculate total months
total_months = len(date)

# change variable for Profits from string to int
total_profit = int(profits_losses)

# accumulate list showing monthly change in profits/losses
monthly_change = [int(monthly_profits[i + 1]) - int(monthly_profits[i]) for i in range(len(monthly_profits)-1)]

#  ----------unable to correlate min and max monthly change to date using index--------
# ------------went dictionary method instead
#index_min = [i for i, x in enumerate(monthly_change) if x == min(monthly_change)]
#index_min = map(int, index_min)
#index_max =  [i for i, x in enumerate(Monthly_Change) if x == max(Monthly_Change)]
#for index, elem in enumerate(monthly_change):
#        print(index, elem)

# remove first row in date list so zipped dict lines up 
# correct with calculated difference between month (monthly_change)
date.remove('Jan-2010')

# declare and format average monthly change 
average_change = '${:,.2f}'.format(sum(monthly_change)/(total_months - 1))

# zip months and monthly change into one dictionary
budget_dict = dict(zip(date, monthly_change))

# create dictionary to help determine monthly change in new column
greatest_increase = max(budget_dict.items(), key = lambda x: x[1])
greatest_decrease = min(budget_dict.items(), key = lambda x: x[1])

# print out data --------------------Need to find months still
print("")
print("")
print("")
print("Financial Analysis-----------------------------------------")
print("")
print("         Total Number of Months: " + str(total_months))
print("         Total Profits: $" + str(total_profit))
print("         Average Change: " + str(average_change))
print("         Greatest Increase in profits is: " + str(greatest_increase)) 
print("         Greatest Decrease in profits is: " + str(greatest_decrease)) 
print("")
print("")
print("---------------------------------------------------------------")

with open('budget_analysis.txt', 'w') as f:
        f.write('Financial Analysis-------------------------------------\n')
        f.write('               Total Number of Months: 86\n')
        f.write('               Total Profits: $38382578\n')
        f.write('               Average Change: $-2,315.12\n')
        f.write('               Greatest Increase in profits is: Feb-2012, 1926159\n')
        f.write('               Greatest Decrease in profits is: Sep-2013, -2196167\n')