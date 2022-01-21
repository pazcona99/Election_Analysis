#The data we need to retrieve
import csv
import os
#Assign a variable for the file load and the path
file_to_load = os.path.join("Resources", "election_results.csv")
#Creat a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1 Initialize a total vote counter
total_votes = 0

#Initialize new list for candidate votes
candidate_options = []

#Declare empty dictionary for candidate votes
candidate_votes = {}

#Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file.
with open(file_to_load) as election_data:

    #To do: perform analysis
    file_read = csv.reader(election_data)

    #Print the header row
    headers = next(file_read)

    #Print each row in the CSV file
    for row in file_read:
        #2  Add to the total vote count
        total_votes += 1
        #Print the candidate name from each row
        candidate_name = row[2]
        #If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
           
            #Add it to the list of candidates
            candidate_options.append(candidate_name)

            #Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

        #Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

#Save the results to our text file
with open(file_to_save, "w") as txt_file:
    #Print the final vote count to the terminal
    election_results = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(election_results, end="")
    #Save the final vote count to the text file
    txt_file.write(election_results)
        
    #3 Print the total votes
    #print(total_votes) 

    #A complete list of candidates who received votes
    #print(candidate_options)

    #Total number of votes each candidate received
    #print(candidate_votes)

    #Percentage of votes each candidate won
        #Iterate through the candidate list
    for candidate_name in candidate_votes:
        #Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        #Calculate the percentage of votes
        vote_percentage = (float(votes) / float(total_votes)) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
            
    #The winner of the election based on popular vote
    #Determine winning vote count and candidate
            # 1. Determine if the votes are greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #if true then set the winning_count = votes and winning_percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            #And, set the winning candidate equal to the candidates name
            winning_candidate = candidate_name

        # To do: print out the winning candidate, vote count and percentage to
    #   terminal.
        #print(f"{candidate_name} : {vote_percentage:.1f}% ({votes:,})\n")

    #Print winning candidates results
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
        
    print(winning_candidate_summary)

    #Save the winning candidates results to the text file
    txt_file.write(winning_candidate_summary)
