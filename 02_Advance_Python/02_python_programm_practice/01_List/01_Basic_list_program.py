
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
'''def max_of_two_num(a, b):
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
print(maximum4)'''


# **********************************************************************************************************

'''Q6. Python | Ways to check if element exists in list
'''
# Solution:
'''list = test_list = [1, 6, 3, 0, 5, 3, 4]
def elem_exists_or_not(array: list, elem):
    if elem in array:
        return True
    else:
        return False
print(elem_exists_or_not(list, 3))

def elem_exists_or_not2(array: list, elem):
    # if elem in array:
    #     return True
    # else:
    #     return False
    s = 0
    for e in array:
        if e == elem:
            s += 1
    if s > 0:
        return True
    else:
        return False
print(elem_exists_or_not2(list, 3))

if 4 in list:
    print(True)

result = any(el==3 for el in list)
print(result)

test = list.count(4)
if test > 0:
    print(True)
else:
    print(False)

from collections import Counter
f = Counter(test_list)
print(f[3]>0)

try:
    list.index(4)
    print(True)
except ValueError:
    print(False)

def check_element_exists_set(lst, target):
  return target in set(lst)
check_element_exists_set(list, 4)'''

# **********************************************************************************************************

'''Q7. Different ways to clear a list in Python
'''
# Solution:
'''GEEK = [6, 0, 4, 1, 5, 4, 6, 7, 8, 9, 2, 0]
GEEK.clear()
print(GEEK)

ls = [6, 0, 4, 1, 5, 4, 6, 7, 8, 9, 2, 0]
print(ls)
ls = []
print(ls)

ff = [6, 0, 4, 1, 5, 4, 6, 7, 8, 9, 2, 0]
del ff[:]
print(ff)

tt = [6, 0, 4, 1, 5, 4, 6, 7, 8, 9, 2, 0]
while len(tt) != 0:
    tt.pop()
print(tt)

lst = GEEK[:0]
print(lst)'''


# **********************************************************************************************************

'''Q8. Reversing a List in Python
'''
# Solution:
'''list = [4, 5, 6, 7, 8, 9, 3, 1, 2]
l1 = [4, 5, 6, 7, 8, 9]
l1.reverse()
# print(l1)

s = []
for i in list:
    s.insert(0, i)
# print(s)

r = [4, 5, 6, 7, 8, 9]
s = r[::-1]
# print(s)
    
def reverse_list(lst):
    left = 0
    right = len(lst)-1

    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        print(left)
        right -= 1
        print(right)
    return lst
# print(reverse_list(list))

new_list = [list[len(list)-i] for i in range(1, len(list)+1)]
# print(new_list)

new = [list[i] for i in range(len(list)-1, -1, -1)]
# print(new)

import numpy as np
arr = np.array(list)
reversed = arr[::-1].tolist()
print(reversed)'''
# **********************************************************************************************************

'''Q8. Python | Cloning or Copying a list
'''
# Solution:
'''list = [4, 8, 2, 10, 15, 18]
def cloning(lst):
    li = list[:]
    return li
# print(cloning(list))

def cloning1(lst):
    l1 = []
    l1.extend(lst)
    return l1
# print(cloning1(list))

def cloning(lst):
    li = lst
    return li
# print(cloning(list))

import copy
l2 = copy.copy(list)
# print(l2)

def cloning3(lst):
    li = [i for i in list]
    return li
# print(cloning3(list))

def cloning4(lst):
    li = []
    for item in list: li.append(item)
    return li
# print(cloning4(list))

lst1 = copy.deepcopy(list)
# print(lst1)

lst2 = map(int, list)
# print([*lst2])

from collections import deque
lst3 = [(deque(list))]
# print(lst3)'''

# **********************************************************************************************************

