## 3.Read a file containing birthdays. Check todays date and display the birthday that is today
## Eg.  file:
## 02-04-1884  "Lord Tennyson"
## 06-09-1995 "Herbert"
## 08-09-2015 "Vimala"

## todays date is : 06-09-2019
## Display:
## Happy Birthday Herbert!


from datetime import date
today = date.today()
# dd/mm/YY
d1 = today.strftime("%d-%m-%Y")
d2 = today.strftime("%d-%m")
data = []
f=open("bday.txt", "r")
data_array=[]

print("Todays date is :",d1)
while True:
    # read line
    line = f.readline()
    data=line.split(" ")
    print(data)
    if not line.find(d2):
    	if(len(data)>1):
         	print("Happy Birthday ",data[1])
    if not line:
        break

f.close()







