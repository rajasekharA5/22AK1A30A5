def is_prime(n):
    """Check if the number n is a prime number."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def next_palindrome(n):
    """Find the next palindrome number greater than n."""
    def is_palindrome(num):
        return str(num) == str(num)[::-1]

    num = n + 1
    while not is_palindrome(num):
        num += 1
    return num

def main():
    try:
        num = int(input("Enter a number: "))
        if is_prime(num):
            print("Next palindrome after", num, "is", next_palindrome(num))
        else:
            print("Not prime")
    except ValueError:
        print("Invalid input. Please enter an integer.")

if__name_ == "_main_":
    main()