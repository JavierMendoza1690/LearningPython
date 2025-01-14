
#* Functions

# para crear una funcion esta debe iniciar con la palabra def

#creando funcion llamada main (para calcular un promedio)
#la funcion recibe como parametro un argumento llamado mylist
#my_list es una lista que solo debe contener numeros
def mean (my_list):
    the_mean = sum(my_list) / len(my_list)
    return the_mean;

# initializing a list
this_is_a_list = [1,4,5];

#llamando a la función mean, y enviando la lista como argumento
#importante que la lista solo debe contener valores numericos
print(mean(this_is_a_list));