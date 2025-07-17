print("my calculator".upper())
try:
    a = int(input("Enter a Number: "))
    b = int(input("Enter a Number: "))

    print("The (+) is addition of two number\nThe (-) is Subtraction of number\n" \
    "The (*) is Multiply of two number\nThe (/) is devision of two number")

    O = input("Enter your operation: ")

    match O:
        case "+":
            print(f"The result is {a+b}")
        case "-":
            print(f"The result is {a-b}")
        case "*":
            print(f"The result is {a*b}")
        case "/":
            print(f"The result is {a/b}")

    
except Exception as e:
    print("Enter a valid value of a & b")