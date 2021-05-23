# Write your code here
import random


def play_game(play_exit):
    if play_exit == "play":

        list_of_words = ['python', 'java', 'kotlin', 'javascript']

        word1 = random.choice(list_of_words)
        #word = input()
        replace_word = (len(word1)) * "-"
        i = 0
        
        letter_list = ""
        while i <= 7:
            print("")
            print(replace_word)
            letter = input('Input a letter: ')

        #checking user put just one letter
            if len(letter) != 1:
                print("You should input a single letter")
                i = i
                continue
            
            #checking if the input letter is in lowercase
            elif letter.isupper() or not letter.isalpha() or letter.isspace():
                print("Please enter a lowercase English letter")
                i = i
                continue

            #checking if letter was already guessed
            elif letter in letter_list:
                print("You've already guessed this letter")
                i = i
                continue

            #if the input letter is right
            a=""
            place = 0
            if (letter in word1)  and word1.count(letter) > 1:
                for a in word1:
                    if a == letter:
                        replace_word = replace_word[:place] + letter + replace_word[place+1:]
                        i=i
                    place += 1 
            elif letter in word1:
                place = word1.index(letter)
                replace_word = replace_word[:place] + letter + replace_word[place+1:]
                i=i
            #if input letter is not the word
            else:
                print("That letter doesn't appear in the word")
                i += 1
            
            #if the full word is guessed
            if replace_word == word1:
                print(f"You guessed the word {replace_word}!")
                break
            letter_list = letter_list + letter
            
        if replace_word == word1:
            print("You survived!")
        else:
            print("You lost!")
    elif play_exit == "exit":
        pass

print("H A N G M A N")
print("")

play_exit = input('Type "play" to play the game, "exit" to quit: ')

if play_exit == ("play" or "exit"):
    play_game(play_exit)
else:
   play_exit = input('Type "play" to play the game, "exit" to quit: ') 


