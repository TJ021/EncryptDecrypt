"""
Encrypt or decrypt the contents of a message file using a deck of cards.
"""

import cipher_functions

DECK_FILENAME = 'deck1.txt'
MSG_FILENAME = 'message-encrypted.txt'
MODE = 'd'  # 'e' for encryption, 'd' for decryption.


def main():
    """ () -> NoneType

    Perform the encryption using the deck from a file called DECK_FILENAME and
    the messages from a file called MSG_FILENAME. If MODE is 'e', encrypt;
    otherwise, decrypt. Print the decrypted message to the screen.
    """

    # The message thats needs to be encrypted or decrypted is opened along
    # with  a deck of cards.
    open_deck = open(DECK_FILENAME, 'r')
    open_message = open(MSG_FILENAME, 'r')

    # The deck and message are sent to the child class to be placed in a list
    # and to be joined together.
    deck = cipher_functions.read_deck(open_deck)
    message = cipher_functions.read_messages(open_message)

    # The message is either decrypted or encrypted.
    msg = cipher_functions.process_messages(deck, message, MODE)
    # The message is converted to a string.
    msg = ''.join(msg)

    # The program outputs the message.
    print(msg)

    # The files are closed.
    open_deck.close()
    open_message.close()

main()
