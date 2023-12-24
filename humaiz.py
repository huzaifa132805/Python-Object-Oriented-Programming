num = int(input("Enter the number: "))
reverse = num[::-1]
reverse = int(num)
first_digit = reverse % 10
last_digit = num % 10
total = first_digit+last_digit
print(total) 