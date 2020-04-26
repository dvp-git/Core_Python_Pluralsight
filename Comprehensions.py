# Comprehensions 1:
import os
import glob
from math import factorial
from pprint import pprint as pp
"""
Notes:
List comprehension  : [ expr(item) for item in iterable]
Set comprehension   : { expr(item) for item in iterable}
Dict comprehension  : {key_expr(item):value_expr(item) for item in iterable} =--- Use dict.items() method

"""
#List comprehension
words = "Why sometimes I have believed as many s si impossible things before breakfast".split()
print([len(word) for word in words])

#finding the number of decimal digits for first 20 factorials
f = [len(str(factorial(X))) for X in range(21)]
print(f)

# Dictionary Comprehensions
country_to_capital = {'UK':'London',\
                    'Brazil':'Brasilia',\
                    'Morocco':'Rabat',\
                    'Sweden':'Stockholm'}
capital_to_country = { capital:country for country,capital in country_to_capital.items()}
pp(capital_to_country)

#Complex comprehension: Mapping filesize to their paths:
file_sizes = {os.path.realpath(p): os.stat(p).st_size for p in glob.glob('*.py')}
print("Below are the file sizes in format : 'PATH':'size'")
pp(file_sizes)


"""
Ouput
[3, 9, 1, 4, 8, 2, 4, 1, 2, 10, 6, 6, 9]
[1, 1, 1, 1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 18, 19]
{'Brasilia': 'Brazil',
 'London': 'UK',
 'Rabat': 'Morocco',
 'Stockholm': 'Sweden'}
Below are the file sizes in format : 'PATH':'size'
{'C:\\Darryl_Files\\Learnings_Trainings\\PluralSight_Courses\\Python_Learning_Path\\Pluralsight_Exercises_files\\Core_Python\\CommandLineArgument.py': 1524,
 'C:\\Darryl_Files\\Learnings_Trainings\\PluralSight_Courses\\Python_Learning_Path\\Pluralsight_Exercises_files\\Core_Python\\Comprehensions.py': 1160,
 'C:\\Darryl_Files\\Learnings_Trainings\\PluralSight_Courses\\Python_Learning_Path\\Pluralsight_Exercises_files\\Core_Python\\Decorators.py': 1387,
 'C:\\Darryl_Files\\Learnings_Trainings\\PluralSight_Courses\\Python_Learning_Path\\Pluralsight_Exercises_files\\Core_Python\\ExceptionsFlow.py': 2116,
 'C:\\Darryl_Files\\Learnings_Trainings\\PluralSight_Courses\\Python_Learning_Path\\Pluralsight_Exercises_files\\Core_Python\\HeronofAlexandriaSquareRoot.py': 1619,
 'C:\\Darryl_Files\\Learnings_Trainings\\PluralSight_Courses\\Python_Learning_Path\\Pluralsight_Exercises_files\\Core_Python\\ListCopyTest.py': 1827,
 'C:\\Darryl_Files\\Learnings_Trainings\\PluralSight_Courses\\Python_Learning_Path\\Pluralsight_Exercises_files\\Core_Python\\ReRaiseExceptions.py': 1476,
 'C:\\Darryl_Files\\Learnings_Trainings\\PluralSight_Courses\\Python_Learning_Path\\Pluralsight_Exercises_files\\Core_Python\\SetOperations.py': 2156,
 'C:\\Darryl_Files\\Learnings_Trainings\\PluralSight_Courses\\Python_Learning_Path\\Pluralsight_Exercises_files\\Core_Python\\UrlBytesTest.py': 1552,
 'C:\\Darryl_Files\\Learnings_Trainings\\PluralSight_Courses\\Python_Learning_Path\\Pluralsight_Exercises_files\\Core_Python\\argparseExample.py': 1127,
 'C:\\Darryl_Files\\Learnings_Trainings\\PluralSight_Courses\\Python_Learning_Path\\Pluralsight_Exercises_files\\Core_Python\\fetch_words.py': 2360}
"""
