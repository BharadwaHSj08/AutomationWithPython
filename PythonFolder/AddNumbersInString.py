input_String=input("Enter the Numbers:")
print(input_String)
given_String=input_String.split(",")

length_of_str=len(given_String)
new_lst=[]

for i in range(length_of_str-1):
    new_list_element=given_String[i] + given_String[i+1]
    new_lst.append(new_list_element)

print(new_lst)

str_int_converted_lst=[int(x) for x in new_lst]
print(max(str_int_converted_lst))





