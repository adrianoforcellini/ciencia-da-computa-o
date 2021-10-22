def iterative_reverse(list):
    reversed_list = []
    for item in list:
        reversed_list.insert(0, item)
    return reversed_list

def reverse(list):
    if len(list) < 2:
        return list
    else:
        return reverse(list[1:]) + [list[0]]    

def iterative_countdown(n):
   while n > 0:
       print(n)
       n = n - 1
   print("FIM!")

   return n

def iterative_factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact


iterative_factorial(5)


# NOTA : APESAR DE MAIS ELEGANTE, RARAMENTE
#   A PERFORMANCE É MELHOR. 
# DE PREFERENCIA Á ITERATIVIDADE!!