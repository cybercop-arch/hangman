import random
#create a greeting
print("Welcome to Hangman!")
#create your word list
words = ["apple","banana","cherry","strawberry","mango"]
#randomly choose a word from the list  you have created
secret_word = random.choice(words)
print("you have 5 guesses.")
#create a empty list
display_word = []
for letter in secret_word:
    display_word += "_"
print(display_word)
num = 0
game_over = False
while not game_over:
    guess = input("enter a letter:").lower()
    for position in range(len(secret_word)):
        letter = secret_word[position]
        if letter == guess:
            display_word[position] = letter
    if guess not in secret_word:
        num += 1
        guesses_left = 5 - num
        print(f"you have {guesses_left} guesses left")
        if num >= 5:
            print("you loser")
            game_over = True
    print(display_word)
    if "_" not in display_word:
        print("you WIN!")
        game_over = True
