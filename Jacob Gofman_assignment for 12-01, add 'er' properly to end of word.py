##Jacob Gofman
##Due December 1st

import re

vowel = ['a', 'e', 'i', 'o', 'u'] ##set of vowels
specific_consonants = ['r', 'w', 'x', 'y'] ##set of consonants that are exceptions
affirmative = ['yes', 'yep', 'y', 'yea', 'sure', 'please', 'mhmm'] ##set of answers for 'yes'
negative = ['no', 'nope', 'n', 'nah'] ##set of answers for 'no'

def change_ending_to_er(): ##main function
    word_only = False
    string = ''
    while word_only == False: ##prompt for user that only lets you pass if you enter letters as a response
        string = raw_input('\nEnter a word and I will add "er" to it with proper English grammar: ')
        word_only = string.isalpha()

    if (len(string) >= 3):
        ## 3+ letter words
        ending = re.search('(.)(.)(.)$',string)
        ##checks the last three characters of the word entered
        if (ending.group(3) == 'y'): print('\nThis is the new word: ' + (string.replace(string[-1], 'ier')))
        ## 'y' --> 'ier'
        elif ((ending.group(3) == 'y') and (ending.group(2) in vowel)): print('\nThis is the new word: ' + (string + 'er'))
        ## if it's a y following a vowel just add 'er' (Deviation from assignment, exceptions)
        elif (ending.group(3) == 'e'): print('\nThis is the new word: ' + (string + 'r'))
        ## e --> add 'r'
        elif ((ending.group(3) not in specific_consonants) and (ending.group(2) in vowel) and (ending.group(1) in vowel)): print('\nThis is the new word: ' + (string + 'er'))
        ## if regular consonant following a vowel which follows another vowel (eat), add 'er'
        elif ((ending.group(3) not in (specific_consonants or vowel or ending.group(2))) and (ending.group(2) in vowel)): print('\nThis is the new word: ' + (string + string[-1] + 'er'))
        ## if regular consonant and not identical to the previous character, double and add 'er'
        elif (ending.group(3) in specific_consonants): print('\nThis is the new word: ' + (string + 'er'))
        ## if specific consonant then add 'er' (Deviation from assignment, exceptions)
        elif ((ending.group(3) and ending.group(2)) not in vowel): print('\nThis is the new word: ' + (string + 'er'))
        else: print('\nI\'m sorry, but I cannot add "er" to the end of this word.')

    ## EXTRA SECTION for 1 and 2 letter word exceptions

    elif (len(string) == 2):
        ## 2 letter words
        ending = re.search('(.)(.)$',string)
        ## checks the last two characters of the word entered
        if ((ending.group(2) in vowel) and (ending.group(1) not in vowel)): print('\nI don\'t think you can add "er" to the end of this word but this is the new word: ' + (string + 'er'))
        ## if last letter is a vowel following a consonant, then it's probably not a word you can add 'er' to but since there might be a word that allows that, I followed through anyway
        if ((ending.group(2) not in vowel) and (ending.group(1) in vowel)): print('\nThis is the new word: ' + (string + string[-1] + 'er'))
        ## if last letter is a consonant following a vowel, then double the last letter and add an 'er' (i was thinking of in-->inner and up-->upper)
    elif ((len(string) == 1) or ((ending.group(2) and ending.group(1)) not in vowel) or ((ending.group(2) and ending.group(1)) in vowel)):
        ## 1 letter words or words with two consonants/vowels in a row
        print('\nInvalid word.\n')
        change_ending_to_er()

    
    check = True
           
    while check == True:  ## option for program restart
        response = raw_input('\nWould you like to try another word? ')
        if response in affirmative:
           change_ending_to_er()
           check = False
        elif response in negative:
           print('\nHave a nice day.')
           check = False
            

    return

change_ending_to_er()
