# Election Results
import os
import csv

CSV_PATH = os.path.join("Resources", "election_data.csv")
OUTPUT_PATH = os.path.join("analysis", "analysis.txt")

# Total Vote Count

vote_count = 0
candidate_votes = {}
total_votes= 0
print(__file__)

os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open (CSV_PATH) as election_data:
    csv_reader = csv.reader(election_data)
    next(csv_reader) #skipped the header row
    for row in csv_reader:
        vote_count += 1

        # The List of Candidates
        total_votes += 1
        candidate_name = row[2]
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] += 1
        else:
            candidate_votes[candidate_name] = 1

percentage_votes = {candidate:(votes/total_votes * 100) for candidate, votes in candidate_votes.items()}

# The Winner

winner = max(candidate_votes, key=candidate_votes.get)

#Text Output
results = []
results.append("Total Votes: " + str(vote_count))  # Added vote count
results.append("Election Results")
results.append("-------------------------")
results.append(f"Total Votes: {total_votes}")
results.append("-------------------------")
for candidate, votes in candidate_votes.items():
    percentage = percentage_votes[candidate]
    results.append(f"{candidate}: {percentage:.3f}% ({votes})")
results.append("-------------------------")
results.append(f"Winner: {winner}")
results.append("-------------------------")



with open(OUTPUT_PATH, "w") as output_file:
    output_file.write('\n'.join(results))

# Print the results
print("Total Votes:", vote_count)
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