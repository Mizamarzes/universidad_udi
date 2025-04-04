cont = 0
acumulador = 0

mayor = None
menor = None

for i in range(10):
    x = int(input())
    cont += 1
    acumulador += x

    if mayor is None or x > mayor:
        mayor = x
    if menor is None or x < menor:
        menor = x

media = acumulador / cont
rango = mayor - menor

print(media, rango)

