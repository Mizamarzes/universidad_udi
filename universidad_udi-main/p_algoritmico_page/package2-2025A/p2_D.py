numeros = []

for i in range(4):
    n = int(input())
    numeros.append(n)

contador = 0

for i in range(4):
    for j in range(i+1, 4):         
        suma = numeros[i] + numeros[j]
        for k in range(4):         
            if k != i and k != j and suma == numeros[k]:
                contador += 1

if contador > 0:
    print("SI", contador)
else:
    print("NO 0")
