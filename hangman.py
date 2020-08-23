def print_welcome_screen(MAX_TRIES):
    """A function that print the Welcome Screen.
    :param MAX_TRIES: MAX_TRIES value
    :type MAX_TRIES: int
    :return: print to screen the welcome screen and The number of guesses of the player
    :rtype: None
    """

    HANGMAN_ASCII_ART = """
      _    _                                         
     | |  | |                                        
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |                      
                         |___/"""
    print(HANGMAN_ASCII_ART, '\n', MAX_TRIES)


HANGMAN_PHOTOS = {0: "x-------x", 1: """    x-------x
    |
    |
    |
    |
    |""", 2: """    x-------x
    |       |
    |       0
    |
    |
    |
""", 3: """    x-------x
    |       |
    |       0
    |       |
    |
    |
""", 4: """    x-------x
    |       |
    |       0
    |      /|""""""\\""""""
    |
    |
""", 5: """    x-------x
    |       |
    |       0
    |      /|""""""\\""""""
    |      /
    |
""", 6: """    x-------x
    |       |
    |       0
    |      /|""""""\\""""""
    |      / """"""\\""""""
    |
      """}


def print_hangman(num_of_tries):
    """A function that Show to the player the appropriate position of the hangman on the number of his failed attempts.
    :param num_of_tries: num_of_tries value
    :type num_of_tries: int
    :return: print to screen the appropriate position of the hangman
    :rtype: None
    """
    if int(num_of_tries) == 0:
        print(HANGMAN_PHOTOS[0])
    elif int(num_of_tries) == 1:
        print(HANGMAN_PHOTOS[1])
    elif int(num_of_tries) == 2:
        print(HANGMAN_PHOTOS[2])
    elif int(num_of_tries) == 3:
        print(HANGMAN_PHOTOS[3])
    elif int(num_of_tries) == 4:
        print(HANGMAN_PHOTOS[4])
    elif int(num_of_tries) == 5:
        print(HANGMAN_PHOTOS[5])
    elif int(num_of_tries) == 6:
        print(HANGMAN_PHOTOS[6])


def show_hidden_word(secret_word, old_letters_guessed):
    """A function that returns a string which consists of letters and lower hopes.
    The string shows the letters from the old_letters_guessed list that are in the secret_word string in their
    appropriate position, and the other letters in the string (which the player has not yet guessed) as underlines.
    :param secret_word: secret_word string value
    :param old_letters_guessed: old_letters_guessed character's list value
    :type secret_word: str
    :type old_letters_guessed: list
    :return: print to screen the secret word in the form of underscores.
    :rtype: None
    """
    n = secret_word
    for char in secret_word:
        c_exist = False
        for c in old_letters_guessed:
            if char == c:
                c_exist = True
                n = n.replace(char, c)
                break
        if c_exist == False:
            n = n.replace(char, ' _ ')
    print(n)


def choose_word(file_path, index):
    """A function that accepts as parameters: a string that represents a path to a text file that contains spaced words,
    and an integer that represents the location of a particular word in the file.
    The function returns a word in the position obtained as an argument to the function (index)
    that will be used as the secret word for guessing.
    :param file_path: Path to text file
    :param index: index value
    :type file_path: str value that represents a path to a text file
    :type index: int
    :return: The word from file in the index position, which will be used as the secret word for guessing
    :rtype: str
    """
    with open(file_path, "r") as file:
        text = file.read()
        text = text.split(" ")
        different_words = []
        for w in text:
            if str(w) not in different_words:
                different_words.append(w)
        num_different_words = len(different_words)
        while int(index) > len(text):
            index = (int(index) - len(text))
        secret_word = text[int(index) - 1]
        return secret_word


