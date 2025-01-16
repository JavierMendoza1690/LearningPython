

#adding the correspondings inputs
name =      input('Enter your name: ');
surname =   input('Enter your surname: ')

#concating by old method
message = "Hello %s %s!" % (name, surname);

# print(message);

#concating bt new method
message_new = f"Hellos {name} {surname}!";

print(message_new);

#* There is also another way to format strings using the "{}".format(variable) form. Here is an example:

# name = "John"
# surname = "Smith"
 
# message = "Your name is {}. Your surname is {}".format(name, surname)
# print(message)
# Output: Your name is John. Your surname is Smith