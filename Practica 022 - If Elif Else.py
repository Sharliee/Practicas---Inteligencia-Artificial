#Carlos Andres Riveramelo Del Toro
#20310382
#Practica 22 - Inteligencia Artificial

edad = int(input('¿Cuantos Años Tienes?\tTengo: '))
if edad <= 0:
	print('\nError, intento de chiste no valido.')
elif edad >= 1 and edad <= 17:
	print('\nSi no tienes los 18, a tu casa, a ver pocoyo.')
elif edad >= 18 and edad <= 45:
	print('\nFelicidades, eres mas legal que el cafe.')
elif edad >= 45 and edad <=100:
    print("\nEntre mas arrugada la pasa, mas dulce la fruta")
elif edad >= 100 and edad <=120:
    print("\nSi ves un tunel, no vayas a la luz.")
else:
	print('\nAlav, ¿Eres pariente de chabelo o que?20000.')