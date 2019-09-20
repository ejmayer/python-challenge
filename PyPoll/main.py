#This is main.py in PyPoll

import os
import csv

# may need to adjust path---------------------------------------
Election_csv = os.path.join("Election_Data.csv")

Voter_ID = []
Candidate = []
Indiv_Candidates =[]


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
OTooley_Votes = (Candidate.count("O'Tooley"))




print(Li_Votes)
print(Correy_Votes)
print(OTooley_Votes)
print(Khan_Votes)
print(total_votes)

khan_percent = '{:.3%}'.format(Khan_Votes / total_votes)
li_percent = '{:.3%}'.format(Li_Votes / total_votes)
correy_perent ='{:.3%}'.format (Correy_Votes / total_votes)
otooley_percent = '{:.3%}'.format(OTooley_Votes / total_votes)


print("------------------------------------------")
print("Election Results")
print("------------------------------------------")
#print("Total votes: " + str(total_votes))
print("------------------------------------------")
#print("Khan: " + str(khan_percent)
#print(li_percent)
#print(correy_perent)
#print(otooley_percent)

#print("Correy: " + float(Correy_Votes/total_votes) + "(" + Correy_Votes = ")") 
#print("Li: " + float(Li_Votes/total_votes) + "(" + Li_Votes = ")") 
# print("O'Tooley: " + float(OTooley_Votes/total_votes) + "(" + OTooley_Votes = ")")
#print("Winner:" + str(Winner)

