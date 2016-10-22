#Programa para hacer girar la luna entorno a la tierra
import math
def acelera (a, b):
	return a+b
def fuerza (x, y):
	fuerza = math.sqrt (x**2 + y**2)
	return (fuerza)


dias = int(input("Introduce el tiempo total de la simulación (días): "))
incremento = int(input("Introduce el incremento en cada paso del tiempo (s): "))
mt = 5.972*10**24
ml = 7.349*10**22
num = math.sqrt (4**2 + 3** 2)
print (num)

x= int(input("Eje x: "))
y = int(input("Eje y: "))
fuerxa = fuerza (x, y)
print (fuerxa)

print (mt)
print (ml)
while dias <= 0 or incremento <= 0:
	print ("Vuelve a introducir los datos.")
	dias = int(input("Introduce el tiempo total de la simulación (días): "))
	incremento = int(input("Introduce el incremento en cada paso de tiempo (s): "))
	
