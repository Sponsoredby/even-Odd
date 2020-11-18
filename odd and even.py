print ("Welcome to even and odd checker v 0.1a")
x = input ("please enter a number: ")
x = int (x)

#create a function here

if x%2 == 0:
    print ('\n',x, "is an even number")
else:
    print ('\n',x, "is an odd number")

if x == int(x):
    print("\nEnter another number to try again or enter q to quit:")


#exit - maybe once time has been learned make it so if no input is entered after set period then the program auto exits
#a simple even and odd number checker taken from py4e
# i added user input and converted string to interger
#deliberate bugs number can be non numerical and program doesnt loop
