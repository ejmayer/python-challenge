#This is main.py in PyPoll

import os
import csv

# may need to adjust path---------------------------------------
election_csv = os.path.join("election_data.csv")

Voter_ID = []
Candidate = []

# open and read the csv file
with open(election_csv, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        
        next(csvreader)
 
        for row in csvreader:

                # append Voter ID row
                Voter_ID.append(row[0])

                # append Candidate row
                Candidate.append(row[2])
                
                # find number of total votes cast
                total_votes = len(Voter_ID)

# find and create new list of candidates recieving votes
new_set = set(Candidate)
find_unique_candidates = list(new_set)

# retrieve names and create variables to move forward with
from operator import itemgetter
candidate_one, candidate_two, candidate_three, candidate_four = itemgetter(0,1,2,3)(find_unique_candidates)

 # find total number of Khan votes
votes_one = (Candidate.count(candidate_one))

# find total number of Correy votes
votes_two = (Candidate.count(candidate_two))

# find total number of Li votes
votes_three = (Candidate.count(candidate_three))

# find total number of O'Tooley votes
votes_four = (Candidate.count(candidate_four))

# find percentage of votes and properly format
Candidate_one_percent = '{:.3%}'.format(votes_one / total_votes)
Candidate_two_percent = '{:.3%}'.format(votes_two / total_votes)
Candidate_three_perent = '{:.3%}'.format(votes_three / total_votes)
Candidate_four_percent = '{:.3%}'.format(votes_four / total_votes)

# list of all candidates
Indiv_Candidates = [
                candidate_one,
                candidate_two,
                candidate_three,
                candidate_four]

# dictionaries of candidates - to be used to help print summary data
Dict_One = {
        "Name": candidate_one,        
        "Percentage": Candidate_one_percent,
        "Votes": votes_one}

Dict_two = {
        "Name": candidate_two,
        "Percentage": Candidate_two_percent,
        "Votes": votes_two}

Dict_three = {
        "Name": candidate_three,
        "Percentage": Candidate_three_perent,
        "Votes": votes_three}

Dict_four = {
        "Name": candidate_four,
        "Percentage": Candidate_four_percent,
        "Votes": votes_four}

# find largest vote-getter using dictionary and finding max item value and returning candidate
import operator
Winner_dict = {candidate_one : votes_one, candidate_two : votes_two, candidate_three : votes_three, candidate_four : votes_four}
winner = max(Winner_dict.items(), key=operator.itemgetter(1))[0]

# print results
print("")
print("------------------------------------------")
print("Election Results")
print("------------------------------------------")
print("Total votes: " + str(total_votes))
print("------------------------------------------")
#print(Kahn("Name")
print(Dict_One)
print(Dict_two)
print(Dict_three)
print(Dict_four)
print("------------------------------------------")
print("Winner: " + winner)
print("------------------------------------------")
print("")

# import using dictwriter in cvs module
import csv
csv_columns = ['Name', 'Percentage', 'Votes']
dict_data = [
        {"Name": candidate_one,        
        "Percentage": Candidate_one_percent,
        "Votes": votes_one},
        {"Name": candidate_two,
        "Percentage": Candidate_two_percent,
        "Votes": votes_two},
        {"Name": candidate_three,
        "Percentage": Candidate_three_perent,
        "Votes": votes_three},
        {"Name": candidate_four,
        "Percentage": Candidate_four_percent,
        "Votes": votes_four}]
csv_file = "election_results.csv"
try:
        with open(csv_file, 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
                writer.writeheader()
                for data in dict_data:
                        writer.writerow(data)

except IOError:
        print("I/O error")