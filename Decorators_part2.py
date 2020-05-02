def decorator_func(any_function):
    def wrapper_function(*args, **kwargs):
        print("This is awesome function")
        any_function(*args, **kwargs)
    return wrapper_function
@decorator_func
def func(a):
    print(f"This is function with agrument {a}")
func(7)

def decorator_func(any_function):
    def wrapper_function(*args, **kwargs):
        print("This is awesome function")
        return any_function(*args, **kwargs)
    return wrapper_function

@decorator_func
def add1(a, b):
    return a+b

print(add1(2, 5))
func(10)


from functools import wraps

def decorator_func(any_function):
    @wraps(any_function)
    def wrapper_function(*args, **kwargs):
        print("This is awesome function")
        return any_function(*args, **kwargs)
    return wrapper_function


@decorator_func
def add1(a, b):

    ''' This is add function'''

    return a+b

print(add1.__doc__)
print(add1.__name__)



from functools import wraps

def decorator_func1(any_function):
    @wraps(any_function)
    def wrapper_function(*args, **kwargs):
        print(f"Out put \nyou are calling {any_function.__name__} function")
        print(f"{any_function.__doc__}")
        return any_function(*args, **kwargs)
    return wrapper_function


@decorator_func1
#@print_function_data
def add2(a, b):
    '''This is a function takes two numbers as arguments and return their sum'''
    return a+b

print(add2(4, 125))

######## practice

from functools import wraps
import time
def decorator_func2(any_function):
    @wraps(any_function)
    def wrapper_function(*args, **kwargs):
        print(f"Executing ...{any_function.__name__}")
        t1 = time.time()

        return_value = any_function(*args, **kwargs)

        t2 = time.time()
        total_time = t2-t1

        print(f"This function took {total_time} seconds")
        return return_value

    return wrapper_function

@decorator_func2
def square_finder(n):
    return [i**2 for i in range(1, n+1)]
square_finder(1000)



#practice 2

# only int allow
from functools import wraps

def only_int_allow(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        data_type = []
        for arg in args:
            data_type.append(type(arg)==int )
        if all(data_type):
            return function(*args, **kwargs)
        else:
            print("invalid agruments")

    return wrapper

@only_int_allow
def add_all(*args):

    total = 0
    for i in args:
        total +=i
    return  total
print(add_all(1, 2, 3, 4, 5, [1, 2, 3]))




def only_int_allow(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        if all([type(arg)== int for arg in args]):
            return function(*args, **kwargs)
        print("invalid agruments")
  #      data_type = []
   #     for arg in args:
    #        data_type.append(type(arg)==int )
     #   if all(data_type):
      #      return function(*args, **kwargs)
       # else:


    return wrapper

@only_int_allow
def add_all(*args):

    total = 0
    for i in args:
        total +=i
    return  total
print(add_all(1, 2, 3, 4, 5))


## practice


from functools import wraps

def only_data_type_allow(data_type):
    def only_int_allow1(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            if all([type(arg) == data_type for arg in args]):
                return function(*args, **kwargs)
            print("invalid agruments")

        return wrapper
    return only_int_allow1


@only_data_type_allow(str)
def string_join(*args):
    string= ""
    for i in args:
        string+=i
    return string
print(string_join("Anoop", "Singh"))

