__author__ = 'stas'


def task_7_1_8(a,n):
    '''
        two param
    '''
    if n==1:
        return a[0]
    return a[n-1] + task_7_1_8(a, n-1)

def task_7_1_8_1(a):
    '''
        one param
    '''
    if len(a)==1:
        return a[0]
    return a[-1] + task_7_1_8_1( a[:-1] )

def task_7_1_8_reduce(a):
    return reduce(lambda x,y:x+y,a,0)


array = range(0,10,1)
summ = task_7_1_8(array,len(array))
summ2 = task_7_1_8_1(array)
summ3 = task_7_1_8_reduce(array)

print('Expect: %s'%sum(array))
print(summ)
print(summ2)
print(summ3)
