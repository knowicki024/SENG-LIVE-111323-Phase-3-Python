# 1. ✅ Demonstrate First Class Functions
    # Create functions to be used as callbacks 
    # Create a higher-order function that will take a callback as an argument

def dance(music):
    print(f"we dance to {music}")

def listen(music):
    print(f"we listen to {music} and love {music}! ")

#higher order function that takes callback as a param 
def activate_fun(callbackfunc):
    #callback function invocation 
    return callbackfunc("Prince")

activate_fun(dance) # 
activate_fun(listen) #

# 2. ✅ Create a higher-order function that returns a function




# 3. ✅ Demonstrate a decorator
# Create a function that takes a function as an argument, has an inner function, and returns the inner function
# Demo examples of the decorator with and without pie syntax '@'

    # Without pie syntax 


    # With pie syntax

def my_decorator_outer_function(func):
    def inner_function():
        print(" ---- 1 before ----")
        func()
        print( " ----- 3 after ----")
    return inner_function

@my_decorator_outer_function
def say_hello():
    print(" 2 hello!! ")

say_hello()


###################

def fun_decorator(func):
    def wrapper(*args, **kwargs): #arbitrary arguments
        result = func(*args, **kwargs)
        print( f" wow, {result}, this is exciting----")
        return result 
    return wrapper 

@fun_decorator
def generate_random_number():
    import random
    return random.randint(1, 100)

@fun_decorator
def greet(name):
    return f"hello, {name}"

random_result = generate_random_number()
greeting_result = greet("Steven")