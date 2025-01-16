
#Validadndo función para trabajar con diccionarios
def mean (value):
    #*forma alternativa de verificar que sea un diccionario (valido para cualquier tipo de variable)
    if(isinstance(value, dict)):
        the_mean = sum(value.values()) / len(value);
    else:    
        the_mean = sum(value) / len(value)
        
    return the_mean;
    


# initializing dictionary
student_grades = {'Mary':9.1, 'Sim': 8.8, 'John': 7.5}

#llamando a la funcion enviando el diccionario como argumento
print(mean(student_grades))