# Example of List copies and list repeatation
import copy

list_1 = [1,2,3,4,5,6]

list_2 = list_1[:]

# Test for equivalence:
print("\n############### Test for List Equivalence ################\n ")
print(f"list_1 is equivalent to list_2 {list_1 == list_2}")
print(f"list_1 is list_2 {list_1 is list_2}")


# Note that these are shallow copies, meaning that the elements within both the lists refer to the same object
print(f" Note that these are shallow copies, meaning that the elements within both the lists refer to the same object")
for i in range(0,len(list_1)):
    print(f"list[{i}] equal to list[{i}] : {list_1[1] == list_2[1]}")


# Shallow copy can be done using:
# list_1 = list_2[:]
# list_2 = copy.copy(list_1)
# list_2 = list(list_1)

# Demonstrating Deep copy

print("\n############### Demonstrating Deep copy ################\n ")
list_1 = copy.deepcopy(list_1)
print(f"list_1:{list_1}")
list_1[0] = 1231
print(f"Changed list_1: {list_1}")
print(f"list_2: {list_2}")


# Demonstrating list repeatation

print("\n############### Demonstrating list repeatation ################\n ")
repeat_1 = [[1,0,2]] * 4

print(f"Initial list for repeat{repeat_1}")

print(f"Making repeat_1[1][2] = 819" )
print(f"Appending 900 to first list repeat_1[0].append(900)")
repeat_1[1][2] = 819
repeat_1[0].append(900)


print(f"Final result makes changes in all the entries: {repeat_1}")


"""
Output:
list_1 is equivalent to list_2 True
list_1 is list_2 False
 Note that these are shallow copies, meaning that the elements within both the lists refer to the same object
list[0] equal to list[0] : True
list[1] equal to list[1] : True
list[2] equal to list[2] : True
list[3] equal to list[3] : True
list[4] equal to list[4] : True
list[5] equal to list[5] : True
"""
