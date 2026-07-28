cantidad = float(input("Cantidad en MXN: "))
print("Monedas: 1.USD 2.EUR 3.THB 4.JPY 5.KRW 6.AUD 7.PEN 8.CAD 9.VES 10.ARS")
opcion = int(input("Elige opción: "))

match opcion:
    case 1:
        resultado = cantidad / 16.5
        moneda = "USD"
        print("Convertido a: ",resultado,"USD")
    case 2:
        resultado = cantidad / 18.0
        moneda = "EUR"
        print("Convertido a: ",resultado,"EUR")
    case 3:
        resultado = cantidad / 0.45
        moneda = "THB"
        print("Convertido a: ",resultado,"THB")
    case 4:
        resultado = cantidad / 0.12
        moneda = "JPY"
        print("Convertido a: ",resultado,"JPY")
    case 5:
        resultado = cantidad / 0.013
        moneda = "KRW"
        print("Convertido a: ",resultado,"KRW")
    case 6:
        resultado = cantidad / 11.5
        moneda = "AUD"
        print("Convertido a: ",resultado,"AUD")
    case 7:
        resultado = cantidad / 2.8
        moneda = "PEN"
        print("Convertido a: ",resultado,"PEN")
    case 8:
        resultado = cantidad / 8.2
        moneda = "CAD"
        print("Convertido a: ",resultado,"CAD")
    case 9:
        resultado = cantidad / 0.0023
        moneda = "VES"
        print("Convertido a: ",resultado,"VES")
    case 10:
        resultado = cantidad / 0.046
        moneda = "ARS"
        print("Convertido a: ",resultado,"ARS")
    case _:
        print("Opción no válida")
        resultado = None