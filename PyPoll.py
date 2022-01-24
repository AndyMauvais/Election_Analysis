# Total number of votes cast
# List of candidates who received votes
# Total number of votes each candidate recevied
# Percentage of votes each candidate won
# The winner of the election based on popular vote.

import csv
import os

file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")


total_votes = 0
candidate_options = []
candidate_votes = {}

winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:
    # read file object with reader function
    file_reader = csv.reader(election_data)
    # read header row
    headers = next(file_reader)

    # Each row in the csv file
    for row in file_reader:
        # counts each row as a vote
        total_votes += 1

        candidate_name = row[2]
        # Adds candidate to the list of candidates if not already in list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

    #Save results to the text file
    with open(file_to_save, "w") as txt_file:
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n"
        )
        print(election_results, end="")
        txt_file.write(election_results)

        for candidate_name in candidate_votes:
            # candidate vote count
            votes = candidate_votes[candidate_name]
            # voter perctange
            vote_percentage = (float(votes) / float(total_votes)) * 100
            # print(f"{candidate_name}: received {vote_percentage: .1f}% of the votes")
            candidate_results = f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n"
            print(candidate_results)
            txt_file.write(candidate_results)

        # Determine if the votes are greater than the winning count.
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                winning_count = votes
                winning_percentage = vote_percentage
                winning_candidate = candidate_name
            
        winning_candidate_summary = (
        "\nWinning Candidate Summary \n"
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
        print(winning_candidate_summary)
        txt_file.write(winning_candidate_summary)

