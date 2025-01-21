
#* we need save the list values/10 in a new list

temps = [221,234,340,230, -9999];

#*-----------Traditional way-------------
# creating empty list
# new_temps = [];

# for tem in temps:
#     new_temps.append(tem/10);
    
# print(new_temps);

#*---------comprehension way--------------------

#creating new list with comprehension
# new_temps = [temp/10 for temp in temps];

# print(new_temps)

#* ---------comprehension with conditionals----------

new_temps = [temp/10 for temp in temps if temp != -9999]

#print new_temps list
print(new_temps)
