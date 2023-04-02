
# ------------------------------------------------
# File Name: Set_Operations.py
# ------------------------------------------------
# Date Finished: 07-12-2022
# ------------------------------------------------
# Description:
# This is a set operation calculator that 
# takes the union, intersection, difference,
# & symmetric difference of two sets.  
# ------------------------------------------------

import sys

print("\n---------------- Set Operations Calculator ----------------")

def menu_options():
    print("\nSelect an operation to perform:\n",
          "1 - Union (∪)\n",
          "2 - Intersection (∩)\n",
          "3 - Difference (-)\n",
          "4 - Symmetric Difference (∆)\n",
          "5 - Exit/Terminate program\n")


def menu_input():
    while True:
        try:
            menu_input.menu_choice = int(input("Enter choice: "))
            
            if menu_input.menu_choice < 1:
                print("Invalid choice! Try again.\n")
            
            elif menu_input.menu_choice > 5:
                print("Invalid choice! Try again.\n")
            
            else:
                break
        except:
            print("Invalid choice! Try again.\n")


separator = "-----------------------------------------------------------"


def element_input():
    
    print(separator)
    
    setA_1 = input("Enter 1st element of set A: ")  # 1st element of set A
    setA_2 = input("Enter 2nd element of set A: ")  # 2nd element of set A
    setA_3 = input("Enter 3rd element of set A: ")  # 3rd element of set A
    setA_4 = input("Enter 4th element of set A: ")  # 4th element of set A
    setA_5 = input("Enter 5th element of set A: ")  # 5th element of set A
    print("\r")
    setB_1 = input("Enter 1st element of set B: ")  # 1st element of set B
    setB_2 = input("Enter 2nd element of set B: ")  # 2nd element of set B
    setB_3 = input("Enter 3rd element of set B: ")  # 3rd element of set B
    setB_4 = input("Enter 4th element of set B: ")  # 4th element of set B
    setB_5 = input("Enter 5th element of set B: ")  # 5th element of set B
            
    print(separator)
    element_input.set_A = {setA_1, setA_2, setA_3, setA_4, setA_5}    # Set A
    element_input.set_B = {setB_1, setB_2, setB_3, setB_4, setB_5}    # Set B

    print("\nSets:\n",
          "A = ", element_input.set_A,
          "\nB = ", element_input.set_B, sep="")


def calculation():
    
    menu_options()
    menu_input()

    if menu_input.menu_choice == 1:
        element_input()
        
        print("\nUnion:\nA ∪ B =",
              element_input.set_A | element_input.set_B, "\n") # Calculates the union of set A & B
        
        print(separator, "\n")
        calculation()
            
    elif menu_input.menu_choice == 2:
        element_input()
        
        print("\nIntersection:\nA ∩ B =",
              element_input.set_A & element_input.set_B, "\n") # Calculates the intersection of set A & B
        
        print(separator, "\n")
        calculation()

    elif menu_input.menu_choice == 3:
        element_input()
        
        print("\nDifference:\nA - B =",
              element_input.set_A - element_input.set_B, "\n") # Calculates the difference of set A & B
        
        print(separator, "\n")
        calculation()

    elif menu_input.menu_choice == 4:
        element_input()
        
        print("\nSymmetric Difference:\nA ∆ B =",
              element_input.set_A ^ element_input.set_B, "\n") # Calculates the symmetric difference of set A & B
        
        print(separator, "\n")
        calculation()

    elif menu_input.menu_choice == 5:
        print(separator)
        sys.exit("Program terminated!\n")

calculation()

