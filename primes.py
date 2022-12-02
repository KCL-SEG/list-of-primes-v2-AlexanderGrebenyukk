"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    currentNumber = 2
    while(number_of_primes>len(list)):
        prime=True

        for i in range(2, currentNumber-1):
            if(currentNumber%i==0):
                prime = False
                break

        if prime:
            listPrimes.append(currentNumber)
            currentNumber = currentNumber + 1
        else:
            currentNumber = currentNumber + 1
    return list
