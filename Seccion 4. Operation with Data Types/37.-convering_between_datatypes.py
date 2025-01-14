#From tuple to list:

cool_tuple = (1, 2, 3)
cool_list = list(cool_tuple)
print(cool_list); #output->[1, 2, 3]


#From list to tuple:

cool_list = [1, 2, 3]
cool_tuple = tuple(cool_list)
print(cool_tuple); #(1, 2, 3)


#From string to list:

cool_string = "Hello"
cool_list = list(cool_string)
print(cool_list); #['H', 'e', 'l', 'l', 'o']


#From list to string:

cool_list = ['H', 'e', 'l', 'l', 'o']
cool_string = str.join("", cool_list)
print(cool_string); # 'Hello'