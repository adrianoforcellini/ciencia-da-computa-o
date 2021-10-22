# Exercício 1: Crie um algoritmo não recursivo para contar quantos números 
# pares existem em uma sequência numérica (1 a n).

def count_pairs_numbers_in_range(final_number):
  count = 0
  for number in range(final_number):
    if number % 2 == 0:
      count += 1     
  return count

# Exercício 2: Transforme o algoritmo criado acima em recursivo.

def recursively_count_pairs_numbers_in_range(final_number):
  if final_number == 1:
    return 0
  elif final_number % 2 == 0:
    return 1 + recursively_count_pairs_numbers_in_range(final_number-1)
  else:
    return recursively_count_pairs_numbers_in_range(final_number-1)

## Ironicamente ficou mais simples a iterativa

# Exercício 3: Crie um algoritmo recursivo que encontre,
#  em uma lista, o maior número inteiro.

def maiorinteiro_aux(lista, tamanho):
    if tamanho == 1:
        return lista[0]
    else:
        maior_do_resto_da_lista = maiorinteiro_aux(lista, tamanho-1)
        if maior_do_resto_da_lista > lista[tamanho-1]:
            return maior_do_resto_da_lista
        else:
            return lista[tamanho-1]


def maiorinteiro(lista):
    tamanho = len(lista)
    return maiorinteiro_aux(lista, tamanho)
    


print(maiorinteiro([1, 21, 300, 4, 57]))