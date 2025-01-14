
#inicializando lista
monday_temperatures = [9.1, 8.8, 7.5];
#                       0   1   2

#*------------Metodo recomendado----------------
#accediendo a alementos de la lista
#primer elemento
print('[0]', monday_temperatures[0]);

#segundo elemento
print('[1]', monday_temperatures[1]);

#tercer elemento
print('[2]', monday_temperatures[2]);

#*------------Metodo NO recomendado----------------
#accediendo con metodos generalesde listas (no recomendable)
#accediendo a la primera posición con metodo __getitem__
aux = monday_temperatures.__getitem__(0); 

print('primera posicion con __getitem__', aux)
