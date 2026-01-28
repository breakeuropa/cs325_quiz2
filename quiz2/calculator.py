def add(a: int, b: int) -> int:
    sum = a + b
    print(f"{a} + {b} = ", end = " ")
    return sum

def subtract(a: int, b: int) -> int:
    difference = a - b
    print(f"{a} - {b} = ", end = " ")
    return difference

def mul(a: int, b: int) -> int:
    product = a * b
    print(f"{a} * {b} = ", end = " ")
    return product

def div(a: int, b: int) -> int:
    quotient = a / b
    print(f"{a} / {b} = ", end = " ")
    return quotient

if __name__ == "__main__":
    print(add(1, 2))
    print(subtract(5, 3))
    print(mul(2, 2))
    print(div(15, 3))
