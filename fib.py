#code 
# Write code below here
n = int(input("enter number: "))
if(n<=0):
    print("invalid")
if(n==1):
    print(0)
if(n>=2):
    a=0
    b=1
    for i in range(0,n):
        c=a+b
        print(c)
        a=b
        b=c
# Print the n'th fibon
