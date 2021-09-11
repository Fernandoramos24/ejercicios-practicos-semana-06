descuento=0
precio = float(input("digite precio: "))
dia = input("ingrese dia de la semana")

if dia=="martes" or dia=="jueves":
    descuento = precio * 0.15

preciofinal = precio - descuento
print("el precio final a pagar es de $", preciofinal,"con un descuento de",descuento)