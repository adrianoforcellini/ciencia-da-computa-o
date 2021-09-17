# Exercício 1: Faça um programa que receba um 
# nome e imprima o mesmo na vertical em escada invertida
import random
def invertScalPrint(name):
  for i in range(len(name)):
    print(name[slice(-i)])

invertScalPrint('adrian')


# Exercício 2: Jogo da palavra embaralhada. Desenvolva um jogo em que a
# pessoa usuária tenha que adivinhar uma palavra que será mostrada com as
# letras embaralhadas. O programa terá uma lista de palavras e escolherá
# uma aleatoriamente. O jogador terá três tentativas para adivinhar a palavra.
# Ao final a palavra deve ser mostrada na tela, informando se a pessoa
# ganhou ou perdeu o jogo.

def scrambledWordGame():
  word = random.choice(["prismatic", "assiduous", "wonderful"]) 
  scrambled_word = "".join(random.sample(word, len(word)))
  attempts = 0
  while (attempts < 3):
   x = (input("Scrambled word is: %s, what word is it?   " %scrambled_word))
   attempts += 1
   if attempts == 3:
    print("Correct answer is '%s'" %word) 
   if x == word:
     print('You Win!!')
     break

scrambledWordGame()