# Создайте функцию генератор чисел Фибоначчи 

def fibonacci_gen():
    x, y = 0, 1
    while True:
        yield x
        x, y = y, x + y


fib = fibonacci_gen()
for i in range(10):
    print(next(fib))  