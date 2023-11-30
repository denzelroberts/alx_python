def is_prime(number):
    if number < 2:
        return False  # Numbers less than 2 are not prime
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False  # If it has a divisor other than 1 and itself, it's not prime
    return True  # Otherwise, it's prime