integer_number = 58746
i = len(str(integer_number))
# print(i)
while i>0:
     print(integer_number//(10**(i-1)))
     integer_number = integer_number%(10**(i-1))
     i -= 1
