n = int(input("enter number: "))
# Write code below here
for i in range (2,n):
    if n % i == 0:
        print(n,"is not a prime")
        break
    else:
        print(n,"is a prime number")
# Print the n'th prime number
 #submission