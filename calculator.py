"""A simple command line calculator."""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Simple Calculator")
    parser.add_argument("a", type=float, help="First number")
    parser.add_argument("op", choices=['+','-','*','/'], help="Operation")
    parser.add_argument("b", type=float, help="Second number")
    args = parser.parse_args()

    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide,
    }
    result = operations[args.op](args.a, args.b)
    print(result)

if __name__ == "__main__":
    main()
