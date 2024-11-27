## Niedferson Vargas

## Valor Absoluto


def valor_absoluto (x):
    if x >= 0:
        valor = x
    else:
        valor = -x
    return valor 

x = float(input("Ingrese un numero real x: "))
valor_abs = valor_absoluto(x)
print("")

## Condicional (Que mierda es elif)

## Buscar que es un while


i = 0
while(i <= 10):
    print("Este numero es el",i)
    i = i + 1

## problema 3

x = int(input("Ingrese un numero entero de 1 hasta el 255 "))

while(90 <= x <= 255):
    x = x + 1
    s = chr(int(x))
    print("Su simbolo es ",s)

## Otra actividad (Que estrés)
precio = 15 
cantidad = int(input("Cuantos panes va a llevar? "))
total = precio * cantidad

if(cantidad >= 5):
     porcentaje = total * 0.05
precio_total = cantidad * precio - porcentaje
print("El precio total es de",precio_total)

## Buscar (merch)