'''Q9. Python | Count occurrences of an element in a list.
'''
# Solution:
'''lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
from collections import Counter
s = Counter(lst)
# print(s)

def count(lst, x):
    count = 0
    for i in lst:
        if i == x:
            count += 1
    return count
# print(count(lst, 10))

def count1(lst, x):
    return lst.count(x)
# print(count1(lst, 10))

import operator as op
s = op.countOf(lst, 10)
# print(s)

occurrence = {i: lst.count(i) for i in lst}
# occurrence = {i: count(lst, i) for i in lst}
# print(occurrence)

import pandas as pd
coun = pd.Series(lst).value_counts()
# print(coun)

ele = 8
x = [i for i in lst if i == ele]
print(len(x))'''

# **********************************************************************************************************

'''Q10. Find sum and average of List in Python.
'''
# Solution:
'''L = [4, 5, 1, 2, 9, 7, 10, 8]
c = 0
for i in L:
    c += i
ave = c/len(L)
# print(c, ave)

sum1 = sum(L)
avg1 = sum1/len(L)
# print(sum1, avg1)

import statistics
sum2 = sum(L)
avg2 = statistics.mean(L)
# print(sum2, avg2)

import numpy as np
sum3 = np.sum(L)
avg3 = np.average(L)
# print(sum3, avg3)

def sum_avg(list):
    sum = 0
    count = 0
    for i in list:
        sum += i
        count += 1
    avg = sum/count
    return sum, avg
# print(sum_avg(L))

from functools import reduce
count4 = reduce(lambda x,y: x+y, L)
avg4 = count4/len(L)
# print(count4, avg4)'''

# **********************************************************************************************************

'''Q11. Python | Sum of number digits in List
'''
# Solution:
'''test_list = [12, 67, 98, 34]
res = []
for i in test_list:
    sum = 0
    for d in str(i):
        sum += int(d)
    res. append(sum)
# print(res)

# res1 = list(map(lambda ele: sum(int(sub) for sub in str(ele)), test_list))
# print(str(res1))

from functools import reduce
res4 = [reduce(lambda x, y: int(x) + int(y), list(str(i))) for i in test_list]
# print(res4)

def digit_sum(num):
    digit_sum = 0
    while num > 0:
        digit_sum += num % 10
        num //=10
    return digit_sum
def sum_digit(lst):
    return list(map(digit_sum, lst))
# print(sum_digit(test_list))

res5 = [sum(int(s) for s in str(num1)) for num1 in test_list]
# print(res5)'''

# **********************************************************************************************************

'''Q12. Python | Multiply all numbers in the list
'''
# Solution:
list1 = [1, 2, 3]
s = 1
for i in list1:
    s *= i
# print(s)

import numpy as np
res1 = np.prod(list1)
# print(res1)

from functools import reduce
r = reduce(lambda x, y: x*y, list1)
# print(r)

import math
res4 = math.prod(list1)
# print(res4)

def product_list(nums):
    if not nums:
        return 1
    return nums[0] * product_list(nums[1:])
# print(product_list(list1))

from functools import reduce
from operator import mul
res6 = reduce(mul, list1)
    
# **********************************************************************************************************

'''Q13. 
'''
# Solution:

# **********************************************************************************************************

'''Q14. 
'''
# Solution:

# **********************************************************************************************************

'''Q15. 
'''
# Solution:
'''Q6. 
'''
# Solution:
'''Q6. 
'''
# Solution:
'''Q6. 
'''
# Solution:
'''Q6. 
'''
# Solution:
'''Q6. 
'''
# Solution:
'''Q6. 
'''
# Solution:
'''Q6. 
'''
# Solution:
'''Q6. 
'''
# Solution:
'''Q6. 
'''
# Solution:
'''Q6. 
'''
# Solution:
'''Q6. 
'''
# Solution:
'''Q6. 
'''
# Solution:
'''Q6. 
'''
# Solution:
'''Q6. 
'''
# Solution:
'''Q6. 
'''
# Solution:
'''Q6. 
'''
# Solution:
