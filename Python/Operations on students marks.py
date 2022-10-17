marks=[]
n=int(input("enter a no. of students:"))
def read():
	for i in range (n):
		num=int(input("enter the marks:"))
		marks.append(num)
def display():
	print(marks)
	
def avg():
	sum=0
	cnt=0
	for i in range(n):
		if(marks[i]>=0):
			sum+=marks[i]
			cnt+=1
		avg=sum/cnt
	print("The Average marks is:",avg)
	print("Absent Student Count is:",(n-cnt))
		
def hs():
	max=0
	for i in range(n):
		if((marks[i]>=0) and (marks[i]>max)):
			max=marks[i]
	print("The Maximum value is:",max)
		
def ls():
	min=0
	for i in range(n):
		if((marks[i]>=0) and (marks[i]<min)):
			min=marks[i]
	print("The Minimum value is:",min)

def absent():
	ab=0
	for i in range(n):
		 if(marks[i]<0):
		 	ab+=1
	print("The no. of absent students is:",ab)
	
def hsf():
	hsf=0
	for i in range(n):
		a=0
		if(marks[i]==marks[a+1]):
			 hsf+=1
	print("Highest Frequency is:",hsf)
		
def main():
	read()
	display()
	avg()
	hs()
main() 
