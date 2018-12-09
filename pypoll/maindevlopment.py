import os
import csv
Filepath = os.path.join('..','..','..','UNCCHAR201811DATA3','02-Homework','03-Python','Instructions','PyPoll','Resources','election_data.csv')
#print(Filepath)
#C:/Users/cjans/documents/Bootcamp/HW2VBA/python-challenge/pypoll/.git/
#Filepath = '..\..\..\UNCCHAR201811DATA3\02-Homework\03-Python\Instructions\PyPoll\Resources\election_data.csv'
class Elect():
   def __init__(self, name):
      self.name = name
      self.votes = 1
   
   def countVote(self,z):
        self.votes += z   
        print(self.votes)

   def countVote1(self):
        self.votes += 1   
      
   def displayCanidate(self,total):
        #print(f"Name : {self.name} Salary: {self.votes}")
        print(f"{self.name}: {round(self.votes/total*100,3)}% ({self.votes})")

MyElection = {}
i = 0

with open(Filepath,newline= "") as Pollfile:
    csv_poll = csv.reader(Pollfile, delimiter=",")
    csv_header = next(csv_poll)
    print(csv_header)
    for row in csv_poll:
        n = row[2]
        i += 1
        #print(n)
        if n in MyElection:
            #print(n)
            #p1=MyElection[n]
            #print(p1.name)
            #p1.votes +=1
            #p1.countVote(1)
            #MyElection[n].countVote(1)
            MyElection[n].countVote1()
            #print(p1.votes)
            #p1.n.countVote
            #MyElection[n]= p1
            #print(p1.votes)
           
        else:
            p2 = Elect(n)
            #print(p2.name.title()+ "new")
            MyElection[n] = p2
        if i >1000:
            break        
Totalvotes = 0
Winner = ""
Maxvotes = 0
for x in MyElection:
    Totalvotes =Totalvotes + MyElection[x].votes
    print (Totalvotes)
for x in MyElection:
    if MyElection[x].votes > Maxvotes:
        Maxvotes = MyElection[x].votes
        Winner = MyElection[x].name
        print(Winner)

#print(len(MyElection))
print(f"       Election Results")
print(f"----------------------------")
print(f"Total Votes: {Totalvotes}")
print(f"----------------------------")
for x in MyElection:
    MyElection[x].displayCanidate(Totalvotes)
    #print(f"{p3.name}: {p3.votes/Totalvotes*100}% ({p3.votes})")
    #p3.displayCanidate(Totalvotes)
print(f"----------------------------")
print(f"Winner: {Winner}")
print(f"----------------------------")





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
