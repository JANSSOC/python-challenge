import os
import csv
bankpath = os.path.join('..','..','..', 'UNCCHAR201811DATA3','02-Homework','03-Python','Instructions','PyBank','Resources','budget_data.csv')

#bankpath = os.path.join('budget_data.csv')


#C:\Users\cjans\Documents\Bootcamp\UNCCHAR201811DATA3\02-Homework\03-Python\Instructions\PyBank\Resources

#C:/Users/cjans/documents/Bootcamp/HW2VBA/python-challenge/pybank/.git/
Month =0
Total_P_L = 0
Increase = 0
Inc_Month = "A"
Decrease = 0 
Dec_Month = "A"
Last_Month =0
Monthly_Change = 0
Current_val = 0

with open(bankpath,newline= "") as bankfile:
    csv_bank = csv.reader(bankfile, delimiter=",")
    csv_header = next(csv_bank)
    for row in csv_bank:
        Month = Month + 1
        Current_val = float(row[1])
        Total_P_L = Total_P_L + Current_val
        if Increase < Current_val:
            Increase = Current_val
            Inc_Month = row[0]
        if Decrease > Current_val:
            Decrease = Current_val
            Dec_Month = row[0]
        if Month > 1:
            Monthly_Change = Monthly_Change + abs(Last_Month - Current_val)       
        Last_Month = Current_val
        
print(f"       Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {Month}")
print(f"Total: ${Total_P_L}")
print(f"Average Change: ${Monthly_Change/Month}")
print(f"Greatest Increase in Profits: {Inc_Month} ({Increase})")
print(f"Greatest Decrease in Profits: {Dec_Month} ({Decrease})")

with open("Output.txt", "w") as text_file:
    print(f"       Financial Analysis", file=text_file)
    print(f"----------------------------", file=text_file)
    print(f"Total Months: {Month}", file=text_file)
    print(f"Total: ${Total_P_L}", file=text_file)
    print(f"Average Change: ${Monthly_Change/Month}", file=text_file)
    print(f"Greatest Increase in Profits: {Inc_Month} ({Increase})", file=text_file)
    print(f"Greatest Decrease in Profits: {Dec_Month} ({Decrease})", file=text_file)



"""               Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167) """
