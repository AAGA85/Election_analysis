#Add our dependencies
import csv
import os

# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources","election_results.csv")

# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize a total vote counter
total_votes=0
# Candidate Options
candidate_options=[]
# Declare a empty dictionary 
candidate_votes={}

#Winning Candidate, vote count and percentage tracker
winning_candidate=""
winning_count=0
winning_percentage=0


# Open the election results and read the file
with open(file_to_load) as election_data:
   #Read the file object with the reader function.
   file_reader= csv.reader(election_data)

   #Read  the header row
   headers= next(file_reader)

   #Print each row in the CSV file
   
   for row in file_reader:
      # Add to the total vote count.
      total_votes += 1

      # Print the candidate name form each row
      candidate_name=row[2]
      
      #If the candidate does not match any existing candidate...
      if candidate_name not in candidate_options:

         # Add the candidate name to the candidate list
          candidate_options.append(candidate_name)

          #Begin tracking that candidate's vote count
          candidate_votes[candidate_name] =0

      #Add a vote to that candidate's count
      candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save,"w") as txt_file:
   election_results=(  

      f'Election Results\n'
      f'-------------------------\n'
      f'Total Votes:{total_votes:,}\n'
      f'--------------------------\n')

   print(election_results,end="")

   #Save the final vote count to the text file 
   txt_file.write(election_results)
      
   #Determine the percentage of votes for each candidate by looping through the counts
   #Iterate through the candidate list
   for candidate_name in candidate_votes:
      # Retrive vote count of a candidate
       votes=candidate_votes[candidate_name]
      # Calculate the percentage of votes
       vote_percentage = float(votes)/float(total_votes)*100
      #Print the candidate name and percentage of votes
       candidate_results=(
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

      #Print each candidate's voter count and percentage to the terminal  
       print(candidate_results)

      #Save the candidate resultsto to our text file
       txt_file.write(candidate_results)

      #Determine winning vote count, winning percentage, and candidate
       if (votes> winning_count)and (vote_percentage>winning_percentage):
          winning_count=votes
          winning_candidate=candidate_name
          winning_percentage=vote_percentage
   #Print the winning candidates'results to the terminal
   winning_candidate_summary=(
      f"-------------------------\n"
      f'Winner:{winning_candidate}\n'
      f'Winning Vote Count: {winning_count:,}'
      f'Winning Percentage: {winning_percentage:.1f}%\n'
      f'--------------------------\n')

   print(winning_candidate_summary)

   #Save the winning candidate's results to the text file
   txt_file.write(winning_candidate_summary)

#3 Print the candidate list
#print(candidate_votes)


   





#Write some data to the file



#1. The total number of votes cast
#2. A complete list of cadidates who received votes
#3. The percentage of votes each candidate won
#4. Tht total number of votes each candidate won
#5. The winner of the election based on popular vote