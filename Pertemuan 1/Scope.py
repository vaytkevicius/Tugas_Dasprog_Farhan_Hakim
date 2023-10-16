x = 10
def my_function():
  x = 10
  print(x)

def outer_function():
  y = 20 # y is in the enclosing scope
  def inner_function():
    print(y) # inner_function can access y from the enclosing scope

z = 30 # z is in the global scope
def another_function():
 print(z) # another_function can access z from the global scope

print(len("Hello, World!")) # len is a built-in function