def fibonacci_sequence(limit):
    if limit <= 0:
        raise ValueError("Limit must be a positive integer.")
    
    sequence = [0, 1]
    while sequence[-1] + sequence[-2] <= limit:
        sequence.append(sequence[-1] + sequence[-2])
    
    return sequence

# Example usage
try:
    limit = 100
    result = fibonacci_sequence(limit)
    print("Fibonacci Sequence up to", limit, ":", result)
except ValueError as e:
    print(e)
