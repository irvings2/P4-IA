import math
import random

def objetivo1(x):
    return x*4 + 3*x3 + 2*x*2 - 1

def objetivo2(x):
    return x**2 - 3*x - 8

def templado_simulado(funcion, x0, T0, alfa, L):
    x_actual = x0
    T = T0
    x_min = x_actual
    f_min = funcion(x_actual)
    
    for i in range(L):
        x_nuevo = x_actual + random.uniform(-1, 1)
        delta = funcion(x_nuevo) - funcion(x_actual)
        
        if delta < 0:
            x_actual = x_nuevo
            if funcion(x_actual) < f_min:
                x_min = x_actual
                f_min = funcion(x_actual)
        else:
            p = math.exp(-delta / T)
            if random.uniform(0, 1) < p:
                x_actual = x_nuevo
        
        T = alfa * T
    
    return x_min, f_min

# Función 1: f(x) = x^4 + 3*x^3 + 2*x^2 - 1
x0 = random.uniform(-10, 10)
T0 = 100
alfa = 0.99
L = 10000
x_min1, f_min1 = templado_simulado(objetivo1, x0, T0, alfa, L)
print(f"Función 1: f(x) = x^4 + 3*x^3 + 2*x^2 - 1")
print(f"Valor mínimo: x = {x_min1}, f(x) = {f_min1}")
print()

# Función 2: f(x) = x^2 - 3*x - 8
x0 = random.uniform(-10, 10)
T0 = 100
alfa = 0.99
L = 10000
x_min2, f_min2 = templado_simulado(objetivo2, x0, T0, alfa, L)
print(f"Función 2: f(x) = x^2 - 3*x - 8")
print(f"Valor mínimo: x = {x_min2}, f(x) = {f_min2}")