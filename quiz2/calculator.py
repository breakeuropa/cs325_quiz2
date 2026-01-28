def add(a: int, b: int) -> int:
    sum = a + b
    print(f"{a} + {b} = ", end = " ")
    return sum

def subtract(a: int, b: int) -> int:
    difference = a + b
    print(f"{a} - {b} = ", end = " ")
    return difference

if __name__ == "__main__":
    print(add(1, 2))
    print(subtract(5, 3))
