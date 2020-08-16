#import modules
import os
import csv

#define resource file path
csv_path = os.path.join("Resources","election_data.csv")

#declare variables
totalvotes = 0
candidates = []
cand_votes = []
cand_percent = []
winner = ""

#open resource file
with open(csv_path) as csvfile:
    #read resource file
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip header row
    csv_header = next(csvreader)

    #loop through each row of the dataset
    for row in csvreader:
        #add 1 to the total votes running total
        totalvotes += 1
        
        #populate candidate list, and add necessary list slots for votes and percentages lists
        if row[2] not in candidates:
            candidates.append(row[2])
            cand_votes.append(0)
            cand_percent.append(0.00)

        #add to candidate's running vote total
        for candidate in range(len(candidates)):
            if row[2] == candidates[candidate]:
                cand_votes[candidate] += 1
    
    #calculate candidate vote totals, and insert values in percentages list
    for candidate in range(len(candidates)):
        cand_percent[candidate] = round((cand_votes[candidate] / totalvotes)*100,2)     

    #find winner based on the candidates list index that matches the index of the max value of
    #the candidates' votes list
    winner = candidates[cand_votes.index(max(cand_votes))]

#print results to terminal
print("Election Results")
print("---------------------------")
print(f"Total Votes: {totalvotes}")
print("---------------------------")
for candidate in range(len(candidates)):  
    print(f"{candidates[candidate]}: {cand_percent[candidate]}% ({cand_votes[candidate]})") 
print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")

#output results to a new txt file

#define output file path
output_path =os.path.join("analysis","Election Analysis.txt")

#open output file in write mode
with open(output_path, "w") as output_file:
    #print results to output file
    output_file.write("Election Results\n")
    output_file.write("---------------------------\n")
    output_file.write(f"Total Votes: {totalvotes}\n")
    output_file.write("---------------------------\n")
    for candidate in range(len(candidates)):  
        output_file.write(f"{candidates[candidate]}: {cand_percent[candidate]}% ({cand_votes[candidate]})\n") 
    output_file.write("---------------------------\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write("---------------------------\n")
    