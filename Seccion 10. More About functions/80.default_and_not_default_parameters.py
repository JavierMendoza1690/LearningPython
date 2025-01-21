
# A default parameter cannot be in the first position if there is a non-default parameter.

# defining area function
#a parameter is when the function arguments have initials values
#b is a parameter (overridable)

#* "a" is a non-default parameter
#* "b" is a default parameter
def area(a,b =4):
    return a*b;

#*invoking fuction with non-default parameters
#in this case the order of the parameters does not matter

#* 3 is a non-keyword(positional) argument
#* b=7 keyworkd argument
#the keywords should be next the non-keywords arguments
print(area (3, b=7))
