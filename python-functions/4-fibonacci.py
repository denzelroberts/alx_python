def fibonacci_sequence(n):
    if n <= 0:
        return []  # Return an empty list for non-positive n
    elif n == 1:
        return [0]  # Special case for n = 1
    else:
        fib_numbers = [0, 1]  # Initialize the list with the first two Fibonacci numbers
        while len(fib_numbers) < n:
            next_fib = fib_numbers[-1] + fib_numbers[-2]
            fib_numbers.append(next_fib)
        return fib_numbers