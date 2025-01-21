
#* opening files using "with"

#my_file is the variable name that will manipulate the file
with open("Seccion 11. File Procesing/fruits.txt", 'r') as my_file:
    #creating variable content that will containt the file information
    content = my_file.read();

print(content);