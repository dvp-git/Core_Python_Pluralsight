 # Generators:
import sys
"""
 Generators are iterable sequeces which make use of the yield keyword to return values. Lazy evaluation is the key here \
 which means that the next value of the iterable is computed on demand.
 * Can be used to model large infinite sequences : Ex: Logging , streams of data from sensors
 * Can be composed into complex pieplines ( Stream processing)\
 """

def gen():
     "Generator function can have an implict return statement"
     yield 1
     yield 2
     yield 3
     return

g = gen()

print(f"g is a {g} , an iterator")
print(f"1st next(g): {next(g)}")
print(f"2nd next(g): {next(g)}")
print(f"3rd next(g): {next(g)}")

"""
* Generators can be used with for loops or any constructs that expects an iterable , since generators are iterators and every object of an iterator is
  an iterable
* When the fiest yield is encountered by call to the next() , the geneator function stops execution and yields the value. On successive next calls, \
the program continues from the last stop place i.e. the state of the call is remembered. Belos is a demonstration.
 """

 # Demonstration of the yield states using print statements
def gen1295():
    print("About to yield 1")
    yield 1
    print("About to yield 2")
    yield 2
    print("About to yield 9")
    yield 9
    print("About to yield 5")
    yield 5
    print("About to return")
    return

g = gen1295()
try:
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
except StopIteration as e:
    print(f"Stop iteration here and continue {e}",file=sys.stderr)
    print("Program continues")
