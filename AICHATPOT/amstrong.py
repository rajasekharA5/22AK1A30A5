def is_armstrong(n):
    return n == sum(int(digit) ** len(str(n)) for digit in str(n))

num = int(input("Enter a number: "))
if is_armstrong(num):
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")