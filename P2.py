### Problema No. 2 Write a function named positive_sum() which receives as parameters a list of decimal numbers.
### The function computes the total sum of the positive numbers. For example, if the list is L=[9,-1,10,0,-2], the result of the funtion is 19


def positive_sum(L):
    positive_sum = 0
    for n in L:
        if n >= 0:
            positive_sum = n + positive_sum
    return positive_sum


L = [-1, 2, 14, 0, 0,1]
print "Sum L: ", positive_sum(L)

M= [1,1,2,8,1]
print "Sum M: ", positive_sum(M)

W= [-1,-2,-3]
print "Sum W: ", positive_sum(W)