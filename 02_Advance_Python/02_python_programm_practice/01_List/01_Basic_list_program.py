
'''Q1. Given a list, write a Python program to swap first and last element of the list.
'''
# Solution:
'''Input = [12, 35, 9, 56, 24]
def swap_list(list):
    Input[0],Input[-1] = Input[-1],Input[0]
    return list

print(swap_list(Input))

def swap_list2(list):
    size = len(list)
    temp = list[0]
    list[0] = list[size-1]
    list[size-1] = list[0]
    return list
print(swap_list2(Input))

def swap_list3(list):
    a, *b, c = list
    list = c, *b, a
    return list
print(swap_list3(Input))

def swap_list5(list):
    first = list.pop(0)
    last = list.pop(-1)

    list.insert(0, last)
    list.append(first)
    return list
print(swap_list5(Input))

def swap_list6(list):
    if len(list) >= 2:
        # Swap the first and last elements using slicing
        lst = list[-1:] + list[1:-1] + list[:1]
    return lst
print(swap_list6(Input))'''

# **********************************************************************************************************

'''Q2. Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list.
'''
# Solution:
'''List = [23, 65, 19, 90]
def swap_any_two_elements(array: list, pos1: int, pos2: int):
    # breakpoint()
    if pos1 and pos2 <= len(array):
        array[pos1-1], array[pos2-1] = array[pos2-1], array[pos1-1]
        return array
    return IndexError("List Index Out of range")
print(swap_any_two_elements(List, 1, 0))'''

# **********************************************************************************************************

'''Q3. Sometimes, while working with data records we can have a problem in which we need to perform certain swap operation in which we need to change one element with other over entire string list. This has application in both day-day and data Science domain. Lets discuss certain ways in which this task can be performed. 
'''
# Solution:
'''test_list = ['Gfg', 'is', 'best', 'for', 'Geeks']
res = [sub.replace('G', '-').replace('e','G').replace('-', 'e') for sub in test_list]
print(res)

res = ', '.join(test_list)
res = res.replace('G', '-').replace('e','G').replace('-', 'e').split(', ')
print(res)

import re
res = [re.sub('-', 'e', re.sub('e','G', re.sub('G', '-', sub))).replace('e','G').replace('-', 'e') for sub in test_list]
print(res)'''

# **********************************************************************************************************

'''Q4. How To Find the Length of a List in Python
'''
# Solution:
'''li = [10, 20, 30]
n = len(li)
print(n)

count = 0
for i in li:
    count += 1
print(count)

from operator import length_hint
length = length_hint(li)
print(length)

list_len = sum(1 for i in li)
print(list_len)

for i, l in enumerate(li):
    pass
i += 1
print(i)

from collections import Counter
len1 = sum(Counter(li).values())
print(len1)

def count_elements_recursion(lst):
    if not lst:
        return 0
    # Recursive case: add 1 to the count of the remaining elements in the list
    return 1 + count_elements_recursion(lst[1:])
print(count_elements_recursion(li))'''

# **********************************************************************************************************

'''Q5. Given two numbers, write a Python code to find the Maximum of these two numbers.
'''
# Solution:
def max_of_two_num(a, b):
    return a if a >= b else b
print(max_of_two_num(4,8))

maximum = max(3, 6)
print(maximum)

a=2; b=5
maximum2 = lambda a,b: a if a >= b else b
print(maximum2(a, b))

maximum3 = [a if a >= b else b]
print(maximum3)

x = [a,b]
x.sort()
print(x[-1])

from functools import reduce
maximum4 = reduce(lambda x, y: x if x > y else y, [a, b])
print(maximum4)


# **********************************************************************************************************

'''Q6. 
'''
# Solution:

