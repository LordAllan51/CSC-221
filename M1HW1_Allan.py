# CSC 221
# M1HW1 - Arrat Creation and Manipulations
# Lord Jenar Adolph C Allan
# 8/18/2021

def DisplayMenu():
    print("MENU")
    print("_____________")
    print("1)	Create a 3-by-3 Array")
    print("2)	Display cube Values for elements in array")
    print("3)	Add 7 to every element and display result")
    print("4)	Multiply elements by 6 and display result")
    print("5)	Exit")


def mainMenu():
    ''' This menu function is formatted to prevent error '''
    loop = '1'
    while loop == '1':
        DisplayMenu()
        selection = input("Enter your choice: ")
        if selection == '1':
            print()

            
        elif selection == '2':
            print()

            
        elif selection == '3':
            print()

            
        elif selection == '4':
            print()

            
        elif selection == '5':
            print()
            loop = '2'
            print()
            print("Bye!")
            ##raise SystemExit(0)#exit feature for spyder#REMOVED
        else:
            print()
            print("Invalid input/choice. Choose within 1-4")
        
if __name__ == "__main__":
    mainMenu()