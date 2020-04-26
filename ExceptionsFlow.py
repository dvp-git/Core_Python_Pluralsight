# Exceptions and control flow:
import sys

DIGIT_MAP = {
    'zero':'0',
    'one':'1',
    'two':'2',
    'three':'3',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7',
    'eight':'8',
    'nine':'9',
    'ten':'10'
}


def convert(s):
    x = -1
    try:                        # Possibly would raise exception
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        print("Attempted and Successful")
        x = int(number)
    # except KeyError:
    #     print("Attempted and Failed")
    #     x = -1                  # Handles exception in case it is raised
    # except TypeError:
    #     print("Convertions failed due to incorrect type")
    #     x = -1
    # return x

    #Using a single except block for 2 types of errors
    except (KeyError,TypeError) as e:
        print(f"Conversion error: {e!r}",file=sys.stderr)
    return x

    #Re-raising an exception without using standard error control return types
    # except (KeyError,TypeError) as e:
    #     print(f"Conversion error: {e!r}",file=sys.stderr)
    #     raise

convert((123,123))
"""
Output:
========
>>> convert("I am a disco dancer".split(' '))
Attempted and Failed
-1
>>> convert("three five seven nine nine".split(' '))
Attempted and Successful
35799
>>> convert(123)
Convertions failed due to incorrect type
-1

Exception as object:
>>> convert((123,123))
Conversion error: KeyError(123)

>>> convert(123)
Conversion error: TypeError("'int' object is not iterable")

"""


"""
Query:
You're partially correct. When you say from ExceptionsFlow import convert, test_func, you're only importing the names "convert" and "test_func"
into your current namespace (in this case, the namespace of the REPL). However, the functions referred to by those names still have access to the objects
in ExceptionsFlow (e.g. the DIGIT_MAP dictionary). In other words, to use a function from another module, you only need to import that function,
not everything it depends on as well. This is a really important quality for maintainability.
"""
