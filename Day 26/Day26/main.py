# For Loop

numbers = [1,2,3]
new_list = []
for n in numbers:
    add_1 = n+1
    new_list.append(add_1)

print(new_list)

#Alternative List Comprehension
#new_list = [new_item for item in list]

new_list_comp = [n+1 for n in numbers]
print(new_list_comp)

#
#range_list = [new_item for item in list]
range_list = [num*2 for num in range(1,5)]
print(range_list)

#conditional list comprehensions
#range_list = [new_item for item in list]
names = ["Alex", "Beth", "Dave", "Christopher"]
short_names = []


