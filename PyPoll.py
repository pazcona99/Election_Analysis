#The data we need to retrieve
import csv
import os
#Assign a variable for the file load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
#Creat a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Open the election results and read the file.
with open(file_to_load) as election_data:

    #To do: perform analysis
    file_read = csv.reader(election_data)

    #Print the header row
    headers = next(file_read)
    print(headers)




#Total number of votes cast
#A complete list of candidates who received votes
#Total number of votes each candidate received
#Percentage of votes each candidate won
#The winner of the election based on popular vote