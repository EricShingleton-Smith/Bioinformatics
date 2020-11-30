def fibonacci(n):
    if n <= 1:
        return n
   # if n == 2:
    #    return n
    else:
        return (fibonacci(n - 1) + fibonacci(n - 2))

def fibonacci_loop_pythonic(months, offsprings):
    parent, child = 1, 1
    for itr in range(months - 1):
        child, parent = parent, parent + (child * offsprings)
    return child