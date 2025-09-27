#
'''

1  0  1  0  1  0  1
1  0  1  0  1  0  1
1  0  1  0  1  0  1
1  0  1  0  1  0  1
1  0  1  0  1  0  1
1  0  1  0  1  0  1
1  0  1  0  1  0  1

'''
def pattern(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(j%2,' ',end='')
        print()
pattern(7)