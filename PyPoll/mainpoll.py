
import os
import csv


voteTotal = 0


CsvPath = os.path.join("desktop", "Assignment-3", "PyPoll", "election_data.csv")

voteDictionary = {}
candidateName = ''
voterId = ''
county = ''
votesForCandidate = 0

# {'candiateName': [voterId list]}

with open(CsvPath, newline="") as csvfile:
  csv_reader = csv.reader(csvfile, delimiter=",")
  csv_header = next(csvfile)

  for row in csv_reader:
   
    voterId = row[0]
    county = row[1]
    candidateName = row[2]
    voteTotal += 1

    if candidateName not in voteDictionary.keys():
      voteDictionary[candidateName] = [voterId]

    else:
    
      voteDictionary[candidateName].append(voterId)
  

   
    

print(f'Candidate Names = ' + str(voteDictionary.keys()))
print(f'Total Number of Votes = {voteTotal}')

for candidateName in voteDictionary.keys():
  
  print(f'Total votes for candidate {candidateName} are: {len(voteDictionary[candidateName])} or (({len(voteDictionary[candidateName])}/{voteTotal}))')
  print (f'Winner is : {str(voteDictionary[0])}')


file = open('mailpoll.txt',"w")
print(f'Total votes for candidate {candidateName} are: {len(voteDictionary[candidateName])} or (({len(voteDictionary[candidateName])}/{voteTotal}))')
print (f'Winner is : {str(voteDictionary[0])}')
file.close()