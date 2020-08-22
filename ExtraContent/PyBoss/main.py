#import modules
import csv
import os

#define resource file path
filepath = os.path.join("employee_data.csv")

#declare variables
converted_data = []
ConvertedDOB = ""
SSNFinalFour = ""
ConvertedSSN = ""
StateAbbrev = ""
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

#open resource file
with open(filepath) as csvfile:
    #read resource file
    employees = csv.reader(csvfile,delimiter=",")

    #skip header row
    csvheader=next(employees)
    
    #define new header
    converted_data.append(["Emp ID","First Name","Last Name","DOB","SSN","State"])

    #for each row in the datafile, do the following
    for row in employees:
        #convert name into array of [first name,last name]
        SplitName = row[1].split(" ")
        #convert DOB into an array of [year,month,day]
        SplitDOB = row[2].split("-")
        #rearrange name array items into a new string with month/day/year format
        ConvertedDOB = SplitDOB[1] + "/" + SplitDOB[2] + "/" + SplitDOB[0]
        #create a string containing only the last 4 characters of SSN
        SSNFinalFour = row[3][-4] + row[3][-3] + row[3][-2] + row[3][-1]
        #create a string that shows astrerisks and the final four of SSN
        ConvertedSSN = "***-**-" + SSNFinalFour
        #find and record state abbreviation
        StateAbbrev = us_state_abbrev[row[4]]

        #add all converted data as a new list item within the converveted data list
        converted_data.append([row[0],SplitName[0],SplitName[1],ConvertedDOB,ConvertedSSN,StateAbbrev])

#OUTPUT RESULTS TO NEW FILE
#create new file path
outputpath = os.path.join("converted_employee_data.csv")

#open output file in write mode
with open(outputpath, "w",newline="") as outputfile:
    outputwriter = csv.writer(outputfile,delimiter=",")
    #write each row to the output file
    for item in range(len(converted_data)):
        outputwriter.writerow(converted_data[item])