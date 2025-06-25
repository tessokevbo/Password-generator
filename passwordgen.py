print ("Safe password generator")
lenght = int(input("Choose your password lenght (9-13) ")) 
uppercase = input ("Add uppercases?(Yes or No) ")
lowercase = input ("Add lowercase?(Yes or No) ")
numbers = input ("Add numbers?(Yes or No) ")
symbols = input ("Add symbols?(Yes or No) ")
characters = []

import string
uppercase_list = list(string.ascii_uppercase)
lowercase_list = list(string.ascii_lowercase)
numbers_list = [1,2,3,4,5,6,7,8,9,0]
symbols_list = list(string.punctuation)

if uppercase == "Yes": 
    characters = characters + uppercase_list
if lowercase == "Yes": 
    characters = characters + lowercase_list
if numbers == "Yes": 
    characters = characters + numbers_list
if symbols == "Yes": 
    characters = characters + symbols_list

import random
password = "".join(random.choices(characters, k=lenght))

print (password)



