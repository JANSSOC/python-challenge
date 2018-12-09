import os
import csv
Filepath = os.path.join('..','..','..', 'UNCCHAR201811DATA3','02-Homework','03-Python','Instructions','PyPoll','Resources','election_data.csv')

#C:/Users/cjans/documents/Bootcamp/HW2VBA/python-challenge/pypoll/.git/

#C:\Users\cjans\Documents\Bootcamp\UNCCHAR201811DATA3\02-Homework\03-Python\Instructions\PyPoll\Resources

MyElection = {
    "Khan": 0,
    "Correy": 0,
    "Li": 0,
  "O'Tooley":0
}
i = 0
name = ""
vote = 1

with open(Filepath,newline= "") as Pollfile:
    csv_poll = csv.reader(Pollfile, delimiter=",")
    csv_header = next(csv_poll)
    print(csv_header)
    for row in csv_poll:
        n = row[2]
        i += 1
        #print(n)
        if n in MyElection:
            y=MyElection[n]
            y = y + 1
            #print(y)
            MyElection[n] = y
            #print(row[2])
           
        else:
            print("NO")
        #if i >1000:
         #   break        


print(f"       Election Results")
print(f"----------------------------")
print(f"Total Votes: ")
print(f"----------------------------")
print(len(MyElection))
for x in MyElection:

    p3 = MyElection[x]
    print(p3)
    
    




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
