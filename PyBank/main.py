import os
import csv

csvpath = os.path.join("Resources","budget_data.csv")

total_months = 0
total_net = 0
avg_net = 0.00
greatest_increase_amt = 0
greatest_increast_mo = ""
greatest_decrease_amt = 0
greatest_decrease_mo = ""

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header=next(csvreader)

    for row in csvreader:
        total_months += 1
        total_net += float(row[1])
        avg_net = round(total_net / total_months,2)
        if int(row[1]) > greatest_increase_amt:
            greatest_increase_amt = int(row[1])
            greatest_increase_mo = row[0]
        if int(row[1]) < greatest_decrease_amt:
            greatest_decrease_amt = int(row[1])
            greatest_decrease_mo = row[0]

print("Financial Analysis")
print("------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_net}")
print(f"Average Change: ${avg_net}")
print(f"Greatest Increase in Profits: {greatest_increase_mo} (${greatest_increase_amt})")
print(f"Greatest Decrease in Profits: {greatest_decrease_mo} (${greatest_decrease_amt})")

output_path =os.path.join("analysis","Financial Analysis.txt")

with open(output_path, "w") as output_file:
    output_file.write(f"Financial Analysis\n")
    output_file.write("------------------------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${total_net}\n")
    output_file.write(f"Average Change: ${avg_net}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase_mo} (${greatest_increase_amt})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease_mo} (${greatest_decrease_amt})\n")
