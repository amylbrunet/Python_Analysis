# import libraries
import os
import csv

# set path to find the csv file
election_data_csv = os.path.join('Resources', 'election_data.csv')

# set variables
total_votes = 0
khan = 0
correy = 0
li = 0
otooley = 0

# open the csv file
with open(election_data_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # skip header row
    header = next(csvreader)

    #for loop to iterate through each row in csv to count votes for each candidate
    for row in csvreader:

        # find total number of votes
        total_votes += 1

        #if candidate name is found in row[2], add to total votes for that candidate
        if row[2] == "Khan":
            khan += 1
        elif row[2] == "Correy":
            correy += 1
        elif row[2] == "Li":
            li += 1
        elif row[2] == "O'Tooley":
            otooley += 1

# calculate vote percentage for each candidate 
khan_vote_percent = round((khan/total_votes) * 100)
correy_vote_percent = round((correy/total_votes) * 100)
li_vote_percent = round((li/total_votes) * 100)
otooley_vote_percent = round((otooley/total_votes) * 100)

# create two lists to find winner of election using candidate names and vote totals
candidates = ["Khan", "Correy", "Li", "O'Tooley"]
votes = [khan, correy, li, otooley]

# zip the lists and use max to find winner
candidates_votes = dict(zip(candidates,votes))
winner = max(candidates_votes, key=candidates_votes.get)

# print the election results
print(f"Election Results")
print(f"-----------------------------")
print(f"Total Votes: {total_votes}")
print(f"-----------------------------")
print(f"Khan: {khan_vote_percent}.000% ({khan})")
print(f"Correy: {correy_vote_percent}.000% ({correy})")
print(f"Li: {li_vote_percent}.000% ({li})")
print(f"O'Tooley: {otooley_vote_percent}.000% ({otooley})")
print(f"-----------------------------")
print(f"Winner: {winner}")
print(f"-----------------------------")

# write the output file
with open("Election_Results.txt", "w") as file:
    
    file.write(f"Election Results")
    file.write("\n")
    file.write(f"-----------------------------")
    file.write("\n")
    file.write(f"Total Votes: {total_votes}")
    file.write("\n")
    file.write(f"-----------------------------")
    file.write("\n")
    file.write(f"Khan: {khan_vote_percent}.000% ({khan})")
    file.write("\n")
    file.write(f"Correy: {correy_vote_percent}.000% ({correy})")
    file.write("\n")
    file.write(f"Li: {li_vote_percent}.000% ({li})")
    file.write("\n")
    file.write(f"O'Tooley: {otooley_vote_percent}.000% ({otooley})")
    file.write("\n")
    file.write(f"-----------------------------")
    file.write("\n")
    file.write(f"Winner: {winner}")
    file.write("\n")
    file.write(f"-----------------------------")

