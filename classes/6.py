nums = range(2, 100)
print("\nPrime numbers:")
for i in range(2, 10): 
    primes = list(filter(lambda x: x == i or x % i, nums))
print(primes)
