def modify_list(my_list):
    my_list.append(4) # Modifying the list inside the function

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list) 
print('=====================================================')

def reassign_list(my_list):
    my_list = [4, 5, 6] # Reassigning the list to a new object
my_list = [1, 2, 3]
reassign_list(my_list)
print(my_list) 
print('=====================================================')

def modify_integer(x):
    x += 1 # Modifying the integer inside the function

my_integer = 5
modify_integer(my_integer)
print(my_integer)
