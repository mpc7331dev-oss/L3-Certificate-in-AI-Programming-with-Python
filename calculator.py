#Calculator: asks for two numbers and then performs the necessary operations
##Refactorial edit
numbers_needed = []

def machine():

    num1 = float(input("What is your first number? "))
    num2 = float(input("What is your second number? "))
    
    op = input("""Which operator do you want?

add?
subtract?
times?
divide?

""")
    if op == "add":
        return print("The answer is: ",num1+num2)
    elif op == "subtract":
        return print("The answer is: ",num1-num2)
    elif op == "times":
        return print("The answer is: ",num1*num2)
    elif op == "divide":
        try:
            return print("The answer is: ",num1/num2)
        except:
            num2 = 0
            print("You cannot divide by zero!")
    else:
        print("Invalid selection!")
        
machine()
