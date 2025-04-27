def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or not s[0:2].isalpha():
        return False

    if len(s) < 2 or len(s) > 6:
        return False

    found_number = False
    for char in s:
        if char.isdigit():
            if char == '0' and not found_number:
                return False
            found_number = True
        elif found_number:
            return False

    if not s.isalnum():
        return False

    return True


main()
