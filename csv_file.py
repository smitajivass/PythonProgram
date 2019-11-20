#import necessary modules
import csv
with open('/home/rahul/Employee_Details.csv','rt') as f:
   data = csv.reader(f)
   for row in data:
         print(row)



