n = 3
hor_links = [False] * (n * (n+1))
ver_links = [False] * (n * (n+1))

print(hor_links)   # 12 elements
print(ver_links)   # 12 elements

alphabets = list("abcdefghijklmnopqrstuvwxyz")[0:n+1]
numbers = list("0123456789")[0:n+1]

print(alphabets)   # 12 elements
print(numbers)   # 12 elements

dots = []
# dots = [x+str(num) for x in alphabetsfor num in numbers]
# print(dots)

for num in numbers:
    for i in alphabets:
        dots.append(i + num)
print(dots)


def is_linked(pos1, pos2, hor_links,ver_links):
