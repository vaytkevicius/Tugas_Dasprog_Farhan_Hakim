def product(a, b):
    print(a * b)
def product(a, b, c):
   print(a * b * c)
# product(4, 5) # Uncommenting this shows an error

product(4, 5, 5) # This line will call the last function
# Try using *args to solve that problem