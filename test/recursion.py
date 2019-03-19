def sum_array(array):

    '''Return sum of all items in array'''
    total =0
    for i in array:
        total= total + i
    return total

def fibonacci(n):
    FibArray = [0,1]
    '''Return nth term in fibonacci sequence'''

    a = 0
    b = 1

    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2,n):
            c = a + b
            a = b
            b = c
        return b

def reverse(word):

    '''Return word in reverse'''
    rev = ""
    for i in word:
        rev = i + rev
    return rev
