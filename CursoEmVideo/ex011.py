import math

n1 = int(input("Escolha um número inteiro:"))
n2 = int(input("Escolha outro número inteiro:"))
nReal = float(input("Escolha um numero real:"))

r1 = n1 * 2 * (n2 / 2)
r2 = n1 * 3 + nReal
r3 = nReal ** 3

print(f"O produto do dobro do primeiro com metade do segundo é igual a {r1}\n"
      f"A soma do triplo do primeiro com o terceiro é igual a {r2} \n"
      f"O terceiro elevado ao cubo é igual a {r3}")
