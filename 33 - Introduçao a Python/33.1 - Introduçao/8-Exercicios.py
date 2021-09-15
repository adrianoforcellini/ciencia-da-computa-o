## Exercício 1: Crie uma função que receba dois números e retorne o maior deles.
## Exercício 2: Calcule a média aritmética dos valores contidos em uma lista.

## Exercício 3: Faça um programa que, dado um valor n qualquer,
#  tal que n > 1 , imprima na tela um quadrado feito de asteriscos
#  de lado de tamanho n . Por exemplo:

def maior(num1,num2):
    max = num1
    if num2 > max:
        max = num2
    return max

print("maior entre um e tres:", maior(1,3))
print("maior entre nove e tres:",maior(9,3))

def avg(data):
  return sum(data)/len(data)

print("média entre os itens de [1,2]:", avg([1,2]))
print("média entre os itens de [1,2,3]:", avg([1,2,3]))

def printAst(num): 
  for i in range(num):
       print("*" * num)

printAst(6)