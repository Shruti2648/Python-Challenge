# Import dependencies:
import os 
import csv

# Path to collect data from the Resources folder:
budget_data_csv = os.path.join('Resources', 'budget_data.csv')

# Declare variables:

total_months = 0
totalPL = 0
profits_array = []
losses_array = []

# Read the CSV file:
with open(budget_data_csv, newline='') as csvfile:

    # Split the data on commas:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip the header row:
    header = next(csvreader)

# Iterate through every row and perform the following on each row:
    for row in csvreader:

        total_months = total_months + 1

        totalPL = totalPL + int(budget_data_csv[1])

        if (budget_data_csv[1] < 0):
            losses_array.append(int(budget_data_csv[1]))
        else:
            profits_array.append(int(budget_data_csv[1]))

# Calculate average change in profits/losses over the entire period:

    averagePL = totalPL / total_months

# Determine the greatest increase in profits and decrease in losses over the entire period:

    max_profit = max(profits_array) - min(profits_array)

    max_loss = max(losses_array) - min(profits_array)

# Print results:

    print("FINANCIAL ANALYSIS")
    print("Total Months: " + total_months)
    print("Total Profits: $" + totalPL)
    print("Average Change: $" + averagePL)
    print("Greatest Increase in Profits: $" + max_profit)
    print("Greatest Decrease in Profits: $" + max_loss)


