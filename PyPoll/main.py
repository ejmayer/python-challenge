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

        votes = 0

        for row in csvreader:

                # add to candidate list
                Candidate.append(row[2])

               
                # add all candidates who recieved votes
                def unique(Candidate):
                        Candidate_List = Candidate
                        print(Candidate_List)

    

        # accumalate each candidates vote counts
        # Candidate_Votes = Candidate_Votes.total


        print(Candidate List)
        


        print("------------------------------------------")
        print("Election Results")
        print("------------------------------------------")
        print("Total votes: " + "Candidate_Votes.sum()")
        print("------------------------------------------")
                

