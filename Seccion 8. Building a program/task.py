
# something = '';
# final_word='';
# while(True):
#     something = input('Say something: ');
    
#     if(something == '\end'):
#         break;
#     else:
#         final_word += something.capitalize();
#         final_word +='. '
#         continue;

# print(final_word);

# *Metodo profesor

def sentence_maker(phrase):
    capitalized = phrase.capitalize();
    
    interrogative = ('how', 'what', 'why');
    
    if(phrase.startswith(interrogative)):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)
        
results = [];    
        
while True:
    user_input = input("Say something: ");
    if(user_input == '\end'):
        break;
    else:
        results.append(sentence_maker(user_input));

# uniendo las cadenas del arreglo results con un espacio intermedio    
print(" ".join(results));