#Programa para hacer girar la luna entorno a la tierra
dias = int(input("Introduce el tiempo total de la simulación (días): "))
incremento = int(input("Introduce el incremento en cada paso del tiempo (s): "))
while dias < 0 or incremento < 0:
	print ("Vuelve a introducir los datos.")
	dias = int(input("Introduce el tiempo total de la simulación (días): "))
	incremento = int(input("Introduce el incremento en cada paso de tiempo (s): "))
