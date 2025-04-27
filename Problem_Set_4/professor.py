import random

def main():
    level = get_level()
    score = 0
    problem_Round = 0

    while problem_Round < 10:
        x = generate_integer(level)
        y = generate_integer(level)
        answer = 0
        answer_Round = 0

        while  answer_Round < 3:
            try:
                print(f"{x} + {y} = ", end = " ")
                answer = int(input())
                if answer != x + y:
                    print("EEE")
                    answer_Round += 1
                    continue
                break
            except ValueError:
                answer_Round += 1
                print("EEE")
                continue
            answer_Round += 1
        
        if x + y == answer:
            score += 1
        elif answer_Round == 3 and x + y != answer:
            print(f"{x} + {y} = {x + y}")
        
        problem_Round += 1
    
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level <= 0 or level > 3:
                continue
            return level
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()