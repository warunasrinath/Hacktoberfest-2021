# Python program to find the factorial of a number provided by the user.

# change the value for a different result
num = int(input('enter the number\n'))


factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial *= i
   print("The factorial of",num,"is",factorial)
