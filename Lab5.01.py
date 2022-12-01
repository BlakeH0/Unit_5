'''
###########
Lab 5.01
###########

Instructions
------------
Write a program that uses a dictionary to offer users the meanings of common internet abbreviations.
The program, dictionary_lab.py, prompts the user to enter an internet abbreviation they would like explained. 
If the requested abbreviation is in the program's dictionary (use the in keyword with an if statement 
to test this), then it prints out the definition. If the abbreviation is not in the dictionary, the program 
prints an apologetic message saying that it could not find a definition.

Example Output:
---------------
>>> python3 dictionary_lab.py

What word would you like to look up? nbd
nbd: a phrase meaning no big deal

What word would you like to look up? kittens
Sorry, kittens is not defined

What would would you like to look up?

Bonus
------
Extend the program with any of these features:
The user can
update the definitions (values) for existing abbreviations in the dictionary
add new abbreviations (keys) and provide their definitions (values).
delete entries (key, value pairs) from the dictionary.
get the entire dictionary printed to the screen.
Lesson 6.01 did not cover all the techniques for manipulating dictionaries that you will need to program these features. Search for the necessary information in the [Python tutorial about dictionaries][1] and the [advanced Python documentation about dictionaries][2].
'''

# Internet Abbreviatrions Dictionary
abbreviations = {
    'ttyl': 'ttyl: A phrase meaning "talk to you later" ',
    'brb': 'brb: A phrase meaning "be right back" ',
    'gn': 'gn: A phrase meaning "goodnight" ',
    'gm': 'gm: A phrase meaning "goodmorning" ',
    'gg': 'gg: A phrase meaning "good game", often used in videogames ',
    'omw': 'omw: A phrase meaning "on my way" ',
    'omg': 'omg: A phrase meaning "oh my god/gosh" ',
    'lmao': 'lmao: A phrase meaning "laughing my a** off" ',
    'lol': 'lol: A phrase meaning "laugh out loud" ',
    'gtg': 'gtg: A phrase meaning "got to go" ',
    'idk': 'idk: A phrase meaning "I dont know" ',
    'idc': 'idc: A phrase meaning "I dont care" ',
    'idek': 'idek: A phrase meaning "I dont even know" ',
    'idec': 'idec: A phrase meaning "I dont even care" ',
    'smh': 'smh: A phrase meaning "shake/shaking my head" ',
    'ig': 'ig: A phrase meaning "I guess" ',
    'abt': 'abt: A phrase meaning "about" ',
    'bc': 'bc: A phrase meaning "because" '
}

while True:
    print()
    user_choice = int(input("What would you like to do? \n"
    "1. Look up abbreviation \n"
    "2. Delete an abbreviation \n"
    "3. Update a definition \n"
    "4. Display whole dictionary \n"))
    if user_choice == 1:
        user_word = input("What abbreviation would you like to look up? ")
        for i in abbreviations:
            if user_word == i:
                print(abbreviations[user_word])
        if user_word not in abbreviations:
            print(f"Sorry, {user_word} is not defined. ")
    elif user_choice == 2:
        delete_abb = input("What abbreviation would you like to delete? ")
        for word in abbreviations:
            if word == delete_abb:
                del abbreviations[word]
                break
            else:
                print(f"{delete_abb} is not defined in my dictionary.")
                break
    elif user_choice == 3:
        update_word = input("What abbreviation's definition would you like to update? ")
        for abb in abbreviations:
            if abb == update_word:
                new_def = input("What would you like to update the definition to? ")
                abbreviations[abb] = f"{abb}: A phrase meaning '{new_def}'"
            elif update_word not in abbreviations:
                print(f"Uh oh! That abbreviation is not in my database...")
                break
    elif user_choice == 4:
        for item, definition in abbreviations.items():
            print(definition)