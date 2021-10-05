# Exercício 1: Dada uma lista, descubra o menor elemento. 
# Por exemplo, [5, 9, 3, 19, 70, 8, 100, 2, 35, 27] deve retornar 2

def buscaMenor(data):
  i = float("inf")
  for j in data:
    if j < i:
      i = j
  return i

print("busca menor elemento em [1,500,789,32] : " ,buscaMenor([1,500,789,32]))


### Exercício 2: Faça um programa que, dado um valor n qualquer
# , tal que n > 1 , imprima na tela um triângulo retângulo com 
# n asteriscos de base. Por exemplo, para n = 5 o triângulo
#  terá 5 asteriscos na base:

def printTriAst(num): 
  for i in range(num + 1):
       print("*" * i )

printTriAst(5)


# Crie uma função que receba um número inteiro N e retorne o
#  somatório de todos os números de 1 até N .
#  Por exemplo, para N = 5 , o valor esperado será 15 .

def summation(num):
  sum = 0
  for i in range(0, num+1):
    sum += i
  return sum

print("somatorio de 1 á 6 = ", summation(6))

# Exercício 4: Um posto está vendendo combustíveis com a 
# seguinte tabela de descontos:
#  Álcool:
#    - Até 20 litros, desconto de 3% por litro;
#    - Acima de 20 litros, desconto de 5% por litro.
#  Gasolina:
#    - Até 20 litros, desconto de 4% por litro;
#    - Acima de 20 litros, desconto de 6% por litro.

#Escreva uma função que receba o número de litros vendidos, o tipo de combustível
#  (codificado da seguinte forma: A - álcool, G - gasolina), e retorne o 
# valor a ser pago pelo cliente, sabendo-se que o preço do litro da gasolina 
# é R$ 2,50, e o preço do litro do álcool é R$ 1,90.

def totalPrice( l, fuel ):
  if fuel == "A":
    p = 1.9 * 0.97
    if l > 20:
      p = 1.9 * 0.95
  elif fuel == "G":
    p = 2.5 * 0.96
    if l > 20:
      p = 2.5 * 0.94
  
  return p * l    

print("21L de Gasolina", totalPrice(21, "G"))
print("19L de Gasolina", totalPrice(19, "G"))

print("21L de Alcool", totalPrice(21, "A"))
print("19L de Alcool", totalPrice(19, "A"))

