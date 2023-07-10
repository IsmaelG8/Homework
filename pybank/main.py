import os 
import csv

# Set the path to the input file
# Set the path to the input file
# Set the path to the input file
file_path = "C:/Users/ismae/Desktop/Dataclass excel, HW/HW/HW3/pybank/Resources/budget_data.csv"



# Initialize variables
total_months = 0
total_profit_losses = 0
previous_profit_loss = 0
changes = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

# Read the CSV file
with open(file_path, 'r') as file:
    csvreader = csv.reader(file, delimiter=',')
    
    # Skip the header row
    header = next(csvreader)
    
    # Iterate through each row in the CSV file
    for row in csvreader:
        # Increment the total number of months
        total_months += 1
        
        # Get the profit/loss value for the current row
        profit_loss = int(row[1])
        
        # Calculate the net total amount of profit/losses
        total_profit_losses += profit_loss
        
        # Calculate the change in profit/loss since the previous month
        change = profit_loss - previous_profit_loss
        
        # Add the change to the list of changes
        if previous_profit_loss != 0:
            changes.append(change)
        
        # Update the previous profit/loss for the next iteration
        previous_profit_loss = profit_loss
        
        # Check if the current change is the greatest increase or decrease
        if change > greatest_increase[1]:
            greatest_increase = [row[0], change]
        if change < greatest_decrease[1]:
            greatest_decrease = [row[0], change]

# Calculate the average change
average_change = sum(changes) / len(changes)

# Format the results
output = f"""Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total_profit_losses}
Average Change: ${average_change:.2f}
Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})
Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})
"""

# Print the analysis to the terminal
print(output)

# Set the path to the output file
output_file_path = "financial_analysis.txt"

# Export the results to a text file
with open(output_file_path, 'w') as file:
    file.write(output)

print(f"The analysis has been exported to {output_file_path}.")
