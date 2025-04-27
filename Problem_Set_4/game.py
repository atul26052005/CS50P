import random

def main():
    level = get_level()
    num = random.randint(1, level)
    get_guess(num)

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level <= 0:
                continue
            return level
        except ValueError:
            continue

def get_guess(num):
    while True:
        try:
            guess = int(input("Guess: "))
            if guess <= 0:
                continue
            if guess < num:
                print("Too small!")
            elif guess > num:
                print("Too large!")
            else:
                print("Just right!")
                break
        except ValueError:
            continue

if __name__ == "__main__":
    main()
