def message():
    a = """-----------------------------------------
    Welcome to Guacacho Sets
-----------------------------------------\n
Please be conscious and do not make my life harder than discretas 1 with
sets with more than 4 elements please, take it easy Teacher Toro,
we worked so hard but Toro in imperativa does not taught that.\n
"""
    return a


def sets():
    global set1
    a = int(input("How many elements do you want in your set: "))
    set1 = set()

    for i in range(a):
        b = input(f"write the element {i+1}: ")
        set1.add(b)


def counter():
    global contador1
    contador1 = 0

    for i in set1:
        contador1 += 1

    a = (f"The quantity of elemntens in the set is {contador1}")
    return a


# Until here we got the program for cardinality
# Now we gonna make the program to know how many subsets
# we can get from the set

def pow_set():
    total_subsets = 2**contador1
    return total_subsets


def subsets():
    global finalsubsets
    finalsubsets = set()
    listset = ["∅", set1]

    a = """
I told you to not use more than 5 elements, now you have to do it all again,
because it is to hard to do it with 5 elements, even 4 were so hard, so please
make this task as a 5 in my grades. Thanks teacher Toro.
    """

    if not contador1 == 1:
        for i in set1:
            listset.append(i)

    if contador1 == 2:
        return listset
    elif contador1 == 3:
        listset.append({listset[2], listset[3]})
        listset.append({listset[2], listset[4]})
        listset.append({listset[3], listset[4]})
    elif contador1 == 4:
        listset.append({listset[2], listset[3]})
        listset.append({listset[2], listset[4]})
        listset.append({listset[2], listset[5]})
        listset.append({listset[3], listset[4]})
        listset.append({listset[3], listset[5]})
        listset.append({listset[4], listset[5]})
        listset.append({listset[2], listset[3], listset[4]})
        listset.append({listset[2], listset[3], listset[5]})
        listset.append({listset[2], listset[4], listset[5]})
        listset.append({listset[3], listset[4], listset[5]})
    else:
        return a

    return listset


if __name__ == "__main__":
    print(message())
    sets()
    counter()
    print(subsets())