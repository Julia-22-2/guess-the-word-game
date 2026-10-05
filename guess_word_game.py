import random

# list of valid words
words_list = []

def word_game(file_name):
    # load possible answers list
    load_words(file_name)                                       # load words list from txt file

    word_choice = random.randint(0, (len(words_list) - 1))  
    answer = words_list[word_choice].upper()                    # answer

    counter = 0                                                 # no. of guesses

    while counter < 6:
        counter += 1                                            # adds 1 to no. of guesses

        while True:                                             # make guess
            guess = input("Your Guess: ").upper()

            if guess.lower() in words_list:                     # only allows valid words
                break

        if guess == answer:
            print(f"\nYou guessed the word in {counter}!\n")
            break
        elif counter == 6 and guess != answer:
            print(f"\nYou lost!\nThe answer was {answer}\n"
                  "Better luck next time!\n")
        elif guess != answer:
            answer_let_nums = {}                                # no. of each letter in answer
            guess_let_nums = {}                                 # no. of each letter in guess

            # append no. of each letter in guess/answer
            append_letters(answer, answer_let_nums)
            append_letters(guess, guess_let_nums)

            # checks letter correctness
            result = check_letters(guess, answer, answer_let_nums, guess_let_nums)

            # print results
            print(f"\n{guess}\n{result}\n")

def check_letters(guess, answer, answer_let_nums, guess_let_nums, result = ""):
    position = 0

    for letter in guess:
        if letter == answer[position]:
            result += "G"
            minus_letter_count(letter, answer_let_nums, guess_let_nums)
        elif letter in answer:
            if answer_let_nums[letter] >= guess_let_nums[letter]:
                result += "Y"
                minus_letter_count(letter, answer_let_nums, guess_let_nums)
            else:
                result += "X"
        else:
            result += "X"
        position += 1

    return result

def minus_letter_count(letter, answer_let_nums, guess_let_nums):
    answer_let_nums[letter] -= 1
    guess_let_nums[letter] -= 1

def load_words(file_name):
    with open(f"{file_name}") as infile:
        for line in infile:
            word = line.strip()
            words_list.append(word)

def append_letters(word, letter_nums):
    for letter in word:
        if letter in letter_nums:                               # checks no. of each letter in guess/answer
            letter_nums[letter] += 1
        else:
            letter_nums[letter] = 1

def game_menu():
    while True:
        print("Do you want to play?\n---------------------\nPress 'R' for rules\n" \
              "Press 'Y' to play\nPress 'N' to quit")
        
        choice = input("Option Selected: ").upper()

        if choice == "R":
            print("--------------------\nYou must guess the word in 6 guesses\n\nThe answer is STARE\n\n" \
                  "Your Guess: FLANK\n\n" \
                  "Result: XXGXX\nThe 'X' means letter isn't in the word\nThe 'G' means the letter is in the correct spot\n\n" \
                  "Your Guess: BEARD\n\nResult: XYGGX\n" \
                  "The 'Y' means the letter is in the word but in the incorrect spot")
        elif choice == "Y":
            word_game("five_letter_words.txt")
        elif choice == "N":
            print("\nThank you for playing!")
            exit()
        
game_menu()