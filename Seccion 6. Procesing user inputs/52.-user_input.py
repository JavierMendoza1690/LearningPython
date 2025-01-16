
# definiendo la función temperatura:
def weather_condition(temperature):
    if temperature > 7:
        return 'Warm'
    else:
        return 'Cold'

#* Input
# se usa para leer usuarios que el usuario suministra por teplado
# la información suministrada en un input siempre es en formato string

#*--------- leyendo input y guardandolo en una variable---------
#lectura = input('Por favor ingrese un valor'); #la variable lectura guarda la informacion que se ingresa
#lectura es de tipo string a menos que se obligue a cambiar su tipo


#*--------------leyendo  input y forzando cambio de tipo a float--------
read_temperature = float( input(' ingrese temperatura: '));

#llamando a la función weather_condition
print(weather_condition(read_temperature));