num1 = int(input("Escolha um número"))
num2 = int(input("Escolha um número"))
num3 = int(input("Escolha um número"))
num4 = int(input("Escolha um número"))
num5 = int(input("Escolha um número"))

maior = num1
menor = num1

if num2 > maior:
    maior = num2
if num3 > maior:
    maior = num3
if num4 > maior:
    maior = num4
if num5 > maior:
    maior = num5

if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3
if num4 < menor:
    menor = num4
if num5 < menor:
    menor = num5

print("Maior:", maior)
print("Menor:", menor)