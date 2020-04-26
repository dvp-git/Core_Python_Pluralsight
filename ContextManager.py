# Creating a simple Context Manager.
# The 'with' statement can be used anywhere the context manager protocol is supported.
""" Demonstrate a Raid on the fridge"""

from contextlib import closing

class RaidRefridgerator():
    """ Raid a Refridgerator"""
    def open(self):
        print("Opening the fridge door")

    def take_food(self,food):
        print(f"Finding food item : {food}")
        if food == "deep fried chicken":
            raise RuntimeError("Health Warning!")
        print(f"Taking {food}")

    def close(self):
        print("Closing the door")



def raid(food):
    with closing (RaidRefridgerator()) as r:
        r.open()
        r.take_food(food)

raid("test")
raid("deep fried chicken")
