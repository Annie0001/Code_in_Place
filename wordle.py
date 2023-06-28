import random

word_dictionary=["ghost","brand","break","chain","crown","sharp","solid","goose","horse","peace","lease","knife","ankle","crave","flute","audit","digit","habit","fruit","debit"]

def choose_dictionary_word():
  random_item = random.choice(word_dictionary)
  return random_item

# check for the existance of any character 
def character_exists():
  if user_input[i] in random_word:
    return True
  return False

random_word=choose_dictionary_word()
print(random_word)

for i in range(6):
  user_input= input("Please enter 5 character word: ")

  if len(user_input) != 5:
    print("Please enter the 5 character word.")
    break

  if user_input == random_word:
    print("Great Job. You guessed it!!!")
    break
  
  # Declares the correct place for each character 
  for i in range(len(user_input)):
    character_exists_storage = character_exists()
    #if character_exists_storage == True:
      #print(user_input[i] ,"exists")
    if character_exists_storage == True and user_input[i] == random_word[i]:
      print(str(user_input[i]) + " Character exists and it is in the right place.")
    elif character_exists_storage == True and user_input[i] != random_word[i]:
      print(str(user_input[i]) + " Character exists but not in the right place.")
    else:
      print(str(user_input[i])+ " Does not exist")
