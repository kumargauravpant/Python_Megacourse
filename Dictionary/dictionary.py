import json
from difflib import get_close_matches

# Load the json data
dictionaryData = json.load(open("data.json","r"))

# Function to translate the word
def translate(word):
    # Check for lower case : rain
    if word.lower() in dictionaryData.keys():
        return dictionaryData[word.lower()]
    # Check for Camel case : Delhi
    elif word.title() in dictionaryData.keys():
        return dictionaryData[word.title()]
    # Check for upper case : USA
    elif word.upper() in dictionaryData.keys():
        return dictionaryData[word.upper()]
    # Check for the match case instead
    elif len(get_close_matches(word, dictionaryData.keys())):
        user_input = input("Did you mean '{}' instead? (y/n): ".format(get_close_matches(word, dictionaryData.keys())[0]))

        if user_input.lower() == "y":
            return dictionaryData[get_close_matches(word, dictionaryData.keys())[0]]
        elif user_input.lower() == "n":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your response."

    else:
        return "The word doesn't exist. Please double check it."



def printResult(translation):
    if isinstance(translation, list):
        for count,item in enumerate(translation):
            print("\n", str(count+1) + ".", item)
    else:
        print("\n", translation)



print("##########################################################################################")
print("##                                                                                      ##")
print("##                           The Ultimate Dictionary                                    ##")
print("##                                                                                      ##")
print("##########################################################################################")

while True:
    user_input = input("\n* Please select an option. \n* 1. Lookup a Word\n* 0. Exit\n\n")

    if user_input == "1":
        word = input("Enter Word: ")
        translation = translate(word)
        #print("\n", "\u0332".join(word + ":"))  # Not working in windows.
        print("\n", word + ":")
        printResult(translation)
    elif user_input == "0":
        print("Thanks for using 'The Ultimate Dictionary'.")
        break
    else:
        print("We didn't understand your response. Please try again.")




