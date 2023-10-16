if 'a' == 'a':
   def greet():
     return "Hello, World!"
else:
   def greet():
     return "Hi there!"

def say_hello():
   print("Hello, World!")

greeting = say_hello # Assigning the function to a different name
greeting() # Calls the function

def say_hello():
   print("Hello, Python!")

say_hello() # Calls the updated function

def divide_by_zero(a):
   result = divide_by_zero(5) # comment this and see the differences
print("After function is called/executed")