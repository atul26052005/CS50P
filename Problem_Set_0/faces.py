def convert(str):
    return str.replace(":)", "🙂").replace(":(", "🙁")

def main():
    str = input()
    print(convert(str))

if __name__ == "__main__":
    main()