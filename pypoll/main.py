import os
import csv

# Set the path to the input file
file_path = "C:/Users/ismae/Desktop/Dataclass excel, HW/HW/HW3/pypoll/Resources/election_data.csv"


# Initialize variables
total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

# Read the CSV file
with open(file_path, 'r') as file:
    csvreader = csv.reader(file, delimiter=',')
    
    # Skip the header row
    header = next(csvreader)
    
    # Iterate through each row in the CSV file
    for row in csvreader:
        # Increment the total number of votes
        total_votes += 1
        
        # Get the candidate name for the current row
        candidate = row[2]
        
        # Add the candidate to the dictionary of candidates
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# Format the results
output = "Election Results\n"
output += "-------------------------\n"
output += f"Total Votes: {total_votes}\n"
output += "-------------------------\n"

# Calculate and display the percentage of votes for each candidate
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    output += f"{candidate}: {percentage:.3f}% ({votes})\n"
    
    # Check if the current candidate has more votes than the previous winner
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

output += "-------------------------\n"
output += f"Winner: {winner}\n"
output += "-------------------------\n"

# Print the analysis to the terminal
print(output)

# Set the path to the output file
output_file_path = "election_results.txt"

# Export the results to a text file
with open(output_file_path, 'w') as file:
    file.write(output)

print(f"The analysis has been exported to {output_file_path}.")
