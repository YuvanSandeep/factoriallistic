n = 0
def recur_factorial (n):
    if n == 1:
        return n
    else:
        return n*recur_factorial(n-1)
number = int(input("What is your number? "))
if number < 0:
    print ("Sorry, factorial of negative numbers do not exist.")
elif number == 0:
    print ("The factorial of 0 is 1")
else:
    print (recur_factorial(number))