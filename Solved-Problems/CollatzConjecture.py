'''
The Collatz conjecture in mathematics asks whether repeating two simple arithmetic operations will eventually transform every positive integer into one. 
It concerns sequences of integers in which each term is obtained from the previous term as follows: 
if the previous term is even, the next term is one half of the previous term. 
If the previous term is odd, the next term is 3 times the previous term plus 1. 
The conjecture is that these sequences always reach 1, no matter which positive integer is chosen to start the sequence.
'''

def Collatz_Conjecture(n):
    if n < 1:
        return "Input must be greater than 0"
    
    while n < 100000:
        if n % 2 == 0:
            n = n // 2
            print(n)
        else:
            n = (n * 3) + 1
            print(n)

        if n == 1:
            break


Collatz_Conjecture(2048)
