first_number=int(input("Enter 1st Number:"))
second_number=int(input("Enter 2nd Number:"))
third_number=int(input("Enter 3rd Number:"))

if first_number > second_number > third_number:
    print(first_number)
elif second_number > third_number:
    print(second_number)
else:
    print(third_number)
