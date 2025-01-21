
#* writting in a file
# the w represents that the file will be writable, by default it is in r that represents reading
# if the file does not exist it will create it
# if the file exist it will be overwritten
with open('Seccion 11. File Procesing/vegetables.txt', 'w') as myfile:
    #writing in the file
    #\n represents a line break
    myfile.write('Tomato\ncucumber\n')
    #this writting will be done in the next line
    myfile.write('Garlic')
    #closing the file
    myfile.close();