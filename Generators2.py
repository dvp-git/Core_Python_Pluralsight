# Stateful Generatror functions: Maintain the state of the generators in local variables to create a complex control flow and Lazy evaluation.

# Remember to yield an item , the next() function needs to be called on the generator object assigned to the generator functions

def take(count,iterable):
    """Takes the items from the front of an iterable

    Args:
        count: The number of items from the iterable to be taken,
        iterable: The iterable sequence.

    Returns:
        Yields the count items from the iterable
    """
    counter = 0
    for item in iterable:
        if count == counter:
            return
        counter +=1
        yield item

def distinct(iterable):
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)


# def run_pipeline():
#     """This will give the counted items one by one
#     Using for loop , since take( .... ) is a generator functions\
#     Here the count= 7 , so 7 objects will be printed"""
#     items = [1,2,4,5,18,36,1,3,2,22,]
#     for item in take(7,items):
#         print(item)


# def run_pipeline():
#     """Remove the duplicates and run the pipeline"""
#     items = [1,1,1,1,1,3,1,3,2,3,2,22,2,8,9]
#     for item in distinct(items):
#         print(item)


def run_pipeline():
    """This will remove the duplicate items and return the 'count' number of objects"""
    items = [1,1,1,1,1,3,1,3,2,3,2,22,2,8,9]
    for item in take(5,distinct(items)):
        print(item)                        # Note that print is required here since the yield returns a value to item, which needs to be printed

run_pipeline()


"""
Output:
only take():(7,[1,2,4,5,18,36,1,3,2,22,])
1
2
4
5
18
36
1

only distinct():[1,1,1,1,1,3,1,3,2,3,2,22,2,8,9]
1
3
2
22
8
9

Pipeline Output:
1
3
2
22
8

"""
