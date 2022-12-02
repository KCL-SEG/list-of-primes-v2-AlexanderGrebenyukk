"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError
    else:
        list = []
        currentNumber = 2
        while(number_of_primes>len(list)):
            prime=True

            for i in range(2, currentNumber-1):
                if(currentNumber%i==0):
                    prime = False
                    break

            if prime:
                list.append(currentNumber)
                currentNumber = currentNumber + 1
            else:
                currentNumber = currentNumber + 1
        return list
