while True:
    try:
        fraction = input("Fraction: ")
        x, y = fraction.split('/')
        x = int(x)
        y = int(y)

        if y == 0:continue

        if x > y:continue

        percentage = (x / y) * 100

        if percentage <= 1:
            print("E")
        elif percentage > 1 and percentage <= 25:
            print(f"{int(round(percentage))}%")
        elif percentage > 25 and percentage <= 50:
            print(f"{int(round(percentage))}%")
        elif percentage > 50 and percentage <= 75:
            print(f"{int(round(percentage))}%")
        elif percentage >= 99:
            print("F")
        else:
            print(f"{int(round(percentage))}%")

        break
    except ValueError:
        print("Error: Invalid input. Please enter integers for X and Y. Try again.")
    except ZeroDivisionError:
        print("Error: Denominator cannot be zero. Try again.")