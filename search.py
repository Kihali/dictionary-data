import json
import difflib

# Load JSON data into a Python dictionary
def load_dictionary(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Create a function to get the definition of a word
def get_definition(word, dictionary):
    # Convert the word to lowercase to handle case insensitivity
    word = word.lower()
    return dictionary.get(word, None)

# Suggest a word that might be intended
def suggest_word(word, dictionary):
    # Convert the dictionary keys to lowercase for comparison
    keys = [key.lower() for key in dictionary.keys()]
    suggestions = difflib.get_close_matches(word.lower(), keys)
    return suggestions

# Main function to search for word definition
def search_word(word, dictionary):
    definition = get_definition(word, dictionary)
    if definition:
        print(f"Definition of '{word}': {definition}")
    else:
        print(f"'{word}' not found in the dictionary.")
        suggestions = suggest_word(word, dictionary)
        if suggestions:
            print("Did you mean:")
            for suggestion in suggestions:
                print(f"  - {suggestion}")
        else:
            print("No suggestions available.")

# Path to the JSON file
file_path = 'data.json'  

# Load the dictionary
dictionary = load_dictionary(file_path)

# Get user input and search for the word
word = input("Enter a word to define: ")
search_word(word, dictionary)
