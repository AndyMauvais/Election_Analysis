# Total number of votes cast
# List of candidates who received votes
# Total number of votes each candidate recevied
# Percentage of votes each candidate won
# The winner of the election based on popular vote.

import csv
import os

file_to_load = os.path.join("Resources","election_results.csv")
file_to_save = os.path.join("analysis", "election_analysis.txt")
# election_data = open(path,"r")
# election_data.close()
with open(file_to_load) as election_data:
    #read file object with reader function
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    # data = next(file_reader)
    print(headers)
    # # print(data)
    # for i in range(5) :
    #     print(next(file_reader))