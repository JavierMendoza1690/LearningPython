
# *Sumando elementos de un una lista

# Definiendo la lista 
student_grades = [9,1, 8.8, 7.5];

#verificando funciones globales dentro de python
# print(dir(__builtins__));  #retorna todas las funciones que vienen por defecto en el programa

#usando la funcion suma para sumar todos los elementos de una lista
mysum = sum(student_grades);

#retornando el numero de elementos que tiene la lista
length = len(student_grades) -1;

#calculando el promedio de las calificaciones de los estudiantes
mean = mysum / length;

#imprimiendo el promedio calculado
print(mean);
print(length);

