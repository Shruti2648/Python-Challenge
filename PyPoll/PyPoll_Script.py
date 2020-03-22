# Import dependencies:
import os 
import csv

# Path to collect data from the Resources folder:
election_data_csv = os.path.join('Resources', 'election_data.csv')

# Declare variables:

total_votes = 0

votes_won_Khan = 0
votes_won_Correy = 0
votes_won_Li = 0
votes_won_OTooley = 0

candidates = {
    "Khan": votes_won_Khan,
    "Correy": votes_won_Correy,
    "Li": votes_won_Li,
    "O'Tooley": votes_won_OTooley
}

winner = ""

# Read the CSV file:
with open(election_data_csv, newline='') as csvfile:

    # Split the data on commas:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip the header row:
    header = next(csvreader)

# Iterate through every row and determine the total votes and votes per candidate:
    for row in csvreader:

        total_votes = total_votes + 1

        if (election_data_csv[2] == "Khan"):
            votes_won_Khan = votes_won_Khan + 1
            candidates.update({"Khan": votes_won_Khan})

        elif (election_data_csv[2] == "Correy"):
            votes_won_Correy = votes_won_Correy + 1
            candidates.update({"Correy": votes_won_Correy})           

        elif (election_data_csv[2] == "Li"):
            votes_won_Li = votes_won_Li + 1
            candidates.update({"Li": votes_won_Li})

        elif (election_data_csv[2]== "O'Tooley"):
            votes_won_OTooley = votes_won_OTooley + 1
            candidates.update({"O'Tooley": votes_won_OTooley})

    # Determine the winner:
    winner = max(candidates)
    
    # Print results:

    print("ELECTION RESULTS:")
    print("Total Votes: " + str(total_votes))

    print(candidates)

    percent_won_Khan = votes_won_Khan / total_votes * 100
    percent_won_Correy = votes_won_Correy / total_votes * 100
    percent_won_Li = votes_won_Li / total_votes * 100
    percent_won_OTooley = votes_won_OTooley / total_votes * 100    

    print("Khan: " + str(percent_won_Khan)) 
    print("Correy: " + str(percent_won_Correy))
    print("Li: " + str(percent_won_Li))
    print("O'Tooley: " + str(percent_won_OTooley))

    print("Winner: " + winner)
    
        

