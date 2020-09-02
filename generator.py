from sys import argv 
import operator
script, maxNumber, filename = argv

#Make input an int
maxNumber = int(maxNumber) + 1

#Open file to make the program
calculator = open(filename, 'w')

#Setup the other document
calculator.write("firstNumber = 0")
calculator.write("\nsecondNumber = 0")
calculator.write("\nmaxNumber = " +str(maxNumber-1)) 
calculator.write("\n\nprint(\"Welcome to my calculator :) You can add, multiply and divide up to \" + str(maxNumber))")
calculator.write("\nfirstNumber = int(input(\"Please enter your first number: \"))")
calculator.write("\noperator = input(\"Please enter the operator, which can be +, * and /: \")")
calculator.write("\nprint(\"Please remember, if you took / you cannot divide by 0!\")")
calculator.write("\nsecondNumber = int(input(\"Please enter your second number: \"))\n")
#From 0 to the max number
def Loop (operation, symbol):
    #In case of divisions
    minimum = 0
    if (symbol == "/"):
        minimum = 1
    #The actual magic, line 30 is the if statement, line 31 the print statement and calculations
    for i in range(0, maxNumber):
        print("Iteration #%2d" % (i) )
        for j in range(minimum, maxNumber):
            calculator.write("\nif (firstNumber == " + str(i) + " and secondNumber == " + str(j) + " and operator == \"" + symbol + "\"):")
            calculator.write("\n    print(\"" + str(i) + " " + symbol + " " + str(j) + " is " + str(operation(i, j)) + "\")")

#Additions, multiplications and divisions
Loop(operator.add, "+")
Loop(operator.mul, "*")
Loop(operator.truediv, "/")
#End line, input to wait for the end so you can see the answer
calculator.write("\nprint(\"If you didn't get your number, please try with valid ones! Thank you for using my calculator :)\")\ninput()")

calculator.close()