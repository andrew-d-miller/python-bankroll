# HW 3 | Python Assignment - Py Me Up, Charlie (PyPoll Script)

# Import Modules
import os
import csv

# Defining Variables
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0


csvpath = os.path.join('Resources', 'election_data.csv')
output_file = os.path.join('Resources', 'election_data_revised.txt')



with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')


    row = next(csvreader)


    for row in csvreader:


        total_votes += 1

        # Counting candidate votes
        if (row[0] == "Khan"):
            khan_votes += 1
        elif (row[0] == "Correy"):
            correy_votes += 1
        elif (row[0] == "Li"):
            li_votes += 1
        else :
            otooley_votes += 1










# Print PyPoll Analysis
print(f"Election Results")
print(f"--------------------------------------")
print(f"Total Votes: {total_votes}")
print(f"--------------------------------------")
print(f"Khan: {khan_votes}")
print(f"Correy: {correy_votes}")
print(f"Li: {li_votes}")
print(f"O'Tooley: {otooley_votes}")
print(f"--------------------------------------")
print(f"Winner: ")
print(f"--------------------------------------")
