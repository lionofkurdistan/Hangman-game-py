import random 

with open('textlist.txt', 'r') as f:
  word = f.readlines()
  
  
word = random.choice(word)[:-1]


allowed_errors = 7
guesses = []
done = False


while not done :
  for letter in word:
    if letter.lower() in guesses:
      print(letter, end=" ")
      else:
        print("_", end="_")
        print("")
        
        guess = input(f"Allowed Errors Left {allowed_errors}, next Guess: ")
        guesses.append(guess.lower())
        if guess.lower() not in word.lower():
          allowed_errors -= 1
          if allowed_errors == 0:
            break
          
    done = True
     for letter in word:
       if letter.lower() not in guesses:
         deon = False 
        
      
if done:
  print(f"You found the word! It was {word}! ")
else:
  print(f"Game over! The word was {word}!")
