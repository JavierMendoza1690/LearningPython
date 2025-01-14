
#* Nota:
#la palabra self en los metodos hace referencia a la propia funcion o metodo, aunque se 
#muestre que hay que enviarla como argumento, no debe enviarse, ya que hace referencia a la misma función

#* Funciona append
#agrega un elemento al final de una lista

# inicializando una lista:

monday_temperatures = [9.1, 8.8, 7.5];

#verificando la lista de metodos que tienen las listas por defecto
# print(dir(monday_temperatures));

#Verificando que hace el metodo append
# print(help(monday_temperatures.append)); #-> agrega un elemento al final de la lista


#agregando un nuevo elemento a la lista monday_temperatures
monday_temperatures.append(8.1);

#imprimiendo resultado
print('after append 8.1:', monday_temperatures);

#* Función clear
# la función clear remueve todos los elementos de una lista

#Removiendo todos los items de la monday_temperatures
monday_temperatures.clear();

#imprimiendo resultado
print('after clear:',  monday_temperatures)

#* Función Index
#retorna el indice de un valor buscado en la lista
# index(self, value, start=0, stop=9223372036854775807, /)
# el valor start indica de que termino empezará a buscar
#el valor stop indica el elemento donde dejará de buscar, por defecto estan inicializados
# es decir, no son argumentos que se necesiten enviar con obligatoriedad

#re-inicializando la lista
monday_temperatures = [9.1, 8.8, 7.5];

#buscando el indice del valor 8.8
position = monday_temperatures.index(8.8);

#imprimiendo el indice encontrado
print('el indice en el que se encuenta el 8.8 es:', position);

print(help(monday_temperatures.remove))

