
# *args indicates that it can receive any number of arguments
def mean(*args):
    #when arguments are sent in this way they become a tuple
    return sum(args) / len(args);

print (mean(1, 2, 3));