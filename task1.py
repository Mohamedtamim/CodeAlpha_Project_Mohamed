def fibonacci_generator(n):
    fib_sequence = [0, 1]  
    for i in range(n):
        next_fib = fib_sequence[-1] + fib_sequence[-2]  
        fib_sequence.append(next_fib)
    return fib_sequence[:n]  

n = int(input("Input n: "))
fib_series = fibonacci_generator(n)
print("The fibonacci sequence of", n, "is:", fib_series)