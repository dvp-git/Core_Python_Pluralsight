# Demonstrating the use of type "set"

"""
        Union: A or B            a.union(b) == b.union(a)
        Difference: A - B        a.difference != b.difference(a)
        Symmetric Difference: A and B but not A intersection B   a.symmetric_difference(b) == b.symmetric_difference(a)
        Intersection: A and B a.intersection(b) == b.intersection(a)

        Predicate methods:
        Subset: A belongs to B : issubset
        Superset: B belongs to A : issuperset
        Disjoint: Part of A that does not belong to B : isdisjoint

"""
blue_eyes = {'Olivia','Harry','Lily','Jack','Amelia'}
blond_hair = {'Harry','Jack','Amelia','Mia','Joshua'}
smell_hcn = {'Harry','Amelia'}
taste_pcn = {'Harry','Lily','Amelia','Lola'}
o_blood = {'Mia','Joshua','Lily','Olivia'}
b_blood = {'Amelia','Jack'}
a_blood = {'Harry'}
ab_blood = {'Joshua','Lola'}

print("Here are the sets: ")
print(f"blue_eyes : {blue_eyes}\n")
print(f"blond_hair : {blond_hair}\n")
print(f"smell_hcn : {smell_hcn}\n")
print(f"taste_pcn  : {taste_pcn}\n")
print(f"o_blood : {o_blood}\n")
print(f"b_blood : {b_blood}\n")
print(f"ab_blood : {ab_blood}\n")


print("============== Demonstrating Set operations =======================")
print(f"People who have either blond hair or blue eyes : {blond_hair.union(blue_eyes)}\n")

print(f"People who have both blond hair and blue eyes : blond_hair.intersection(blue_eyes) : {blond_hair.intersection(blue_eyes)}\n")

print(f"People who have  blond hair but no blue eyes : blond_hair.difference(blue_eyes) : {blond_hair.difference(blue_eyes)}\n")

print(f"People who have  blue eyes but no blond hair : blue_eyes.difference(blond_hair) : {blue_eyes.difference(blond_hair)}\n")

print(f"People who have exclusively blue eyes or no blond hair : blue_eyes.symmetric_difference(blond_hair) : {blue_eyes.symmetric_difference(blond_hair)}\n")


print(f"Check all people who smell_hcn also have blond hair {smell_hcn.issubset(blond_hair)}")

print(f"Check all people who can taste_pcn can also smell_hcn {taste_pcn.issuperset(smell_hcn)}")

print(f"Test for blood group: {o_blood.isdisjoint(a_blood)}")
