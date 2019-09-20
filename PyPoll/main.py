#This is main.py in PyPoll

import os
import csv

# may need to adjust path---------------------------------------
Election_csv = os.path.join("Election_Data.csv")

Voter_ID = []
Candidate = []

#Khan = []
#Correy = []
#Li = []
#OTooley = []

# open and read the csv file
with open(Election_csv, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        
        next(csvreader)
 
        for row in csvreader:

                # append Voter ID row
                Voter_ID.append(row[0])

                # append Candidate row
                Candidate.append(row[2])
                
                # find number of total votes cast
                total_votes = len(Voter_ID)

# find total number of Khan votes
Khan_Votes = (Candidate.count("Khan"))

# find total number of Correy votes
Correy_Votes = (Candidate.count("Correy"))

# find total number of Li votes
Li_Votes = (Candidate.count("Li"))

# find total number of O'Tooley votes
OTooley_Votes = (Candidate.count("O'Tooley")

#Khan_percent = (Khan_Votes / total_votes)
#Li_percent = (Li_Votes / total_votes)
#Correy_perent = (Correy_Votes / total_votes)
#OTooley_percent = (OTooley_Votes / total_votes)
# -----------code for formatting percentage ------ add in later  ----'{:.3%}'.format

#khan_test = 4
#li_test = 5
#Correy_test = 6
#OTooley_test = 7


# List of all candidates
#Indiv_Candidates = ["Khan", 
#                "Li",
#                "Correy",
#                "OTooley"]



# Dictionaries of candidates ----- to be used to help print data in summary table
#Khan = {
#        "Name": "Khan",
#        "votes": Khan_Votes,
#        "Percentage": Khan_Votes}

#Li = {
#        "Name": "Li",
#        "Votes": Li_Votes,
#        "Percentage": Li_Votes}

#Correy = {
#        "Name": "Correy",
#        "Votes": Correy_Votes,
#        "Percentage": Correy_Votes}


#OTooley =  {
#        "Name": "O'Tooley",
#        "Votes": OTooley_Votes,
#        #"Percentage": OTooley_Votes}

# test points
#print(Li)
#print(Correy)
#print(OTooley)
#print(Khan)

print(total_votes)

print("------------------------------------------")
print("Election Results")
print("------------------------------------------")
#print("Total votes: " + str(total_votes))
print("------------------------------------------")
#print("Khan: " + str(khan_percent)




#print("Winner:" +           )

