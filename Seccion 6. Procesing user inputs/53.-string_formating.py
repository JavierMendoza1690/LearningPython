
#leyendo input y almacenando en user_input
user_input = input('Enter your name: ');

#concating by old method
message = "Hello %s!" %user_input;
# print(message)

#concating by new method (f-strings)
message_new = f"Hello {user_input}!";
print(message_new)