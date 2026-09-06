def decorator_function(original_function):
    def wrapper():
        print("Starting...")
        original_function()
        print("Finished...")
    return wrapper

@decorator_function
def hello():
    print("Hello")

hello()