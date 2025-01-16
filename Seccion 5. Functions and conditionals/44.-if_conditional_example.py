
# Validadndo función para trabajar con diccionarios
def mean (value):
    #evaluando si el tipo del argumento es un diccionario
    if(type(value) == dict):
        the_mean = sum(value.values()) / len(value);
    else:    
        the_mean = sum(value) / len(value)
        
    return the_mean;
    


# initializing dictionary
student_grades = {'Mary':9.1, 'Sim': 8.8, 'John': 7.5}

#llamando a la funcion enviando el diccionario como argumento
print(mean(student_grades))