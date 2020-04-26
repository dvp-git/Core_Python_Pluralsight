# Demonstrating the file-like behaviours for various file types:
 # -->  Text files
 # -->  Binary files
 # -->  URL Readers ( Example below:)

from urllib.request import urlopen


def words_per_line(filename):
    return [len(line.split()) for line in filename.readlines()]

with open('wasteland.txt',mode='rt') as fileObj:
    wpl =  words_per_line(fileObj)
    print(wpl)

print(f"Type of the file :{type(fileObj)}")   # Here file is _io.TextIOWrapper


# Demonstration of URL file reader
with urlopen('https://sixty-north.com/c/t.txt') as urlfile:
    wpl =  words_per_line(urlfile)
    print(wpl)


print(f"Type of the URL file :{type(urlfile)}")   # Here file is http.client.HTTPResponse

# Both files are of different types. However since both are file-like objects , the function to read, works for BOTH. Duck Typing.


""" OUtput:
[9, 8, 9, 9]
Type of the file :<class '_io.TextIOWrapper'>

[6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 5, 7, 8, 14, 12, 8]
Type of the URL file :<class 'http.client.HTTPResponse'>

"""
