def sec_decor(func):
    def wrapper():
        print("Chocolate")
        func()
    return wrapper

def decor(func):
    def wrapper():
        print("Strawberry")
        func()
    return wrapper

@sec_decor
@decor
def get_icecream():
    print("Icecream")

if __name__ == "__main__":
    get_icecream()
