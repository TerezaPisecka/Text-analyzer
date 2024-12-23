"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Tereza Písecká
email: pisecka.tereza@seznam.cz
discord: TerkaP terka_41921
"""

import sys
sys.path.append(r'C:\Users\terez\Documents\Python_projekt_1')

import texts

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
    
    print("----------------------------------------")

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
    print("Login failed. Try again.")

print("----------------------------------------")

print("Select a text number (1, 2, 3):")  

choice = input() 

# Checking if the user entered a valid number
if choice.isdigit():  
    choice = int(choice) 
    if 1 <= choice <= 3: 
        text = texts.TEXTS[choice - 1]  
        print("----------------------------------------")
        print(f"You have selected text {choice}:")
        print("----------------------------------------")
        
        # Statistics
        words = text.split()
        wordcount = len(words)
        first_letter_upper = sum(1 for word in words if word[0].isupper())
        word_upper = sum(1 for word in words if word.isupper()) 
        word_lower = sum(1 for word in words if word.islower()) 
        numbers_count = sum(1 for word in words if word.isdigit()) 
        sum_of_numbers = sum(int(word) for word in words if word.isdigit()) 

        # Display of results
        print(f"There are {wordcount} words in the selected text.")
        print(f"There are {first_letter_upper} titlecase words.")
        print(f"There are {word_upper} uppercase words.")
        print(f"There are {word_lower} lowercase words.")
        print(f"There are {numbers_count} numeric strings.")
        print(f"The sum of all the numbers: {sum_of_numbers}")
        
        word_lengths = {}

        # Graph
        for word in words:
            length = len(word)
            if length in word_lengths:
                word_lengths[length] += 1
            else:
                word_lengths[length] = 1
        
        print("\n----------------------------------------")
        print("LEN|  OCCURENCES  |NR.")  
        print("----------------------------------------")
        
        for length in sorted(word_lengths.keys()):
            count = word_lengths[length]
            graf = '*' * count  
            print(f" {length:2}|{graf:<13}|{count}") 
        print("----------------------------------------")
        
    else:
        print("Invalid choice. Choose a number 1, 2 or 3.")  
else:
    print("You have entered an invalid input. It should have been a number.") 

