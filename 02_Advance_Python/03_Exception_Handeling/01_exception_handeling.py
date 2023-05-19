a = 10
b = 0
try:
    d = a/b
    print(d)
    print('Inside Try')
except ZeroDivisionError as e:
    print(e)
    print('Division by zero is not Allowed')
else:
    print('Inside else')
finally:
    print('Inside Finally')

print('Rest of the Code')
