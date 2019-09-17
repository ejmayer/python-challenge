#This is main.py in PyPoll

import os
import csv

# may need to adjust path---------------------------------------
Election = os.path.join("Election_Data.csv")

Voter_ID = []
County = []
Candidate = []

# open the csv file
with open(Election, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")

# skip header in csv file-----------------------------
csv_header = next(csvreader)

for row in csvreader:
    # compile all Voter id's
    Voter_ID.append(row[0])

    # compile all counties
    County.append(row[1])

    # compile all candidates
    Candidate.append(row[2])

    # add all candidates who recieved votes
    CandidateList = Candidate.unique()

    # accumalate each candidates vote counts
    CandidateVotes = CandidateList.value_counts()

    





    print("------------------------------------------")
    print("Election Results")
    print("------------------------------------------")
    print("Total votes: " + TotalVotes)
    print("------------------------------------------")
    print("")

