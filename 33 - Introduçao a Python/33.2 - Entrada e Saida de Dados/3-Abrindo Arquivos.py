file = open("arquivo.txt", mode="w")
file.write("nome idade\n")
file.write("Maria 45\n")
file.write("Miguel 33\n")

print("Túlio 22", file=file)
print("Teste", file=open("teste.txt", mode="w"))



