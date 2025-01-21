
#* Appending text in an existing file
# for append a new text line, we should open the file in mode 'a'
# if we needeed read and write in the file we need add + to the mode (a+)

with open('Seccion 11. File Procesing/vegetables.txt', 'a+') as my_file:
    my_file.write('\nOkra')
    #bringin the cursor to the initial position
    my_file.seek(0);
    #reading a new line in where the cursor is currently located
    content = my_file.read();
    #closing the variable my_file
    my_file.close();
    
    print(content);