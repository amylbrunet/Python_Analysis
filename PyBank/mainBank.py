# import modules os and csv
import os
import csv

# set path to find the csv file
budget_data_csv = os.path.join('Resources', 'budget_data.csv')
# budget_data_csv = "Resources/budget_data.csv"

# Vaariables for the analysis
total_months = 0
net_total = 0
net_change_list = []
month_of_change = []
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999999999999]

# open the csv file
with open(budget_data_csv) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    # skip header row
    header = next(csvreader)
    # print(header[0])
    # Get information for the first row
    first_row = next(csvreader)
    total_months += 1
    net_total += int(first_row[1])
    net_prev = int(first_row[1])


# loop through csv to add the total number of months and net total profit/loss
    for row in csvreader:
        # get total months
        total_months += 1

        # get net total/total profit
        net_total += int(row[1])

        # Net Change
        net_change = int(row[1]) - net_prev
        net_prev = int(row[1])
        net_change_list += [net_change]
        month_of_change += [row[0]]
    
# calculate total number of months to find averages

# calculate total net amount of profit/loss to find averages

# calculate average change in profit/loss per month

# calculate the amount of greatest increase in profits
    if net_change > greatest_increase[1]:
        greatest_increase[0] = row[0]
        greatest_increase[1] = net_change

# find the date of the greatest increase in profits??

# calculate the amounnt of greatest decrease in profits
    if net_change < greatest_decrease[1]:
        greatest_decrease[0] = row[0]
        greatest_decrease[1] = net_change

monthly_avg_net_change = sum(net_change_list)/len(net_change_list)
print("Net Monthly avg change: " , monthly_avg_net_change)
print("Total months: ", total_months)
print(f"Greatest increase : {greatest_increase[0]} greatest increase of {greatest_increase[1]}")
# find the date of the greatest decrease in profits??

# printing the financial analysis??

# creating a text file out for analysis??

