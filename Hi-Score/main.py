import random

def game():
    print("you are playing this game")

    score = random.randint(1,64)

    with open("./Hi-Score/Hi-Score.txt") as f:
        highScore = f.read()
        if(highScore != ""):
            highScore = int(highScore)
        else:
            highScore = 0
    print(f"your score is {score}")

    if(score > highScore):
        with open("./Hi-Score/Hi-Score.txt", "w") as f:
            f.write(str(score))

    return score


game()