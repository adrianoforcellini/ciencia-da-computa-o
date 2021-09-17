# Exercício 1: Faça um programa que receba um 
# nome e imprima o mesmo na vertical em escada invertida

def invertScalPrint(name):
  for i in range(len(name)):
    print(name[slice(-i)])

invertScalPrint('adrian')