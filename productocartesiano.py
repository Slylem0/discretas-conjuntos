def message():
    a ="""________________________________________
    Welcome again to do the product cartesian,
      write the information solicitaded.
      pls i want to sleep, only same cuantify of 
      elements in set 1 and set 2, i dont know nothing
      about Python because toro didnt taught that.
      discretas is the best assignament. 
    _______________________________________________"""
    return a
#THIS IS A 5 IN MY GRADE IN DISCRETAS
def sets():
    set1 = set()
    set2 = set()

    cset1 = int(input("cuantify of values of set 1: "))
    for i in range(cset1):
        b = input(f"write the {i+1} value: ")
        set1.add(b)

    print("___________________________________________________")
    cset2 = int(input("cuantify of values of set 2: "))
    for i in range(cset2):
        b = input(f"write the {i+1} value: ")
        set2.add(b)

    # Now that we have the sets, we're going to organize the letters
    set1list = []
    for i in set1:
        indice = 0
        while indice < len(set1list) and i > set1list[indice]:
            indice += 1
        set1list.insert(indice, i)

    set2list = []
    for i in set2:
        indice = 0
        while indice < len(set2list) and i > set2list[indice]:
            indice += 1
        set2list.insert(indice, i)

    l = len(set1list)
    p = len(set2list)

    high_numer = max(l, p)
    answer = []

    for i in range(high_numer):
        if i < len(set1list) and i < len(set2list):
            answer.append((set1list[i], set2list[i]))    #pls only same dates un the two sets :(, i want to sleep

    print(answer)

if __name__ == "__main__":
    print (message())
    sets()
