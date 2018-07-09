def calculate(str, first, second):
    if str.upper() == "ADD":
        return first + second
    elif str.upper() == "SUBTRACT":
        return first - second
    elif str.upper() == "MULTIPLY":
        return first * second
    elif str.upper() == "DIVIDE":
        return first / second
    else:
        print("Operation not found")
        
print(calculate("multiply",10,10))