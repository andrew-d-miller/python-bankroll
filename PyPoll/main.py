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
output_file = os.path.join('Analysis', 'election_data_revised.txt')



with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')


    row = next(csvreader)


    for row in csvreader:

        # Total number of votes casted
        total_votes += 1

        # Counting the total number of votes casted for each candidate
        if (row[2] == "Khan"):
            khan_votes += 1
        elif (row[2] == "Correy"):
            correy_votes += 1
        elif (row[2] == "Li"):
            li_votes += 1
        else :
            otooley_votes += 1


        # Percentage of votes for each candidate
        khan_percentage = (khan_votes/total_votes) * 100
        correy_percentage = (correy_votes/total_votes) * 100
        li_percentage = (li_votes/total_votes) * 100
        otooley_percentage = (otooley_votes/total_votes) * 100

        # Declaring the winner based on who has the most votes
        winner = max(khan_votes, correy_votes, li_votes, otooley_votes)

        if winner == khan_votes:
            winner_name = "Khan"
        elif winner == correy_votes:
            winner_name = "Correy"
        elif winner == li_votes:
            winner_name = "Li"
        else :
            winner_name = "O'Tolley"         



# Print PyPoll Analysis
print(f"Election Results")
print(f"---------------------------------")
print(f"Total Votes: {total_votes}")
print(f"---------------------------------")
print(f"Khan: {khan_percentage:.3f}% ({khan_votes})")
print(f"Correy: {correy_percentage:.3f}% ({correy_votes})")
print(f"Li: {li_percentage:.3f}% ({li_votes})")
print(f"O'Tooley: {otooley_percentage:.3f}% ({otooley_votes})")
print(f"---------------------------------")
print(f"Winner: {winner_name}")
print(f"---------------------------------")


with open(output_file, "a") as txt_file:
    txt_file.write(f"Election Results\n")
    txt_file.write(f"---------------------------------\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write(f"---------------------------------\n")
    txt_file.write(f"Khan: {khan_percentage:.3f}% ({khan_votes})\n")
    txt_file.write(f"Correy: {correy_percentage:.3f}% ({correy_votes})\n")
    txt_file.write(f"Li: {li_percentage:.3f}% ({li_votes})\n")
    txt_file.write(f"O'Tooley: {otooley_percentage:.3f}% ({otooley_votes})\n")
    txt_file.write(f"---------------------------------\n")
    txt_file.write(f"Winner: {winner_name}\n")
    txt_file.write(f"---------------------------------\n")
