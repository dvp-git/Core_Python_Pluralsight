# Decorators

"""A decorator is a function which takes another function as an argument and returns a modified version of it, \
enhancing its functionality in some way.

Ref: https://samireland.com/writing/decorators/


"""
#Decorator function:
def accept_integers(func):
    def new_func(s):
        if isinstance(s, int):
            s = str(s)
        return func(s)
    return new_func


def make_palindrome(string):
    """Makes a palindromic mirror of a string."""
    return string + string[::-1]


def add_credits(string):
    """Adds the company's credits to the end of any string."""

    return f"{string} (string created by Pro String Inc.)"


def snake_to_camel(string):
    """Converts a string in snake_case to camelCase."""

    words = string.split("_")
    if len(words) > 1:
    	  words = [words[0]] + [word.title() for word in words[1:]]
    return "".join(words)


def insert_commas(string, spacing=3):
  """Inserts commas between every n characters."""

  sections = [string[i: i + spacing] for i in range(0, len(string), spacing)]
  print(sections)
  return ",".join(sections)


make_palindrome = accept_integers(make_palindrome)
add_credits = accept_integers(add_credits)
snake_to_camel = accept_integers(snake_to_camel)
insert_commas =  accept_integers(insert_commas)


x =make_palindrome(12311223)
print(x)
