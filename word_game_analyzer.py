
import random
import string


def word_game():
    words = ["python", "computer", "programming", "keyboard", "internet"]

    secret_word = random.choice(words)
    attempts = 5
    score = 0

    print("\n--- Word Guessing Game ---")
    print("Guess the correct word!")
    print("You have 5 attempts.")

    while attempts > 0:
        guess = input("Enter your guess: ").lower().strip()

        if guess == secret_word:
            score = 10
            print("Correct! You won.")
            break
        else:
            attempts -= 1
            print("Wrong guess!")
            print("Attempts left:", attempts)

    if attempts == 0:
        print("Game over!")
        print("Correct word was:", secret_word)

    print("Your score:", score)


def word_frequency():
    print("\n--- Word Frequency Analyzer ---")

    try:
        with open("sample.txt", "r", encoding="utf-8") as file:
            text = file.read().lower()

        for symbol in string.punctuation:
            text = text.replace(symbol, "")

        words = text.split()
        frequency = {}

        for word in words:
            frequency[word] = frequency.get(word, 0) + 1

        sorted_words = sorted(
            frequency.items(),
            key=lambda item: item[1],
            reverse=True
        )

        print("\nWord Frequency:")
        for word, count in sorted_words:
            print(word, ":", count)

    except FileNotFoundError:
        print("Error: sample.txt file not found!")

    except OSError:
        print("Unable to read the file.")


while True:
    print("\n===== Python Project =====")
    print("1. Word Guessing Game")
    print("2. Word Frequency Analyzer")
    print("3. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            word_game()
        elif choice == 2:
            word_frequency()
        elif choice == 3:
            print("Thank you!")
            break
        else:
            print("Invalid choice!")

    except ValueError:
        print("Please enter a valid number!")
