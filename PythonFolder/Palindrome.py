input="amaama"

length= len(input)
print(length)

half=length//2
print(half)

frst_str=input[:half]
print(frst_str)

scnd_str=input[half:]
print(scnd_str)

if frst_str == scnd_str:
    print("The String is a Palindrome and also symmetrical")
else:
    print("The String is not a plaindrome as well as symetrical")

