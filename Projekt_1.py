"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Tereza Písecká
email: pisecka.tereza@seznam.cz
discord: TerkaP terka_41921
"""
import sys
sys.path.append(r'C:\Users\terez\Documents\Python_projekt_1')

import texts

TEXTS = texts.TEXTS

registered_users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# Login function
def login():
    print("Welcome to a text analyzer!")
    username = input("Please fill in your username:")
    password = input("And now fill in your password:")
    
    print("-" * 40)

    # Login credentials verification
    if username in registered_users and registered_users[username] == password:
        print(f"Hello, {username}! Now you can start analyzing the texts!")
        return True
    else:
        print("Oops, your name or password is wrong.")
        return False
if login():
    pass
else:
    print("Login failed")
    sys.exit()

print("-" * 40)

def clean_word(word):
    return word.strip(",.!?\"'()[]{}:;")

print("Select a text number (1, 2, 3):")  

choice = input() 

# Checking if the user entered a valid number
if choice.isdigit():  
    choice = int(choice) 
    if 1 <= choice <= 3: 
        text = TEXTS[choice - 1]  
        print("-" * 40)
        print(f"You have selected text {choice}:")
        print("-" * 40)

        words = [clean_word(word) for word in text.split() if clean_word(word)]
        
        print(words)

        # Statistics
        word_count = len(words)
        title_case_count = sum(1 for word in words if word.istitle())
        upper_case_count = sum(1 for word in words if word.isupper() and word.isalpha())
        lower_case_count = sum(1 for word in words if word.islower())
        numeric_count = sum(1 for word in words if word.isdigit())
        numeric_sum = sum(int(word) for word in words if word.isdigit()) 

        # Display of results
        print(f"There are {word_count} words in the selected text.")
        print(f"There are {title_case_count} titlecase words.")
        print(f"There are {upper_case_count} uppercase words.")
        print(f"There are {lower_case_count} lowercase words.")
        print(f"There are {numeric_count} numeric strings.")
        print(f"The sum of all the numbers: {numeric_sum}")
        
        word_lengths = {}

        # Graph
        for word in words:
            length = len(word)
            word_lengths[length] = word_lengths.get(length, 0) + 1
        
        print("-" * 40)
        print("LEN|  OCCURENCES  |NR.")  
        print("-" * 40)
        
        for length in sorted(word_lengths.keys()):
            count = word_lengths[length]
            print(f"{length:3} | {'*' * count:<15} | {count}") 
        print("-" * 40)
        
    else:
        print("Invalid choice. Choose a number 1, 2 or 3.")  
else:
    print("You have entered an invalid input. It should have been a number.") 

