#Ejercicio 6
print('Mi primer programa en python')

#Ejercicio 7
print('v\n \ne \n \nr \n \nt \n \ni \n \nc \n \na \n \nl')

#Ejercicio 8
print('*****\n*   *\n*   *\n*   *\n*****')

#Ejercicio 9 
print('*\n***\n*****\n*******\n*********')

#Ejercicio 10
dato = input('Dame un dato: ')
print(dato)

#Ejercicio 11
valor  = input()
print(f"******************************\n El resultado es: {valor}\n *****************************")

#Ejercicio 12:

#ejercicio 2 

#def fraccionMasUno(x,y):
#    return x/y + 1

x = float(input('x = '))
y = float(input('y = '))
resultado = x/y + 1
print(resultado)

#def fraccionSumRes(x,y):
#    return x+y/x-y

x = float(input('x = '))
y = float(input('y = '))
resultado = x+y/x-y
print(resultado)

#def fraccionSobreFraccion(x,y,z):
#    return (x + y/z) / (x -y/z)

x = float(input('x = '))
y = float(input('y = '))
z = float(input('z = '))
resultado = (x + y/z) / (x -y/z)
print(resultado)

#def corchetesYparentesis(x,y):
#    return ((x+y)**2)**2

x = float(input('x = '))
y = float(input('y = '))
resultado = ((x+y)**2)**2
print(resultado)

#Ejercicio 3
x = float(input('x = '))
y = float(input('y = '))
resultado = x + y
print(resultado)

#Ejercicio 4
float(input('tu valor elegido es: '))
y = x + 1 
print(y)

#Ejercicio 5
x = float(input('x = '))
z = float(input('z = '))
y = x + z /2
print(y)

#Ejercicio 13
montoinicial = float(input('Ingresa la cantidad que deseas ingresar: '))
meses = float(input('Ingresa el plazo de disposicion(en meses): '))
incremento = (montoinicial * 6/100) * meses
monto_a_devolver = montoinicial + incremento
print(f'Al finalizar tu plazo, el incremento el total a devolver sera de: {monto_a_devolver}')

#Ejercico 14

llamadas_totales = float(input("Ingresa el total de llamadas realizadas: "))
minutos = float(input("ingresa la cantidad de minutos utilizados: "))

NombreDelUsuario = {
    "Total de llamadas", llamadas_totales,
    "cantidad de minutos", minutos,
}

costo_final = (1.5 * minutos) + llamadas_totales * 12
print(f"El costo total es: {costo_final}")

#Ejercicio 15

sueldo_base = 42000

venta1 = int(input("De cuanto fue tu primera venta: "))
venta2 = int(input("De cuanto fue tu segunda venta: "))
venta3 = int(input("De cuanto fue tu tercera venta: "))

saldo_final = sueldo_base + venta1 *10 /100 + venta2 *10 /100 + venta3 * 10 /100
print(saldo_final)

#Ejercicio 16
segundos_del_dia = 24*60*60
segundos_de_una_hora = 60*60
print(f"Una hora tiene {segundos_de_una_hora} segundos, y un dia {segundos_del_dia}.")

segundos_para_calcular = int(input("Ingrese una cantidad de segundos: "))
segundos_a_minutos = print(round(segundos_para_calcular / 60)) 
segundos_a_horas = print(round(segundos_para_calcular/60/60))
segundos_a_dias = print(round(segundos_para_calcular/60/60/24))

#Ejercicio 17

lista_de_billetes = [100,200,500,1000]
retiro = int(input("Ingresa el monto a retirar: "))

billetes_1000 = retiro // 1000
resto_de_billetes = retiro % 1000
if resto_de_billetes => 500
print(f"el cajero solatara {billetes_1000} billetes de mil\n el cajero soltara {resto_de_billetes} en billetes menores")


#ejercicio 20
x = input("El valor de x es: ")
y = input("El valor de y es: ")
z = input("El valor de z es: ")

print(f"El valor de x es {x}, el valor de y es {y} y el valor de z es {z}")
