import random

def hangman():
    words = ["python", "hangman", "challenge", "programming", "openai"]
    word = random.choice(words)
    guessed_word = ["_"] * len(word)
    attempts = 6
    guessed_letters = set()

    print("Let's play Hangman!")

    while attempts > 0:
        print("\nWord: " + " ".join(guessed_word))
        print(f"Guessed Letters: {', '.join(sorted(guessed_letters))}")
        print(f"Attempts Left: {attempts}")
        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess in word:
            for idx, char in enumerate(word):
                if char == guess:
                    guessed_word[idx] = guess
            if "_" not in guessed_word:
                print("\nCongratulations! You guessed the word: " + word)
                break
        else:
            attempts -= 1
            print(f"Wrong guess! '{guess}' is not in the word.")

    if "_" in guessed_word:
        print("\nGame Over! The word was: " + word)

hangman()
