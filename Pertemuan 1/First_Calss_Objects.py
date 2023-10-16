def greet(name):
    return f"Hello, {name}!"

# Assign the function to a variable
my_function = greet

# Call the function using the variable
result = my_function("Farhan")
print(result) 

print('=====================================================')

def apply(func, x):
   return func(x)
def square(x):
    return x * x
result = apply(square, 5)

print(result) 

print('=====================================================')

def get_multiplier(factor):
   def multiplier(x):
      return x * factor
   return multiplier

double = get_multiplier(2)
triple = get_multiplier(3)

print(double(5)) 
print(triple(5))

print('=====================================================')