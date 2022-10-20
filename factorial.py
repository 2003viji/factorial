# This program is used for finding the factorial for the given input value

# Here I used  the recursion methed for finding the factorial

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)

n=int(input("Enter your value :"))
print("Factorial of a given num is :",fact(n))
