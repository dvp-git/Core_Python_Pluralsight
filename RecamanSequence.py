# Recaman Sequence:
import sys

# The Recaman Sequence is a sequnce in which the nth term a(n) =  a(n - 1)th term - n if the value is positive, if it is yielding a negative result, a(n - 1) + n
# RECAMAN SERIES
# a(n) = { a(n-1) - n , if result is > 0
#          a(n-1) + n , otherwise

from itertools import islice, count

#class islice(builtins.object)
#  |  islice(iterable, stop) --> islice object
#  |  islice(iterable, start, stop[, step]) --> islice object
#  |
#  |  Return an iterator whose next() method returns selected values from an
#  |  iterable.  If start is specified, will skip all preceding elements;
#  |  otherwise, start defaults to zero.  Step defaults to one.  If
#  |  specified as another value, step determines how many values are
#  |  skipped between successive calls.  Works like a slice() on a list
#  |  but returns an iterator.


def recaman_seq():
    """Generate the recama sequence"""
    seen = set()
    a = 0
    for n in count(1):
        if n > 100:
            break
        yield a
        seen.add(a)
        c = a - n
        if c < 0 or c in seen:
            # If the value is negative OR if the value ( a(n - 1) - n )is already present in the series,
            # proceed to get the other number ( a(n - 1) + n )
            c = a + n
        a = c

def write_sequence(filename,num):
    """Write the Recaman series to a text file"""
    f = open(filename, mode = 'wt', encoding='utf-8')
    f.writelines(f"{r}\n" for r in islice(recaman_seq(), num))
    f.close()

if "__main__" == __name__ :
    write_sequence(filename=sys.argv[1],num=int(sys.argv[2]))


# write_sequence('Recamman.dat',50)
# a = islice(recaman_seq(), 20)
# for i in a:
#     print(i)


# Output saver to Recaman.dat
# C:\Darryl_Files\Learnings_Trainings\PluralSight_Courses\Python_Learning_Path\Pluralsight_Exercises_files\Core_Python>python RecamanSequence.py RecamanSequence.dat 50
