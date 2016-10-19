#Programa para hacer girar la Luna entorno a la Tierra
def acelera (a, b):
	return a+b

dias = int(input("Introduce el tiempo total de la simulación (días): "))
incremento = int(input("Introduce el incremento en cada paso del tiempo (s): "))
mt = 5,972*10**24		#Masa de la Tierra
ml = 7,349*10**22		#Masa de la Luna


while dias < 0 or incremento < 0:
	print ("Vuelve a introducir los datos.")
	dias = int(input("Introduce el tiempo total de la simulación (días): "))
	incremento = int(input("Introduce el incremento en cada paso de tiempo (s): "))
	
