
#* Diccionarios

#Temperaturas del dia lunes
monday_temperatures = [9.1, 8.8, 7.5];
# calificaciones de cada estudiante
student_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}

# extrayendo solo las claves-llave del diccionario
keys = student_grades.keys();

#extrayendo solo los valores del diccionario y almacenandolos en una lista
values_students = student_grades.values(); #-> dict_values([9.1, 8.8, 7.5])

#sumando los elementos extraidos en el paso anterior
mysum = sum(values_students);

#calculando el numero de elementos dentro de values_students
length = len(values_students);

#calculando el promedio de las calificaciones de los estudiantes
mean = mysum / length

#imprimiendo resultado
print(mean)
print(keys);

