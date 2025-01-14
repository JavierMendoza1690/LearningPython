
#inicializando la lista
monday_temperatures = [9.1, 8.8, 7.5, 6.6, 9.9];

#accediento a la posicion 4
print('position 4 whith normal index', monday_temperatures[4]); #->9.9

#accediendo a la posicion 4 de atras a adelante
print('position 4 with negative index', monday_temperatures[-1]); #->9.9

#haciendo un slice desde el penultimo indice hasta el ultimo
print('position -2 to final', monday_temperatures[-2:]); #->[6.6, 9.9] 

