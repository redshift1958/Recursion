


#### Recursion

#def RecursionSum(number):

def RecursionMethod(number):
    if number == 1:
        return 1
    else:
        Sum = number + RecursionMethod(number - 1)
        return Sum

    


#### Loop method

def LoopMethod(number):
    Sum = 0
    for i in range(number+1):
        Sum = Sum+i
    return Sum
        
        


# A program to show the two ways of calculating a sum using recursion and loops



# main

number = 1
while number != 0:
    inputnumber = int(input("\n\n What is the number you would like summed?"))
    print("\n ",LoopMethod(inputnumber))
    print(" ",RecursionMethod(inputnumber))
 

    











