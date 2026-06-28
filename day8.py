try :

    number1 = int(input("Enter first number:"))
    number2 = int(input("Enter second number:"))
    operation = input("Enter operation (+,-,*,/):")

    if operation =="+":
        print(number1 + number2)
    elif operation =="-":
        print(number1 - number2)
    elif operation =="*":
        print(number1 * number2)
    elif operation == "/":
        print(number1 / number2)

except ZeroDivisionError:
    print("you cant multiply this number")
except ValueError:
    print("thats not a number")
finally:
    print("calculation Complete")




