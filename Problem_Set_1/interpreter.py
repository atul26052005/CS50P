expression = input("Expression: ")

if "+" in expression:
    a, b = expression.split("+")
    print(float(int(a) + int(b)))

elif "-" in expression:
    a, b = expression.split("-")
    print(float(int(a) - int(b)))

elif "*" in expression:
    a, b = expression.split("*")
    print(float(int(a) * int(b)))

elif "/" in expression:
    a, b = expression.split("/")
    print(float(int(a) / int(b)))