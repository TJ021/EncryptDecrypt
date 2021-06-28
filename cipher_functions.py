# Functions for running an encryption or decryption.

# The values of the two jokers.
JOKER1 = 27
JOKER2 = 28

# Write your functions here:


def clean_message(message):
    '''(str) -> str
    Given a string, the function will return the string with only alphabets and
    all the letters will be upper case.
    REQ: The string must contain atleast one alphabet.
    >>> clean_message('Hello World')
    'HELLOWORLD'
    >>> clean_message('1a2b3c4d')
    'ABCD'
    >>> clean_message('$t#e&j!a@s(v*i^')
    'TEJASVI'
    '''
    clean_message = ''
    for letter in message:
        # Checks if current letter in the message is an alphabet.
        if (letter.isalpha()):
            # The new message contains only upper case alphbets.
            clean_message += letter.upper()

    # The new message is returned.
    return clean_message


def encrypt_letter(char, key):
    '''(str, int) -> str
    Given a letter and a integer key, the function will return the encrypted
    letter.
    REQ: The char must be a letter.
    REQ: The key must be an integer.
    >>> encrypt_letter('a', 9)
    'J'
    >>> encrypt_letter('b', 9)
    'K'
    >>> encrypt_letter('c', 9)
    'L'
    >>> encrypt_letter('d', 9)
    'M'
    '''
    # List used to get the numerical value of the char.
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    char = char.upper()
    # The char is converted into the numerical value of the letter.
    char = alpha.index(char)
    # The key is added to the char.
    char += key

    # If the char is greater than 25, then 26 is subtracted from it.
    if (char > 25):
        char -= 26
    # The char is converted back to a string.
    char = alpha[char]

    # The char is returned.
    return char


def decrypt_letter(char, key):
    '''(str, int) -> str
    Given a letter and a integer key, the function will return the decrypted
    letter.
    REQ: The char must be a letter.
    REQ: The key must be an integer.
    >>> decrypt_letter('j', 9)
    'A'
    >>> decrypt_letter('k', 9)
    'B'
    >>> decrypt_letter('l', 9)
    'C'
    >>> decrypt_letter('m', 9)
    'D'
    '''
    # List used to get the numerical value of the char.
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    char = char.upper()
    # The char is converted into the numerical value of the letter.
    char = alpha.index(char)
    # The key is subtracted from the char.
    char -= key

    # If the char is less than 0, then 26 is added to it.
    if (char < 0):
        char += 26
    # The char is converted back to a string.
    char = alpha[char]

    # The char is returned.
    return char


def swap_cards(deck, index):
    '''(list of int, int) -> NoneType
    Given a list of integers and a index, the function will swap the card at
    the index with teh card that follows it.
    REQ: The deck must have a length greater than 0.
    REQ: The index must be an integer.
    >>> deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> swap_cards(deck, 3)
    >>> deck
    [1, 2, 3, 5, 4, 6, 7, 8, 9, 10]

    >>> deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> swap_cards(deck, 7)
    >>> deck
    [1, 2, 3, 4, 5, 6, 7, 9, 8, 10]

    >>> deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> swap_cards(deck, 9)
    >>> deck
    [10, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    '''
    # If the element at the index given is the same as the element at the end
    # of the index, the first and last elemttn are swapped.
    if (deck[index] == deck[len(deck)-1]):
        temp = deck[-1]
        deck[-1] = deck[0]
        deck[0] = temp

    # The element at the index is swpaped with the following element.
    else:
        temp = deck[index]
        deck[index] = deck[index+1]
        deck[index+1] = temp


def move_joker_1(deck):
    '''(list of int) -> NoneType
    Given a list of integers, the function will move JOKER1, one index back.
    REQ: The deck must be a list of integers containing 27 and must have a
    length greater than 0.
    >>> deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 27]
    >>> move_joker_1(deck)
    >>> deck
    [27, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    >>> deck = [1, 2, 3, 4, 5, 27, 7, 8, 9, 10]
    >>> move_joker_1(deck)
    >>> deck
    [1, 2, 3, 4, 5, 7, 27, 8, 9, 10]
    '''
    # Gets the index of JOKER1.
    joker1 = deck.index(JOKER1)
    # The swap_cards function is used to move JOKER1 back one index.
    swap_cards(deck, joker1)