def check_valid_input(letter_guessed, old_letters_guessed):
    """A Boolean function that receives a character and a list of letters that the user has previously guessed.
    The function checks the validation of the input and whether it is legal to guess this signal
    (i.e., the player has not guessed this signal before) and returns true or false accordingly.
    :param letter_guessed: secret_word string value
    :param old_letters_guessed: old_letters_guessed character's list value
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: boolean value that meaning whether the input is valid or not.
    :rtype: bool
    """
    if (len(letter_guessed) > 1) or (not (letter_guessed.isalpha())) or (
            letter_guessed.lower() in old_letters_guessed or (letter_guessed.upper() in old_letters_guessed)):
        return False
    else:
        return True


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """The function uses the check_valid_input function to know if the character is valid and has not been guessed in
    the past or the character is not valid and / or is already on the guess list.
    If the character is invalid or the character has been guessed before, the function prints the
    character "X" , below it the list of letters that have already been guessed and returns a False.
    If the character is valid and has not been guessed before - the function adds the character to the guess list and returns true.
    :param letter_guessed: secret_word string value
    :param old_letters_guessed: old_letters_guessed character's list value
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: boolean value that meaning whether the character is valid and has not been guessed before.
    :rtype: bool
    """
    if not check_valid_input(letter_guessed, old_letters_guessed):
        print('X')
        old_letters_guessed.sort()
        s = " -> "
        print(s.join(old_letters_guessed))
        return False
    else:
        old_letters_guessed += letter_guessed.lower()
        return True


def check_win(secret_word, old_letters_guessed):
    """A Boolean function that checking whether the player won the game.
    i.e., the function returns True if all the letters that make up the secret word are included
    in the list of letters the user guessed. Otherwise, the function returns False
    :param secret_word: secret_word string value
    :param old_letters_guessed: old_letters_guessed character's list value
    :type secret_word: str
    :type old_letters_guessed: list
    :return: boolean value that meaning whether if all the letters that make up the secret word are included
    in the list of letters the user guessed, or not.
    :rtype: bool
    """
    s = " _ "
    n = secret_word
    for char in secret_word:
        c_exist = False
        for c in old_letters_guessed:
            if char == c:
                c_exist = True
                n = n.replace(char, c)
                break
        if c_exist == False:
            n = n.replace(char, ' _ ')
    if n.count(' _ ') != 0:
        return False
    else:
        return True


def main():
    MAX_TRIES = 6
    # Print the Welcome Screen
    print_welcome_screen(MAX_TRIES)

    # Receive Input from the player: text file path and index of word to guess from the text file
    file_path = input("Enter file path: ")
    index = int(input("Enter index: "))
    print("Let’s start!")

    # Initial variables and initial state of the game
    num_of_tries = 0
    print_hangman(num_of_tries)

    secret_word = choose_word(file_path, index)
    len_secret_word = len(secret_word)

    old_letters_guessed = []
    show_hidden_word(secret_word, old_letters_guessed)

    # main iteration - Input of one character per round's game.
    """If the character is valid (two or more characters and / or is not an English letter, or guessed it in the past), 
    type "X" on the screen, and the list of previously guessed letters (as a string in small letters, sorted from small to large and separated by arrows). 
    Request the player to enter an additional character until the character entered is correct."""
    """After each correct guess, the player will be shown the secret word in the form of underlines 
    (even if he has guessed partially or has not yet been able to guess at all).
    In case of a failed guess - the output will be printed for the player :( and below it a picture of the hangman in a more "advanced" mode"""

    """End of the game:
        If the player guesses the whole word correctly - it will be printed on the WIN screen.
        If the player guesses six failed attempts - will be printed on the LOSE screen."""
    while num_of_tries < MAX_TRIES:
        letter_guessed = str(input("Guess a letter: "))
        valid_guess = try_update_letter_guessed(letter_guessed, old_letters_guessed)
        while valid_guess == False:
            letter_guessed = str(input("Guess a letter: "))
            valid_guess = try_update_letter_guessed(letter_guessed, old_letters_guessed)
        if letter_guessed.lower() in secret_word[:].lower():
            if check_win(secret_word, old_letters_guessed):
                print("WIN!")
                exit(1)
        else:
            print(":(" + '\n')
            num_of_tries += 1
            print_hangman(num_of_tries)
        show_hidden_word(secret_word, old_letters_guessed)
    print("LOSE")
    exit(1)


# main program
if __name__ == "__main__":
    main()
