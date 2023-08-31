# Election Results
import os
import csv

csv_file = "Module-3-Challenge---Python\\PyPoll\\Resources\\election_data.csv"

# Vote count code
vote_count = 0
with open (csv_file) as election_data:
    csv_reader = csv.reader(election_data, delimiter=',')
    for vote in csv_reader:
        vote_count += 1

print("Total Votes:", vote_count)

# List of candidates

candidate_votes = {}
total_votes= 0
with open (csv_file) as election_data:
    csv_reader = csv.reader(election_data, delimiter=',')
    next(csv_reader) #skipped the header row
    for row in csv_reader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] += 1
        else:
            candidate_votes[candidate_name] = 1

percentage_votes = {candidate:(votes/total_votes * 100) for candidate, votes in candidate_votes.items()}

winner = max(candidate_votes, key=candidate_votes.get)

# Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidate_votes.items():
    percentage = percentage_votes[candidate]
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")