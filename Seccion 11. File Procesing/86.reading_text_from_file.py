#opening the file from vscode
myfile = open("Seccion 11. File Procesing/fruits.txt");

#reading file from vscode
# print(myfile.read());

#When reading the file the cursor is positioned at the end of the content, with no possibility of returning.

#one solution for print the content multiple times is to store the read in one variable
content = myfile.read();

#closing archive
myfile.close();

#printing results:
print(content);
print(content);