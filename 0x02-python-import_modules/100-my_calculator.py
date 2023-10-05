#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])
    c = 0

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if op not in ["+", "-", "*", "/"]:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    if op == "+":
        c = add(a, b)
    elif op == "-":
        c = sub(a, b)
    elif op == "*":
        c = mul(a, b)
    elif op == "/":
        c = div(a, b)

    print(f"{a} {op} {b} = {c}")
