
#*arbitrary number keywords arguments
#this way generate a dictionary as a response
#key: vale ->key is string

# def mean(**kwargs):
#     return kwargs

# that generates an error, they should be key arguments only
# print(mean(1,2,3)); #->error

# correct way
# print(mean(a=2,b=3, c=1));

#* example keywords arguments

# Enter the correct parameters inside find_sum() so that the output of the code is 9.
def find_sum(**kwargs):
    return sum(kwargs.values())
    
print(find_sum(a=9))