def welcome():
    a = """______________________________________________________
    welcome to this 1rst art of this proyect in 
    this part we gonna work subconjuntos
    ____________________________________________________________"""
    return a

def conjuntos():
    a = int(input("write the number of elements you want to introduce in set A: "))
    set1 = set()

    for i in range(a):
        b = input(f"write the element {i+1}: ")
        set1.add(b)

    print ("__________________________________________________")
    c= int(input("write the number of elements of set B: "))
    print ("___________________________________________________")
    set2 = set()

    for i in range(c):
        b = input(f"write the elemnt {i+1}: ")
        set2.add(b)

    lenset1 = len(set1)
    lenset2 = len(set2)
    print ("________________________________________")

    #A ⊆ B
    print("now we gonna start with A ⊆ B")
    if lenset1 <= lenset2:
        if set2.issuperset(set1): #using issuperset to check if set1 is in set2
            print (True)
    else:
        print (False)
    print ("____________________________________")

    #A ⊂ B
    print ("now we gonna do with A ⊂ B")
    if lenset1 < lenset2:
        if set2.issuperset(set1): #using issuperset to check if set1 is in set2
            print (True)
    else:
        print (False)
    print ("____________________________________")

    #A -⊂ B 
    print ("now we gonna do with A -⊂ B")
    if lenset1 >= lenset2:
        if set2.issuperset(set1): #using issuperset to check if set1 is in set2
            print (True)
        else:
            print (False)
    else:
        print (False)
    print ("____________________________________")

if __name__ == "__main__":
    print (welcome())
    conjuntos()

