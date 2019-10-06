lower = 1
upper = 1000

# Initialize a list
primes = []
for possiblePrime in range(lower, upper + 1):
    # prime numbers are greater than 1
    if possiblePrime > 1:
        for i in range(2, possiblePrime):
            if (possiblePrime % i) == 0:
                break
        else:
            primes.append(possiblePrime)
