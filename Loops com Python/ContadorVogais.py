nome = str(input("Digite uma palavra: "))
vogal = "aeiou"
contador = 0

for i in nome:
    if i in vogal:
        contador = contador + 1

print(contador)