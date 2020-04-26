# Making use of standard library itertools.islice and itertools.count

from itertools import islice, count
from Comprehensions2 import is_prime
thousand_primes = islice((x for x in count() if is_prime(x)),1000)
for i in thousand_primes:
    print(i)

print(f"Sum is {sum(islice((x for x in count() if is_prime(x)),1000))}")
