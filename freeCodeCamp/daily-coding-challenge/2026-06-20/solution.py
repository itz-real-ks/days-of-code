
def prime_factorization(*,n:int):
    factors = []
    # to allow skipping even numbers later
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    
    # Checks odd numbers from 3 to sqrt(n)
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            factors.append(factor)
            n //= factor
        factor += 2
    
    # if n > 1 then the remaining number is prime
    if n > 1:
        factors.append(n)
    return factors  

num:int = int(input("Enter prime factorizing uInt: "))
print(f"Prime factor of {num}= \n \t {prime_factorization(n=num)}")
