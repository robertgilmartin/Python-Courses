from random import choice

#  EL juego del ahorcado!!

# Crear lista de palabras

lifes = 6
winner = False
lol_champions = ['Ahri', 'Yasuo', 'Jinx', 'Lee Sin', 'Zed', 'Ashe', 'Darius', 'Lux', 'Garen', 'Ekko']
print("Hello Summoner!! Let's guess the League of Legends champion!! Good Luck :D")


# Choice method to select a random word from the list
def choose_a_word_from_the_list(champion_list):
    return choice(champion_list)


# Method to show the user the number of the letters as a '-' symbol
def hide_word(word_list):
    hidden_word_list = []
    for i in word_list:
        hidden_word_list.append('-')
    return hidden_word_list


# Method to input a valid letter by the user (Play in lower cases, if it's in upper use the method lower())
def input_letter():
    return input("Guess the letter: ").lower()


# Method to show the right letter in the hidden word
def show_letter_in_word(index_list, letter, letter_list):
    for index in index_list:
        letter_list[index] = letter
    return letter_list


def letter_index_in_the_word(word_list, letter):
    index_list = []
    for character in word_list:
        current_index = word_list.index(character)
        if character == letter:
            index_list.append(current_index)
            word_list[current_index] = ''
        else:
            pass
    return index_list


# Method to check if is_dead
def is_dead(lifes, word):
    if lifes == 0:
        print(f"You have {lifes} lifes!! You have lost the game. The LoL champion was {word}!!")
    else:
        print(f"You still alive with {lifes} lifes.")


# Method to check if player has_won
def has_won(word_list, word):
    if '-' not in word_list:
        print(f"CONGRATULATIONS!!! The champion is {word}!!")
        return True
    else:
        return False


word = choose_a_word_from_the_list(lol_champions).lower()
init_word_list = list(word)
# print(word)

updated_word = hide_word(init_word_list)
# print(updated_word)

while lifes > 0 and winner == False:

    print(f"Hidden champion:\n{updated_word}")
    possible_letter = input_letter()

    if possible_letter in word and possible_letter not in updated_word:
        print(f"\nCORRECT! The letter '{possible_letter}' is in our champion.\nYou still having {lifes} lifes btw.")
        index_list = letter_index_in_the_word(init_word_list, possible_letter)
        # print(index_list)

        updated_word = show_letter_in_word(index_list, possible_letter, updated_word)

        winner = has_won(updated_word, word)
        # print(winner)

    elif possible_letter in word and possible_letter in updated_word:
        print(f"\nYou have repeated the letter '{possible_letter}'!! I'll discount you a life btw MUAHAHA!!")
        lifes -= 1
        is_dead(lifes, word)

    else:
        print(f"\nThe letter '{possible_letter}' is not in our champion!!")
        lifes -= 1
        is_dead(lifes, word)
