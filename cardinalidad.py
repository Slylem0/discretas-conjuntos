def message():
    a = """___________________________________________________
    Now this part is the cardinality of this program
________________________________________________"""
    return a

def sets():
    global set1, set2
    set2 = {1, 2, (3,5,6,(3,4)), (6), 8, (9,23), 2, (5,9)}      #this example its declarated by us, u can modificated and played with it 
    a = int(input("write the number of elements you want to introduce in set A: "))
    set1 = set()                        #if u want u can modificated this to do values thaht u want 

    for i in range(a):
        b = input(f"write the element {i+1}: ")
        set1.add(b)

def counter ():
    contador1 = 0
    contador2 = 0

    for i in set1:
        contador1 += 1 

    for i in set2:  
        contador2 += 1

    a = (f"the exmaple thaht u can modoficated is {contador2}, and the user information is {contador1}")
    return a

if __name__ == "__main__":
    print (message())
    sets()
    print (counter())
    