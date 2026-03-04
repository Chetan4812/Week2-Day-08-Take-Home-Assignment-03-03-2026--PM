#Performance (Efficiency): The current loop runs up to n-1 This is O(n) complexity. You only need to check divisors up to the square root of n
#If n has a factor larger than root(n), it must have a corresponding factor smaller than root(n) 

#Logic/Redundancy: While not a "crash" bug, the code checks every single number. 
# By handling the number 2 as a special case, we can skip all even numbers in the loop, cutting the work in half.


import math

def is_prime(n):
    if n < 2: 
        return False
    
    if n == 2: 
        return True
    
    if n % 2 == 0: 
        return False
    
    limit = int(math.sqrt(n)) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
            
    return True
