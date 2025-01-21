
#* Forma normal del ciclo while

#declarando variable
# username = '';
# while( username != 'pypy'):
#     username = input('Enter your username: ');
    
#* Forma con break y continue

#declarando variable username
username = '';
while True:
    username = input('Enter your username: ');
    #declarando condiciones
    #si el nombre es igual a pypy rompa el ciclo
    if( username == 'pypy'):
        break
    else:
        #si el nombre es diferente a pypy continue con la siguiente iteracion
        continue;
        print('hello') #->esta linea jamas se ejecuta
    
