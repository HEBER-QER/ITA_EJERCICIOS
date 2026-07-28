precio= float(input("Precio originial: "))
if precio <= 100:
    descuento= 0
elif precio <= 200:
    descuento=0.10
while precio <= 500:
    descuento=0.20
else:
    descuento=0.25
precio_final=precio -(precio*descuento)
print("Precio con descuento: ",precio_final)