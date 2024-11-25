import math

# Память для хранения числа
memory = 0

def square_root(a):
    if a < 0:
        return "Error: Negative input"
    return math.sqrt(a)

def floor_value(a):
    return math.floor(a)

def ceil_value(a):
    return math.ceil(a)

def memory_add(value):
    global memory
    memory += value

def memory_clear():
    global memory
    memory = 0