def move_joker_2(deck):
    '''(list of int) -> NoneType
    Given a list of integers, the function will move JOKER2, two index' back.
    REQ: The deck must be a list of integers containing 28 and must have a
    length greater than 0.
    >>> deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 28]
    >>> move_joker_2(deck)
    >>> deck
    [2, 28, 3, 4, 5, 6, 7, 8, 9, 1]
    >>> deck = [1, 2, 3, 4, 5, 28, 7, 8, 9, 10]
    >>> move_joker_2(deck)
    >>> deck
    [1, 2, 3, 4, 5, 7, 8, 28, 9, 10]
    '''
    # This is preformed twice because JOKER2 needs to be moved back 2 index'.
    for counter in range(0, 2):
        # Gets the index of JOKER2.
        joker2 = deck.index(JOKER2)
        # The swap_cards function is used to move JOKER2 back one index.
        swap_cards(deck, joker2)


def triple_cut(deck):
    '''(list of int) -> NoneType
    Given a list of integers, the function will preform a triple cut on the
    list of integers.
    REQ: The deck must be a list of integers containing 27 and 28 and must have
    a length greater than 0.
    >>> deck = [1, 2, 3, 27, 5, 6, 7, 28, 9, 10]
    >>> triple_cut(deck)
    >>> deck
    [9, 10, 27, 5, 6, 7, 28, 1, 2, 3]

    >>> deck = [1, 2, 3, 28, 5, 6, 7, 27, 9, 10]
    >>> triple_cut(deck)
    >>> deck
    [9, 10, 28, 5, 6, 7, 27, 1, 2, 3]
    '''
    # Gets the index of JOKER1 and JOKER2.
    joker1 = deck.index(JOKER1)
    joker2 = deck.index(JOKER2)

    # If JOKER1's index is less than JOKER2's index, then all the elements
    # before JOKER1 goes after JOKER2 and all the elemnts after JOKER2 go
    # before JOKER1.
    if (joker1 < joker2):
        deck[:] = deck[joker2+1:] + deck[joker1:joker2+1] + deck[:joker1]

    # If JOKER2's index is less than JOKER2's index, then all the elements
    # before JOKER2 goes after JOKER2 and all the elemnts after JOKER1 go
    # before JOKER2.
    else:
        deck[:] = deck[joker1+1:] + deck[joker2:joker1+1] + deck[:joker2]


def insert_top_to_bottom(deck):
    '''(listof int) -> NoneType
    Given a list of integers, the function will move a specific number of
    elements from the top of the list to the bottom before the last element.
    REQ: The deck must be a list of integers containing 27 and 28 and must have
    a length greater than 0.
    >>> deck = [1, 2, 3, 4, 5, 6, 7, 27, 9, 28]
    >>> insert_top_to_bottom(deck)
    >>> deck
    [1, 2, 3, 4, 5, 6, 7, 27, 9, 28, 28]
    >>> deck = [1, 2, 3, 28, 5, 6, 7, 27, 9, 5]
    >>> insert_top_to_bottom(deck)
    >>> deck
    [6, 7, 27, 9, 1, 2, 3, 28, 5, 5]
    '''
    # If the last element is JOKER2, then the number of cards that need to be
    # moved are 27.
    if (deck[-1] == JOKER2):
        num_cards = JOKER1

    # The number of cards that need to be moved is the last element.
    else:
        num_cards = deck[-1]

    # The specific number of cards aremoved form the top of the deck, to the
    # bottom before the last element.
    deck[:] = deck[num_cards:-1] + deck[:num_cards] + deck[-1:]


def get_card_at_top_index(deck):
    '''(list of int) -> int
    Given a list of integers, the function will return the card at the index
    of the top number.
    REQ: The deck must be a list of integers containing 27 and 28 and must have
    a length greater than 0.
    >>> deck = [5, 2, 3, 28, 5, 6, 7, 27, 9, 5]
    >>> get_card_at_top_index(deck)
    6
    >>> deck = [1, 2, 3, 28, 5, 6, 7, 27, 9, 5]
    >>> get_card_at_top_index(deck)
    2
    '''
    top_card = deck[0]

    # If the card at the top of the deck is JOKER2, then the new top card is
    # 27.
    if (top_card == JOKER2):
        top_card = JOKER1

    card = deck[top_card]

    # The card at the index at the top card is returned.
    return card


