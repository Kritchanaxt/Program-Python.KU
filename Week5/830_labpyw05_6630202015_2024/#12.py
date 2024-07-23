
#* 12.

global_var = "T am a global variable"
def my_function():
    print("Inside the function", global_var)

my_function()
print("Outside the function", global_var)