"""
    Multiples of 3 or 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.

Find and print the sum of all the multiples of 3 or 5 below 1000.
"""
#variable sorting total
total=0
# using for loop
for i in range(1000):
    #check reminder is zero or not
    if i%3 == 0 or i% 5== 0:
        total = total + i 
        print(total)
#Sum of all the multiples of 3 or 5 below 1000 =233168


 
    




    

    















    
    

