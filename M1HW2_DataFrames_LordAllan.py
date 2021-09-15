# This program exercises your comprehension of pandas dataframe manipualtions
# 8/20/2021
# CSC221 M1HW2 – DataFrame 
# Lord Jenar Adolph C Allan
import pandas as pd

"""
To create a Data Frame you need to create a dictionary and use the pandas
dataframe to format it to the dataframe type to start.
Next is custom index within the creation of dataframe to rename the default
0-9 index when creating it without specifying its name.
Next is usage of selecting a specific row, column, multiple rows and columns.
Lastly is to show the methods of describing, sorting and transposing a 
dataframe.
"""

def mainDataFrame():
    thisdict = {#step A start of dictionary
      "Maxine": [88.6,  96.9, 86.2],
      "James": [94.6, 100.9, 89.2],
      "Amanda": [90.9,  95.9, 85.2]
    }
    #Step A & B with custom indices
    temperatures = pd.DataFrame(thisdict, index = ["Morning"
                                                 , "Afternoon"
                                                 , "Evening"])
    temp=temperatures
    print("Temperatures Dataframe\n--------------\n",temp)
    
    #Step C, D, E, F, and G all combined in a menu style
    #selecting from temperatures dataframe
    loop = '0'
    print("\nChoose from temp data 1)Maxine, 2)Morning, 3)Morning and Evening",
          ", 4)Amanda and Maxine, 5) for temp readings.")
    while loop == '0':
        selection = input("Enter your choice (Exit is choice 6):")
        if selection == '1':
            print()
            col_A = temp.Maxine
            print('Selected Column\n---------------\n',col_A,sep='')
        elif selection == '2':
            print()
            row_A = temp.loc["Morning"]
            print('Selected Row\n---------------\n',row_A,sep='')
        elif selection == '3':
            print()
            row_B = temp.loc[["Morning","Evening"]]
            print('Selected Row\n---------------\n',row_B,sep='')
        elif selection == '4':
            print()
            col_B = temp.iloc[[0,2],[0,1,2]]#1st and 3 rows and 1st and 3 col
            print('Selected Columns\n---------------\n',col_B,sep='')
        elif selection == '5':
            print()
            elm_A = temp.iloc[[0,1],[0,2]]#1st and 2rd rows 
            #& 1st and 3nd col
            print('Selected Column\n---------------\n',elm_A,sep='')
        elif selection == '6':
            loop = '2'
            print()
            print("Exiting Menu...")
            ##raise SystemExit(0)#exit feature for spyder#REMOVED
        else:
            print("Invalid input/choice. Choose within 1-5")
        print()
    
    #Step H
    print('\nDescribing method\n---------------\n',temp.describe(),sep='')
    #Step I
    print('\nTransposing method\n---------------\n',temp.transpose(),sep='')
    #Step J
    alphabetic_temp = temp[sorted(temp.columns)]
    print('\nSorting method\n---------------\n',alphabetic_temp,sep='')
    

if __name__ == "__main__":
    mainDataFrame()