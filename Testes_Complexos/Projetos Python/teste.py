lista = input().split(' ')

Ca = int(lista[0])
Ba = int(lista[1])
Pa = int(lista[2])

lista2 = input().split(' ')
Cr = int(lista2[0])
Br = int(lista2[1])
Pr = int(lista2[2])

somaTotal = 0
CaCr = Ca - Cr
BaBr = Ba - Br
PaPr = Pa - Pr

if CaCr < 0:
    somaTotal = somaTotal + (CaCr * -1)

if BaBr < 0:
    somaTotal = somaTotal + (BaBr * -1)

if PaPr < 0:
    somaTotal = somaTotal + (PaPr * -1)

print(somaTotal)
