import random
import sys
import select
import time

class TimeoutExpired(Exception):
    pass

def input_with_timeout(prompt, timeout):
    sys.stdout.write(prompt)
    print()
    sys.stdout.flush()
    ready, _, _ = select.select([sys.stdin], [],[], timeout)
    if ready:
        return sys.stdin.readline().rstrip('\n') # expect stdin to be line-buffered
    raise TimeoutExpired



letters = {
    "a": "alpha",
    "b": "bravo",
    "c": "charlie",
    "d": "delta",
    "e": "echo",
    "f": "foxtrot",
    "g": "golf",
    "h": "hotel",
    "i": "india",
    "j": "juliet",
    "k": "kilo",
    "l": "lima",
    "m": "mike",
    "n": "november",
    "o": "oscar",
    "p": "papa",
    "q": "quebec",
    "r": "romeo",
    "s": "sierra",
    "t": "tango",
    "u": "uniform",
    "v": "victor",
    "w": "whiskey",
    "x": "xray",
    "y": "yankee",
    "z": "zulu"
}

def play_game():
    lives = 3
    score = 0
    while lives > 0:
        letter, correct_word = random.choice(list(letters.items()))
        try:
            word = input_with_timeout(letter, 4)
        except TimeoutExpired:
            print("Time's up!")
            lives -= 1
            print("The correct response was", correct_word)
        else:
            if word == correct_word:
                score += 1
                print("You got it! Score =",score)
            else:
                print("That's wrong.")
                lives -= 1
                print("The correct response was", correct_word)
        time.sleep(1.5)
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        
    print("Game over! Your score: ", score)
    time.sleep(1.5)

def main():
    while True:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("The objective of this game is to respond with the phonetic alphabet word")
        play = input("Play game? (Y/n): ").lower()
        if play == 'y' or play == 'yes' or play == '':
            play_game()
        elif play == 'n' or play == 'no':
            break

if __name__ == "__main__":
    main()

