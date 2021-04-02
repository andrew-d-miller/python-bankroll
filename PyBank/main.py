# HW 3 | Python Assignment - Py Me Up, Charlie (PyBank Script)

# Import Modules
Import os
Import csv

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
budgetdata_csv = os.path.join('..', 'Resources', 'budget_data.csv')

#
with open(budgetdata_csv, newline=' ') as budgetdata

    # Budget Reader splits data at the comma and reads the header line first 
    budgetreader = csv.reader(budgetdata, delimiter=',')
    header = next(budgetreader)
    row = next(budgetreader)

    # Calculate total months, net "P&L" and set variables
    total_months += 1
    net_total = int(row[1])
    greatest_increase = int(row[1])
    date_increase = int(row[1])


    for row in budgetreader:

        # Calculate the total number of months
        total_months += 1

        # Calculate net P&L
        net_total = int(row[1])
        


