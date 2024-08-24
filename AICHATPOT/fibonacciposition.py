def fibonacci_position(n):
    """
    Returns the position of a Fibonacci number.

    Args:
        n (int): The Fibonacci number.

    Returns:
        int: The position of the Fibonacci number.
    """
    a, b = 0, 1
    position = 1
    while b < n:
        a, b = b, a + b
        position += 1
    if b == n:
        return position
    else:
        return -1  # Return -1 if the number is not a Fibonacci number

num = int(input("Enter a number: "))
position = fibonacci_position(num)
if position != -1:
    print(f"The position of {num} in the Fibonacci sequence is {position}.")
else:
    print(f"{num} is not a Fibonacci number.")