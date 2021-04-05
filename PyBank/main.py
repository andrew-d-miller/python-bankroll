# HW 3 | Python Assignment - Py Me Up, Charlie (PyBank Script)

# Import Modules
import os
import csv

# Defining Variables
total_months = 0
net_total = 0
month_count = []
monthly_change = []
greatest_increase = 0
date_increase = 0
greatest_decrease = 0
date_decrease = 0

# Path to the budget data from the resources folder
csvpath = os.path.join('Resources', 'budget_data.csv')

# Open the CSV file
with open(csvpath) as csvfile:

    # CSV Reader splits data at the comma and reads the header first 
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first (skip if no header)
    header = next(csvreader)
    row = next(csvreader)

    # Calculate total months, net "P&L" and set variables
    prev_row = int(row[1])
    total_months += 1
    net_total += int(row[1])
    greatest_increase = int(row[1])
    date_increase = int(row[1])
    

    # Read data after the header
    for row in csvreader:

        # Calculate the total number of months
        total_months += 1

        # Calculate net P&L over entire period
        net_total += int(row[1])

        # Calculate Monthly Change from Current to Previous Month
        rev_change = int(row[1]) - prev_row
        monthly_change.append(rev_change)
        prev_row = int(row[1])
        month_count.append(row[0])

        # Calculate Greatest Increase
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            date_increase = row[0]

        # Calculate Greatest Decrease
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            date_decrease = row[0]

    # Calculate Average and Date
    avg_change = sum(monthly_change)/ len(monthly_change)

    high = max(monthly_change)
    low = min(monthly_change)
    

# Print PyBank Analysis
print(f"Financial Analysis")
print(f"------------------------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${avg_change}")
print(f"Greatest Increase in Profits:, {date_increase}")
print(f"Greatest Decrease in Profits:, {date_decrease}")


output_file = os.path.join('Resources', 'budget_data_revised.txt')

with open(output_file, 'w',) as textfile:
    textfile.write(f"Financial Analysis\n")
    textfile.write(f"---------------------------------\n")
    textfile.write(f"Total Months: {total_months}\n")
    textfile.write(f"Total: {net_total}\n")
    textfile.write(f"Average Change: ${avg_change}\n")
    textfile.write(f"Greatest Increase in Profits:, {date_increase}\n")
    textfile.write(f"Greatest Decrease in Profits:, {date_decrease}\n")
