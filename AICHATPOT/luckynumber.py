def calculate_lucky_number(dob):
    dob_sum = sum(int(digit) for digit in dob.replace("-", "").replace("/", ""))
    while dob_sum > 9:
        dob_sum = sum(int(digit) for digit in str(dob_sum))
    return dob_sum

dob = input("Enter your date of birth (DD/MM/YYYY or DD-MM-YYYY): ")
lucky_number = calculate_lucky_number(dob)
print("Your lucky number is:", lucky_number)