
word_list = ['red','green','yellow']
import random
choosen_word = random.choice(word_list)
guess = input("Guess a letter : ")
for letter in choosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")    