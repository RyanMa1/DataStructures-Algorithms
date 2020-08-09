def fact(integer_num):
    if(integer_num == 1 or integer_num == 0):
        return 1
    return integer_num * fact(integer_num - 1)
print(fact(5))