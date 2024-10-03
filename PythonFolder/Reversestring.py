input="m,yna,mei,ssai"

s=input.split(",")
length=len(s)

print(s)

rev_str=""

for i in range(length):
    rev_str+= s[-i-1] + " "
print(rev_str)
print(input[::-1])
