try:
    number1, number2 = input("Enter two numbers: ").split()
    result = float(number1) / float(number2)
    print("You Entered:", result)
except ValueError:
    print("Invalid numbers entry, Please enter a valid entry numbers (must be a number)")