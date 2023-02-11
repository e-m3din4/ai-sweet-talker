import re
import colorama
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from colorama import Fore, Style

# Print Banner
print('')
print('**************************************************')
print('*     ___  __             ___                    *')
print('*  /\  |  (_      _  __|_  | _.||  _ ._          *')
print('* /--\_|_ __)\/\/(/_(/_|_  |(_|||<(/_|           *')
print('*      -A Montessorian based                     *')
print('*  Artificial Inteligence Prompt                 *') 
print('*        Grammar Analyzer-                       *')
print('*      Author: Edgar Medina.                     *')
print('**************************************************')
print('')

# Function to analyze grammar functions in a given prompt
def analyze_prompt(prompt):
    # Tokenize and tag parts of speech
    tokens = word_tokenize(prompt)
    tagged = pos_tag(tokens)
    
    # Initialize counts for each grammatical function
    noun_count = 0
    article_count = 0
    verb_count = 0
    adjective_count = 0
    adverb_count = 0
    pronoun_count = 0
    conjunction_count = 0
    preposition_count = 0
    interjection_count = 0

    # Dictionary of grammar functions and corresponding colors
    grammar_functions = {
        "NN": Fore.BLUE,
        "NNS": Fore.BLUE,
        "NNP": Fore.BLUE,
        "NNPS": Fore.BLUE,
        "DT": Fore.YELLOW,
        "VB": Fore.GREEN,
        "VBD": Fore.GREEN,
        "VBG": Fore.GREEN,
        "VBN": Fore.GREEN,
        "VBP": Fore.GREEN,
        "VBZ": Fore.GREEN,
        "JJ": Fore.RED,
        "JJR": Fore.RED,
        "JJS": Fore.RED,
        "RB": Fore.CYAN,
        "RBR": Fore.CYAN,
        "RBS": Fore.CYAN,
        "PRP": Fore.MAGENTA,
        "PRP$": Fore.MAGENTA,
        "WP": Fore.MAGENTA,
        "WP$": Fore.MAGENTA,
        "CC": Fore.WHITE,
        "IN": Fore.WHITE,
        "UH": Fore.WHITE
    }

    # Loop through tagged tokens and count grammatical functions
    for token, tag in tagged:
        if tag in grammar_functions:
            color = grammar_functions[tag]
            print(f"{color}{token}{Fore.RESET}", end=" ")
            if tag in ["NN", "NNS", "NNP", "NNPS"]:
                noun_count += 1
            elif tag in ["DT"]:
                article_count += 1
            elif tag in ["VB", "VBD", "VBG", "VBN", "VBP", "VBZ"]:
                verb_count += 1
            elif tag in ["JJ", "JJR", "JJS"]:
                adjective_count += 1
            elif tag in ["RB", "RBR", "RBS"]:
                adverb_count += 1
            elif tag in ["PRP", "PRP$", "WP", "WP$"]:
                pronoun_count += 1
            elif tag in ["CC"]:
                conjunction_count += 1
            elif tag in ["IN"]:
                preposition_count += 1
            elif tag in ["UH"]:
                interjection_count += 1
                
    # Check the count of each type of grammatical function and provide suggestions based on the results
    if noun_count == 0:
        print("Your prompt is missing nouns. Consider adding descriptive nouns to make the prompt more specific.")
    elif noun_count > 5:
        print("Your prompt has a large number of nouns. Consider simplifying the prompt by using fewer nouns.")

    if verb_count == 0:
        print("Your prompt is missing verbs. Consider adding action verbs to make the prompt more interesting.")
    elif verb_count > 5:
        print("Your prompt has a large number of verbs. Consider simplifying the prompt by using fewer verbs.")

    if adjective_count == 0:
        print("Your prompt is missing adjectives. Consider adding descriptive adjectives to make the prompt more interesting.")
    elif adjective_count > 5:
        print("Your prompt has a large number of adjectives. Consider simplifying the prompt by using fewer adjectives.")

    if adverb_count == 0:
        print("Your prompt is missing adverbs. Consider adding adverbs to describe how the actions in the prompt are performed.")
    elif adverb_count > 5:
        print("Your prompt has a large number of adverbs. Consider simplifying the prompt by using fewer adverbs.")

    if pronoun_count == 0:
        print("Your prompt is missing pronouns. Consider adding pronouns to make the prompt more personal.")
    elif pronoun_count > 5:
        print("Your prompt has a large number of pronouns. Consider simplifying the prompt by using fewer pronouns.")

    if conjunction_count == 0:
        print("Your prompt is missing conjunctions. Consider adding conjunctions to connect ideas in the prompt.")
    elif conjunction_count > 5:
        print("Your prompt has a large number of conjunctions. Consider simplifying the prompt by using fewer conjunctions.")

    if preposition_count == 0:
        print("Your prompt is missing prepositions. Consider adding prepositions to make the prompt more specific.")
    elif preposition_count > 5:
        print("Your prompt has a large number of prepositions. Consider simplifying the prompt by using fewer prepositions.")

    if interjection_count == 0:
        print("Your prompt is missing interjections. Consider adding interjections to make the prompt more interesting.")
    elif interjection_count > 5:
        print("Your prompt has a large number of interjections. Consider simplifying the prompt by using fewer interjections.")

# Main function
def main():
    # Prompt the user for input
    prompt = input("Please enter your prompt: ")
    analyze_prompt(prompt)

# Call the main function
if __name__ == "__main__":
    main()
    print(Style.RESET_ALL)
