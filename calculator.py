def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Kan ej dividera med noll!")
    return a / b

if __name__ == "__main__":
    print(add(5,3))
    print(subtract(7, 5))
    print(multiply(5, 5))
    print(divide(8, 2))
