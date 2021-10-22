# Os arrays tem sempre o mesmo tamanho
def multiply_arrays1(array1, array2):
    result = []
    for number1 in array1:
        for number2 in array2:
            result.append(number1 + number2)

    return result

# def multiply_array(numbers):
  # ...

# multiply_array(2_arrays_com_dois_mil_numeros)
# O tempo de execução deste algoritmo foi 0.45s

# multiply_array(2_arrays_com_quatro_mil_numeros)
# Já esse teve tempo de execução de 1.8s, cerca de quatro vezes maior.

def multiply_arrays(array1, array2):
    result = []
    number_of_iterations = 0

    for number1 in array1:
        print(f'Array 1: {number1}')
        for number2 in array2:
            print(f'Array 2: {number2}')
            result.append(number1 * number2)
            number_of_iterations += 1

    print(f'{number_of_iterations} iterações!')
    return result


meu_array = [1,2,3,4,5]

multiply_arrays(meu_array, meu_array)


# Repare como, para dois arrays de tamanho 5, temos 25 iterações! 
# Varie os números e veja como, sempre o número de iterações é n vezes n ,
# ou seja, n² ! Por isso, lá em cima, multiplicar por dois o tamanho da entrada, 
# de 2000 para 4000, multiplicou por quatro o tempo de execução: para um 
# algoritmo O(n²) , aumentar a entrada em n vezes, aumenta o tempo de execução
# em n² vezes!
