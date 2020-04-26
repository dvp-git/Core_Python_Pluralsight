## Making use of functions: fetch_words

def fetch_words():
        from urllib.request import urlopen
        story = urlopen('https://sixty-north.com/c/t.txt')                  # Bytes returned HTTP response
        story_words = []
        # print("story format: {}".format(type(story)))
        for line in story:                                                  # HTTP byte response
            line_words = line.decode('utf-8').split()                       # List type
            for word in line_words:                                         # Strings
                story_words.append(word)
        story.close()
        for word in story_words:
            print(word)

# print(__name__)
if "__main__" == __name__:
    fetch_words()



"""Ouputs vary when IMPORTED OR when RUN AS SCRIPT
IMPORTED:
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import fetch_words
fetch_words


RUN AS SCRIPT:
C:\\Darryl_Files\\Learnings_Trainings\\PluralSight_Courses\\Python_Learning_Path\\Core_Python>python fetch_words.py
__main__


=========================INSTEAD USE:=========================
 if __name__ == "__main__":
     fetch_words()

IMPORTED:
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:06:47) [MSC v.1914 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import fetch_words
>>>

RUN AS SCRIPT:
C:\\Darryl_Files\\Learnings_Trainings\PluralSight_Courses\\Python_Learning_Path\\Core_Python>python fetch_words.py
It
was
the
best
of
times
it
was
the
worst
of
times
it
was
the
age
of
wisdom
it
was
the
age
of
foolishness
it
was
the
epoch
of
belief
it
was
the
epoch
of
incredulity
it
was
the
season
of
Light
it
was
the
season
of
Darkness
it
was
the
spring
of
hope
it
was
the
winter
of
despair
we
had
everything
before
us
we
had
nothing
before
us
we
were
all
going
direct
to
Heaven
we
were
all
going
direct
the
other
way
in
short
the
period
was
so
far
like
the
present
period
that
some
of
its
noisiest
authorities
insisted
on
its
being
received
for
good
or
for
evil
in
the
superlative
degree
of
comparison
only
"""
