# Zip function : yields tuples when iterated
from itertools import chain

sunday = [12, 14, 16, 18,]
monday = [13, 14, 15, 17,]
tuesday = [2, 2, 3, 7, 9]
#Zip yields tuples
for item in zip(sunday,monday):
    print(item)

# Average values
for sun,mon in zip(sunday,monday):
    print("Average : ",(sun + mon)/2.0)


# Zip can accept multiple arguments
for temps in zip(sunday,monday,tuesday):
    print("Temp values",temps)
    print(f"min = {min(temps):4.1f} , max = {max(temps):4.1f} ,average = {sum(temps)/len(temps):4.1f}")

temperatures = chain(sunday,monday,tuesday)  # Chain concatenates iterables and removes any duplicates. = Long temperature series
for i in temperatures:
    print(i)
