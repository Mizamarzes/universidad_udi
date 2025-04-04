N = float(input("Escribe la distancia en metros: "))

cantidadCorredores = 0
sumaVelocidades = 0

minutos = 3215
seg = 9320

while minutos != 0 and seg != 0:
    minutos, seg = map(int, input("Escribe los minutos y segundos separados con una coma: ").split(","))
    seg = (minutos * 60) + seg
    velocidad = N / seg

    cantidadCorredores = cantidadCorredores + 1
    sumaVelocidades = sumaVelocidades + velocidad
    print(f"La velocidad del corredor {cantidadCorredores} es: {velocidad: .2f} metros/segundos")

velocidadMedia = sumaVelocidades / cantidadCorredores
print(f"La velocidad media es: {velocidadMedia: .2f} metros/segundo")
    

