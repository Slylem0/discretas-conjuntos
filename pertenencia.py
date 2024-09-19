def welcome():
    a = """________________________________________________________
    Welocome to the second part of this amazing proyect, this 
    part have the belonging of the sets :)
    ____________________________________________________________"""
    return a

def sets(): #define the sets and te elements thahr can be in there
    global set1
    a = int(input("write the number of elements you want to introduce in set A: "))
    set1 = set()

    for i in range(a):
        b = input(f"write the element {i+1}: ")
        set1.add(b)
    
def belonging():
    print ("_____________________________________")
    while True:                                                 #cicle while true to do a infinite cicle untild the user exit
        option = int(input("1. to search\n2. to leave\n"))

        if option == 1:
            search = input("write to search: ")

            for i in set1:
                if i == search:
                    print ("True")
                    break
            else:
                print (False)        
        else:
            break
    
    print ("goodbay")

if __name__ == "__main__": #entrypoint
    print (welcome())
    sets()
    belonging()