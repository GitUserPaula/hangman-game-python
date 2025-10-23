import random

words = ["tiger", "zebra", "giraffe", "lion"]
guess_word = random.choice(words)
guessed_letters = []
max_attempts = 6
attempts = 0
display_word = ["_"] * len(guess_word)

print("Welcome to Hangman!")
print(f"The word has {len(guess_word)} letters")
print(f"Hint: The first letter is '{guess_word[0]}'")
print(guess_word[0] + " " + " ".join("_" for _ in guess_word[1:]))
#print(" ".join(display_word)) 

while attempts < max_attempts:
    print(f"Letters already guessed: {', '.join(guessed_letters)}")
    guess = input("Please enter a letter:").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter. Try a new one.")
        continue
    print(" ".join(display_word))
    guessed_letters.append(guess)

    if guess in guess_word:
        print("Good guess!")

        for i in range(len(guess_word)):
                if guess_word[i] == guess:
                    display_word[i] = guess 
                if "_" not in display_word:
                    print(f"\n¡CONGRATULATIONS! You won! The word was: {guess_word.upper()}")
                    break
    else:
        attempts += 1
        print(f"Wrong guess! You have {max_attempts - attempts} attempts left.")
       


if attempts == max_attempts and "_" in display_word:
    print(f"\nGAME OVER! You ran out of attempts. The word was: {guess_word.upper()}")