global_var = 10 # Global variable

def modify_global():
    global global_var # Use the global keyword to MODIFY the global variable
    global_var = 20

modify_global()
print(global_var) # This will print the modified global variable, which is 20