def get_next_value(deck):
    '''(list of int) -> int
    Given a list of integers, the function will return the next potential
    keystream value.
    REQ: The deck must be a list of integers containing 27 and 28 and must have
    a length greater than 0 and less than JOKER2.
    >>> deck = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21,\
    24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> get_next_value(deck)
    11
    >>> deck = [23, 26, 28, 9, 12, 15, 18, 21, 24, 2, 27, 1, 4, 7, 10, 13, 16,\
    19, 22, 25, 3, 5, 8, 11, 14, 17, 20, 6]
    >>> get_next_value(deck)
    9
    '''
    # Various functions are called to get the net potential keystream value.
    move_joker_1(deck)
    move_joker_2(deck)
    triple_cut(deck)
    insert_top_to_bottom(deck)
    key = get_card_at_top_index(deck)

    # The potential keystream is returned.
    return key


def get_next_keystream_value(deck):
    '''(list of int) -> int
    Given a list of integers, the function will return the next valid
    keystream.
    REQ: The deck must be a list of integers containing 27 and 28 and must have
    a length greater than 0 and less than JOKER2.
    >>> deck = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21,\
    24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> get_next_keystream_value(deck)
    11
    >>> deck = [23, 26, 28, 9, 12, 15, 18, 21, 24, 2, 27, 1, 4, 7, 10, 13, 16,\
    19, 22, 25, 3, 5, 8, 11, 14, 17, 20, 6]
    >>> get_next_keystream_value(deck)
    9
    '''
    # The potential next keystream.
    key = get_next_value(deck)

    # If the potential keystream is 27 or 28, The function continues to get the
    # next potential keystream value.
    if (key == JOKER1 or key == JOKER2):
        while (key == JOKER1 or key == JOKER2):
            key = get_next_value(deck)

    # The next keystream value is returned.
    return key


def process_message(deck, message, eord):
    '''(list of int, str, str) -> str
    Given a list of integers, a string, and the mode, the function will return
    the encrypted or decrypted message.
    REQ: The deck must be a list of integers containing 27 and 28 and must have
    a length greater than 0.
    REQ: The message must contain atleast one alphabet.
    REQ: The mode must be either e or d.
    >>> deck = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21,\
    24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> process_message(deck,'Tejasvi Singh','e')
    'ENGHCUTDPVPS'
    >>> deck = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21,\
    24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> process_message(deck,'ENGHCUTDPVPS','d')
    'TEJASVISINGH'
    '''
    # The messages is contains only alphabets and is upper case.
    message = clean_message(message)
    keystream_list = list()
    eord_message = ''

    # The list of keystreams.
    for letter in message:
        keystream_list.append(get_next_keystream_value(deck))

    # If the user wants to encrypt the message.
    if (eord == 'e'):
        for counter in range(len(message)):
            eord_message += encrypt_letter(message[counter],
                                           keystream_list[counter])

    # If the user wanst to decrypt the message.
    elif (eord == 'd'):
        for counter in range(len(message)):
            eord_message += decrypt_letter(message[counter],
                                           keystream_list[counter])

    # The encrypted or decrypted message is returned
    return eord_message


def process_messages(deck, messages, eord):
    '''(list of int, list of str, str) -> str
    Given a list of integers, a string, and the mode, the function will return
    the encrypted or decrypted sentence.
    REQ: The deck must be a list of integers containing 27 and 28 and must have
    a length greater than 0.
    REQ: The message must contain atleast one alphabet.
    REQ: The mode must be either e or d.
    >>> deck = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21,\
    24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> process_message(deck,['Tejasvi', 'Singh'],'e')
    'ENGHCUTDPVPS'
    >>> deck = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 3, 6, 9, 12, 15, 18, 21,\
    24, 27, 2, 5, 8, 11, 14, 17, 20, 23, 26]
    >>> process_message(deck,['ENGHCUT', 'DPVPS'],'d')
    'TEJASVISINGH'
    '''
    eord_messages = list()

    # Each message is encrypted or decrypted and stored in one list.
    for message in messages:
        eord_messages.append(process_message(deck, message, eord))

    # The list of messages is returned.
    return eord_messages


def read_messages(file):
    '''(io.TextIOWrapper) -> list of str
    Given an open file, the function will read the file and put the message
    into a list.
    REQ: The file must be open for reading.

    '''
    message = list()
    # The message is stored in a list.
    for next_line in file:
        message.append(next_line.strip('\n'))

    # The message is returned.
    return message


def read_deck(file):
    '''(io.TextIOWrapper) -> list of str
    Given an open file, the function will read the file and put the deck
    into a list.
    REQ: The file must be open for reading.

    '''
    deck = list()
    # The deck is stored in a list.
    for cards in file:
        deck += cards.split()

    # All the elemenst in the deck are converted to strings.
    deck = [int(cards) for cards in deck]

    # The deck is returned.
    return deck
