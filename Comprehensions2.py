# Comprehensions 2:
from pprint import pprint as pp
from math import sqrt

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1 ):
        if x % i == 0:
            return False
    return True

# Making the list comprehension with filtering clause at the end

def main():
    prime_num = [x for x in range(101) if is_prime(x)]
    pp(f"Prime numbers{prime_num}")


    prime_square_divisors = {x*x : (1,x,x*x) for x in range(20) if is_prime(x)}
    pp(prime_square_divisors)

if __name__ == "__main__":
    main()
