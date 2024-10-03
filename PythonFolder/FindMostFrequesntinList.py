#Program to find most frequent element in List

l1=[2,1,1,2,2,3]

#result = dict((i, l1.count(i)) for i in l1)
for i in l1:
    counter=l1.count(i)
    if counter >2:
        x=("The Most frequent Number is:", i)
print(x)


