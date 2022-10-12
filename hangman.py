import random


def read_file(file_name):
    file = open(file_name,'r')
    return file.readlines()


def get_user_input():
    return input('Guess the missing letter: ')


def ask_file_name():
    file_name = input("Words file? [leave empty to use short_words.txt] : ")
    if not file_name:
        return 'short_words.txt'
    return file_name


def select_random_word(words):
    random_index = random.randint(0, len(words)-1)
    word = words[random_index].strip()
    return word


# TODO: Step 1 - update to randomly fill in one character of the word only
def random_fill_word(word):
    '''
    TODO
    '''
    index = random.randint(0, len(word)-1)#generates the random index for random letter
    random_letter = word[index].strip()#contains the random letter
    new_word=""

    #determines which letters that do not match the random letter and replace them with underscores
    for letters in word:
        if letters != random_letter:
            new_word+="_"

        else:
            new_word+=letters

    #finds the duplicate of random letter and replaces it with an underscore        
    if new_word.count(random_letter) == 2:
        return new_word.replace(random_letter,"_",1)

    return new_word


# TODO: Step 1 - update to check if character is one of the missing characters
def is_missing_char(original_word, answer_word, char):
    if char in answer_word :
        return False
    
    elif char in original_word:
        return True
    
    else:
        return False


# TODO: Step 1 - fill in missing char in word and return new more complete word
def fill_in_char(original_word, answer_word, char):
    '''
    TODO
    '''
    # stores the new updated word
    updated_word=""

    #determines what letter to update base on if it matches  the correct missing letter or not
    for letter in original_word:
        if letter in  answer_word:
            updated_word+=letter

        elif letter == char:
            updated_word+=letter
        
        else:
            updated_word+="_"
    return updated_word.strip()


def do_correct_answer(original_word, answer, guess):
    answer = fill_in_char(original_word, answer, guess)
    print(answer)
    return answer


# TODO: Step 4: update to use number of remaining guesses
def do_wrong_answer(answer, number_guesses):

    #decreases the number of guesses
    number_guesses-=1
    
    print('Wrong! Number of guesses left: '+str(number_guesses))
    draw_figure(number_guesses)
    return number_guesses
    


# TODO: Step 5: draw hangman stick figure, based on number of guesses remaining
def draw_figure(number_guesses):

    #stores hangman images in a list
    hangman_image = ['''/----
|
|
|
|
_______''','''
/----
|  0
|
|
|           
_______''','''
/----
|  0
|  |
|  |
|
_______''','''
/----
|  0
| /|\\
|  |
|
_______''',
"""/----
|   0
|  /|\\
|   |
|  / \\
_______"""]

    
    #diplays images according to list index 
    print(hangman_image[4-number_guesses])

# TODO: Step 2 - update to loop over getting input and checking until whole word guessed
# TODO: Step 3 - update loop to exit game if user types `exit` or `quit`
# TODO: Step 4 - keep track of number of remaining guesses
def run_game_loop(word, answer):

    #stores total number of guesses
    num=5
    print("Guess the word: "+answer)

    #runs until word is guessed correctly
    while word != answer:
    

        guess = get_user_input()

        #conditional logic
        if is_missing_char(word, answer, guess):
            answer = do_correct_answer(word, answer, guess)

        #exit game if user enters `exit` or `quit` as an input
        elif guess == "exit" or guess == "quit":
            print("Bye!")
            break
            
        # executes when user enters the wrong letter  
        else:
            num=do_wrong_answer(answer, num)

        # keeps track of number of guesses left  
        if  num==0:
            print(f"Sorry, you are out of guesses. The word was: {word}")
            break
            
        



# TODO: Step 6 - update to get words_file to use from commandline argument
if __name__ == "__main__":
    words_file = ask_file_name()
    words = read_file(words_file)
    selected_word = select_random_word(words)
    current_answer = random_fill_word(selected_word)

    run_game_loop(selected_word, current_answer)

