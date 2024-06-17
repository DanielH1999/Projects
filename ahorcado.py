import random

word_list = ["contra","auto","camino","ayuda","primera","hacia","vi","miedo","adiós","primero","debería","poder","niños","sería","historia","hey","mientras","ciudad","dijiste","espero","cuánto","esposa","pronto","chicos","cualquier","viejo","debemos","deja","año","muerte","hablando","manos","da","loco","problemas","mano","guerra","semana","pasar","vale","cuál","viene","volver","toma","caso","agua","haré","vete","entiendo","horas","personas","capitán","adelante","niño","listo","noches","buenos","iba","juntos","dame","único","déjame","cerca","otros","sigue","grande","arriba","jefe","habla","supongo","manera","quieren","feliz","significa","sangre","fin","bajo","llama","venir","morir","importante","hiciste","ojos","escucha","entrar","ningún","corazón","diablos","necesitamos","atrás","durante","dices","nuestros","persona","abajo","dr","hija","dejar","necesita","llegar","hago","señora","haya","suficiente","doctor","gustaría","tierra","cara","siquiera","genial","cree","supuesto","tomar","equipo","justo","juego","ninguna","matar","cinco","dicen","amo","cuándo","pequeño","algunos","conozco","clase","maldito","unas","muchos","hubiera","segundo","aunque","pueda"]
board = []
wrong_letters = []

def select_word():
    return word_list[random.randint(0, len(word_list)-1)]

def draw_board():
    print(str(board).replace("'","")) #make it neater "['s','t','r']" -> "[s,t,r]"

def update_board(word, user_letter):
    if user_letter not in word:
        wrong_letters.append(user_letter)
        print("te equivocaste: ", wrong_letters)
    else:
        for index in range((len(word))):        #Search for every occurrence of that letter
            if user_letter in word[index]:
                board[index] = user_letter      #Display said letter every time
    draw_board()

def get_letter():
    letter = str(input("Elegi una letra: "))
    letter = letter[0]                      #Make sure it is only 1 character
    if letter not in wrong_letters:
        return letter
    else:
        return ""

def initiate_board(word):
    for letter in word:
        if letter is not word[0]:
            board.append("_")
        else:
            board.append(letter)
    draw_board();

def has_won():
    for character in board:
        if character == "_":
            return False
    return True

def main():
    word = select_word() #Select random word from a list

    user_letters = [word[0]] #Start a list of user given letters, append the first letter of the mistery word

    initiate_board(word) #Print the word with the first

    while(not has_won() and len(wrong_letters) < 6): #Game loop
        letter = get_letter()
        
        if letter not in wrong_letters\
         and letter != ""\
         and letter not in user_letters:

            user_letters.append(letter)
            update_board(word, user_letters[-1])
        
        else:
            print("¡Tu letra ya esta en el tablero!")

    if has_won():
        print("¡Ganaste!")
    else:
        print("¡Perdiste!")
    
main()