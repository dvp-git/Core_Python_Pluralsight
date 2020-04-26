# Re-raising Exceptions


from math import log
from ExceptionsFlow import convert

def string_log(s):
    print(s)
    v = convert(s)
    return log(v)



print(string_log("ouch".split(' ')))


"""Output:

WITHOUT raise:
['ouch']
Conversion error: KeyError('ouch')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Darryl_Files\Learnings_Trainings\PluralSight_Courses\Python_Learning_Path\Pluralsight_Exercises_files\Core_Python\ReRaiseExceptions.py", line 14, in <module>
    print(string_log("ouch".split(' ')))
  File "C:\Darryl_Files\Learnings_Trainings\PluralSight_Courses\Python_Learning_Path\Pluralsight_Exercises_files\Core_Python\ReRaiseExceptions.py", line 10, in string_log
    return log(v)
ValueError: math domain error


WITH raise:
['ouch']
Conversion error: KeyError('ouch')
Traceback (most recent call last):
  File "C:\Darryl_Files\Learnings_Trainings\PluralSight_Courses\Python_Learning_Path\Pluralsight_Exercises_files\Core_Python\ReRaiseExceptions.py", line 14, in <module>
    print(string_log("ouch".split(' ')))
  File "C:\Darryl_Files\Learnings_Trainings\PluralSight_Courses\Python_Learning_Path\Pluralsight_Exercises_files\Core_Python\ReRaiseExceptions.py", line 9, in string_log
    v = convert(s)
  File "C:\Darryl_Files\Learnings_Trainings\PluralSight_Courses\Python_Learning_Path\Pluralsight_Exercises_files\Core_Python\ExceptionsFlow.py", line 25, in convert
    number += DIGIT_MAP[token]
KeyError: 'ouch'
"""
