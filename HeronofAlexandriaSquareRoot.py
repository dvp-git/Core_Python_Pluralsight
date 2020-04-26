#Heron of Alexandria to compute square root
import sys

def sqrt(x):
    """Compute the square root using method of Heron of Alexandria

    Args:
        x : The number for which we need to compute square root.

    Returns:
        THe square root of x

    Raises:
        Error if x is negative.
    """
    if x < 0:
        raise ValueError(f"Cannot compute the square root of negative number {x}")
    guess = x
    i = 0
    try:
        while guess * guess != x and i < 20:
            guess = (guess + x/guess)/2.0
            i += 1
    except ZeroDivisionError:
        raise ValueError()
    return guess


def main():
    try:
        print(sqrt(9))
        print(sqrt(144))
        print(sqrt(-1.0))
        print("This line is not printed")
    except ValueError as e:
        print(e,file=sys.stderr)
    print("Normal Execution here")

main()



"""
sqrt(-1):
3.0
12.0
Traceback (most recent call last):
  File "C:\Darryl_Files\Learnings_Trainings\PluralSight_Courses\Python_Learning_Path\Pluralsight_Exercises_files\Core_Python\HeronofAlexandriaSquareRoot.py", line 27, in <module>
    main()
  File "C:\Darryl_Files\Learnings_Trainings\PluralSight_Courses\Python_Learning_Path\Pluralsight_Exercises_files\Core_Python\HeronofAlexandriaSquareRoot.py", line 25, in main
    print(sqrt(-1.0))
  File "C:\Darryl_Files\Learnings_Trainings\PluralSight_Courses\Python_Learning_Path\Pluralsight_Exercises_files\Core_Python\HeronofAlexandriaSquareRoot.py", line 17, in sqrt
    guess = (guess + x/guess)/2.0
ZeroDivisionError: float division by zero
"""
