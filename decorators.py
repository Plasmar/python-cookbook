##################################################################
##                                                              ##
##  Name        :       decorators.py                           ##
##  Date        :       09.17.2019                              ##
##  Author:     :       Cameron M Merrick                       ##
##  Description :       Shows example usage of decorators       ##
##                                                              ##
##################################################################

def decorator_function(original_func):
    def wrapper_func():
        print("wrapper function executed before {}".format(original_func.__name__))
        return original_func()
    return wrapper_func

def decorator_func(original_func):
    def wrapper_func(*args, **kwargs):
        print("wrapper function executed before {}".format(original_func.__name__))
        return original_func(*args, **kwargs)
    return wrapper_func



@decorator_function
def display():
    print("[*] Display()")


@decorator_func
def display_func(name, favorite_color):
    print("[*] Display() Function:")
    print(name)
    print(favorite_color)

display()
display_func("sam", "orange")
