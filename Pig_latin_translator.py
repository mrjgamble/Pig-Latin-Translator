###################
# Piglatintranslator.py
#
# Program that accepts a word or phrase and returns the pig latin
# translations
#
# Rules - From https://en.wikipedia.org/wiki/Pig_Latin
# 1) For words that begin with consonant sounds, all letters before
# the initial vowel are placed at the end of the word sequence.
# Then, "ay" is added
#
# 2) When words begin with consonant clusters (multiple consonants that form
# one sound), the whole sound is added to the end when speaking or writing
#
# 3) For words that begin with vowel sounds, one just adds "way" to the end
#
# 4) If the word begins with a capital letter, the translation will also contain
#    a proper capitalization
#
# 5) If the word contains punctuation, the letters within the word
#    will be transalted and punctuation stay intacted
def translator():
    """ Takes a user's input (an english word or phrase) and returns the
    Pig Latin translation.
    """

    # Split the input based on spaces
    phrase = get_input().split(' ')

    output = ''
    capital_case = False

    # Loop through our words
    for i in range (len(phrase)):

        # Check to see if this word is characters only
        if phrase[i].isalpha():

            # This is a regular word, so translate it
            phrase[i] = translate_word(phrase[i])

        # Otherwise we know we are going to have to deal with punctuation
        # and potentially numbers
        else:

            partial = ''
            output = ''

            # Loop through our word
            for j in range(len(phrase[i])):

                # If the character is something from the alphabet, add it to
                # our parital word
                if phrase[i][j].isalpha():
                    partial += phrase[i][j]

                # Otherwise we know we found punctuation or a number
                else:

                    # if we've seen characters to the left of this value, we
                    # know we need to translate those values
                    if partial:

                        # convert this word & reset the partial
                        output += translate_word(partial)
                        partial = ''

                    # Add the character to our output
                    output += phrase[i][j]

            # We've come to the end of the word.  Check to see if there are any
            # values that have not been translated, and translate them.
            if partial:
                output+= translate_word(partial)

            # Update our original word
            phrase[i] = output

    # return the translated phrase
    print(' '.join(phrase))


def translate_word(word):
    """ Takes a single word that is composed of characters only and translates
    the value into pig latin
    """

    VOWELS = ('a', 'e', 'i', 'o', 'u')
    new_word = ''

    # Check to see if the first letter is a vowel
    if word[0].lower() in VOWELS:
        new_word = word + 'way'

    # First letter is not a vowel, so we need to cycle through each
    # character
    else:

        # Loop through the word
        for i in range (len(word)):

            # If we found a vowel, translate the word
            if word[i].lower() in VOWELS:
                new_word = word[i:] + word[:i] + 'ay'
                break

    # Check for uppercase
    if word[0].isupper():
        new_word = new_word.capitalize()

    return new_word

def get_input():
    """ Prompts user to input a word or phrase to be translated into Pig Latin.
    The user will be prompted while input is blank"""

    while True:

        phrase = input('Please enter a phrase to be translated: ')

        # We did not receive any input, so prompt again
        if not phrase:
            print('\nI did not understand that. Try again.\n')
            continue
        else:
            break

    return phrase


if __name__ == '__main__':
    translator()
