from hangman_palavras import word_list
from hangman_estagios import estagios
from hangman_arte import logo
import random

#Step 1 

lista_palavras = ["ameixa", "boomerang", "camel"]

#Todo-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

palavra_escolhida = random.choice(word_list)
tamanho_da_palavra = len(palavra_escolhida)
fim_do_jogo = False
vidas = 6

print(logo)

# print(f"A palavra escolhida é {palavra_escolhida}.")

#Todo-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

mostrar = []
for _ in range(tamanho_da_palavra):
    mostrar += "_"

while not fim_do_jogo:
    advinhar = input("Advinhe a letra:").lower()

    if advinhar in mostrar:
        print(f"Voce já advinhou está letra. {advinhar}")

    for posicao in range(tamanho_da_palavra):
        letra = palavra_escolhida[posicao]
        # print(f"Posição atual:{posicao}\nLetra atual:{letra}\nLetra advinhada:{advinhar}")
        if(letra == advinhar):
            mostrar[posicao] = letra

    if advinhar not in palavra_escolhida:
        print(f"Voce advinhou {advinhar}, está não é a letra. Voce perdeu um vida!")
        vidas -= 1
        if vidas == 0:
            fim_do_jogo == True
            print("Voce perdeu!")

    print(f"{' '.join(mostrar)}")
    
    if "_" not in mostrar:
        fim_do_jogo = True
        print("Voce venceu!")

    print(estagios[vidas])