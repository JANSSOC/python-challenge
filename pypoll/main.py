# import the required modules
import os
import csv
# connect to File location
Filepath = os.path.join('..','..','..','UNCCHAR201811DATA3','02-Homework','03-Python','Instructions','PyPoll','Resources','election_data.csv')

# Create Elect Class
class Elect():
   def __init__(self, name):
        self.name = name
        self.votes = 1
           
   def countVote(self):
        self.votes += 1   
      
   def displayCandidate(self,total,output):
        if output == "text":
            print(f"{self.name}: {round(self.votes/total*100,3)}% ({self.votes})", file=text_file)
        else:
            print(f"{self.name}: {round(self.votes/total*100,3)}% ({self.votes})")

# Create Dictionary to store tally of votes by canidate.
MyElection = {}
# Create counter for debugging
#i = 0
# Open csv file and loop through creating candiates as they are found, and tallying the votes
with open(Filepath,newline= "") as Pollfile:
    csv_poll = csv.reader(Pollfile, delimiter=",")
    csv_header = next(csv_poll)
    # Cycle through all lines in input file after the header
    for row in csv_poll:
        # Assign name of canidate to variable
        n = row[2]
        # Counter for debugging
        #i += 1
        # If name exists in dictionary use class method to update vote tally 
        if n in MyElection:
            MyElection[n].countVote()
        # If name does not exist add to dictionary         
        else:
            MyElection[n] = Elect(n)
        # Debugging to stop at 1001 rows reviewed.     
        #if i >1000:
        #    break     

# Create summary after tally of votes           
Totalvotes = 0
Winner = ""
Maxvotes = 0

# loop through dictionary to find total votes
for x in MyElection:
    Totalvotes =Totalvotes + MyElection[x].votes

# loop though dictionary to find Winner    
for x in MyElection:
    if MyElection[x].votes > Maxvotes:
        Maxvotes = MyElection[x].votes
        Winner = MyElection[x].name

# Display results as required       
print(f"      Election Results")
print(f"----------------------------")
print(f"Total Votes: {Totalvotes}")
print(f"----------------------------")
for x in MyElection:
    MyElection[x].displayCandidate(Totalvotes,"Print")
print(f"----------------------------")
print(f"Winner: {Winner}")
print(f"----------------------------")
# Send output to text file. 
with open("Output.txt", "w") as text_file:
    print(f"      Election Results", file=text_file)
    print(f"----------------------------", file=text_file)
    print(f"Total Votes: {Totalvotes}", file=text_file)
    print(f"----------------------------", file=text_file)
    for x in MyElection:
        MyElection[x].displayCandidate(Totalvotes,"text")
    print(f"----------------------------", file=text_file)
    print(f"Winner: {Winner}", file=text_file)
    print(f"----------------------------", file=text_file)

# Output guidance from assignment
"""   Election Results
  -------------------------
  Total Votes: 3521001
  ------------------------- 
  Khan: 63.000% (2218231)
  Correy: 20.000% (704200)
  Li: 14.000% (492940)
  O'Tooley: 3.000% (105630)
  -------------------------
  Winner: Khan
  ------------------------- """

