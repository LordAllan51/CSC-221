"""
CSC 221
M1LAB1 - Double a Number
Lord Jenar Adolph C Allan
8/18/2021
"""

def main():
    """Main Loop of program."""
    #print("Program goes here")
    print("This is the double a number program")
    num = int(input("Enter a number: "))
    dbl = doubleAnumber(num)
    print(num,"doubled is:",dbl)
    
    
def doubleAnumber(num):
    """input : one number
    output. the number * 2."""
    #return 0 # TODO make this actually work
    result = num * 2
    return result

if __name__ == "__main__":
    main()