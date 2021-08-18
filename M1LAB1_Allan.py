"""
CSC 221
M1LAB1 - Double a Number
Lord Jenar Adolph C Allan
8/18/2021
"""
results = []

def main():
    """Main Loop of program."""
    #print("Program goes here")
    print("This is the double a number program")
    #TODP This should loop
    keepgoing = 0
    val = 0
    
    while keepgoing == 0:
        collectNums()
        keepgoing = rep(val)
    print("Bye!")
    print()
    itera = len(results)
    itera = int(itera / 2)
    
    index1 = 0
    index2 = 1
    for x in range(itera):
        print(f'Number {results[index1]}. is doubled to {results[index2]}.')
        index1+=2
        index2+=2
    
def collectNums():
    num = int(input("Enter a number: "))
    dbl = doubleAnumber(num)
    print()
    print("A doubled ",num,"is:",dbl)
    results.append(num)
    results.append(dbl)
    

def doubleAnumber(num):
    """input : one number
    output. the number * 2."""
    #return 0 # TODO make this actually work
    result = num * 2
    return result

def rep(val):
    while val == 0:
        print("1. Enter another number")
        print("2. Exit")
        select = int(input("Enter your choice: "))
        if select == 1:
            val += 1
            return (0)
        elif select == 2:
            val += 1
            return (1)
        else:
            print("Invalid input.")
        

    
    


if __name__ == "__main__":
    main()
