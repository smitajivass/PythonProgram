try: 
	f=open("Employee Detail.txt","r")
	emprows, empcols = (13, 5) 
	empdata = [[0]*empcols]*emprows 
	empcount=0
	while True:
	     line=f.readline()
	     if ( line == ''):
		     break;
	     empdata[empcount]=line.split(" ")
	     empcount += 1 
	for i in range(1,empcount):
		     print(empdata[i])	
	f.close()					
except EOFError:
	print("END OF FILE") 
	f.close()
try: 
	t=open("Workdays File.txt","r")
	dayrows, daycols = (13, 5) 
	daydata = [[0]*daycols]*dayrows 
	daycount=0
	while True:
	     line=t.readline()
	     if ( line == ''):
		     break;
	     daydata[daycount]=line.split(" ")
	     daycount += 1 
	for i in range(1,daycount):
		     print(daydata[i])				
	t.close()
except EOFError:
	print("END OF FILE") 
	t.close()
fulltimeday=0
parttimeday=0
monthStr = input("Enter the Month for which salary need to be computated  : ")
for i in range(1,daycount):
	print(daydata[i])
	if monthStr == daydata[i][0]:
		fulltimeday = daydata[i][1]
		parttimeday = daydata[i][2]
		break;
print("fulltimeday = "+ str(fulltimeday))
print("parttimeday = "+ str(parttimeday))
print(monthStr)
for i in range(1,empcount):
	data = input("What is the actual number of days " +empdata[i][0] + " work for the month  ") 
	if(empdata[i][2] == "FT"):
		noofworkingdays = fulltimeday
	else:
		noofworkingdays = parttimeday

	print(noofworkingdays)
	print(data)
	salary=(int(data)/int(noofworkingdays)) * float(empdata[i][1]) 
	print(str(empdata[i][0])+" salary is Rs. " +str(salary))

	

