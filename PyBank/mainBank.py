# import modules os and csv
import os
import csv

# set path to find the csv file
budget_data_csv = os.path.join('Resources', 'budget_data.csv')

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
    
    # Get information for the first row
    first_row = next(csvreader)

    #find the total number of months
    total_months += 1

    #find the net total of profit/loss
    net_total += int(first_row[1])

    #add the profit in the first row to the count
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
    
# calculate the amount of greatest increase in profits and find the month it occured
greatest_increase = max(net_change_list)
greatest_index = net_change_list.index(greatest_increase)
greatest_month = month_of_change[greatest_index]

# calculate the amounnt of greatest decrease in profits and find the month if occured
greatest_decrease = min(net_change_list)
least_index = net_change_list.index(greatest_decrease)
least_month = month_of_change[least_index]

# Calculate avergae monthly net change
monthly_avg_net_change = sum(net_change_list)/len(net_change_list)

# print the financial analysis
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(net_total)}")
print(f"Average Change: ${str(round(monthly_avg_net_change,2))}")
print(f"Greatest Increase in Profits : {greatest_month} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {least_month} (${str(greatest_decrease)})")

# establish path for output file

# write the output file
with open("Financial_Analysis.txt", "w") as file:

    file.write("Financial Analysis")
    file.write("\n")
    file.write("-----------------------------")
    file.write("\n")
    file.write(f"Total Months: {str(total_months)}")
    file.write("\n")
    file.write(f"Total: ${str(net_total)}")
    file.write("\n")
    file.write(f"Average Change: ${str(round(monthly_avg_net_change,2))}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits : {greatest_month} (${str(greatest_increase)})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {least_month} (${str(greatest_decrease)})")

