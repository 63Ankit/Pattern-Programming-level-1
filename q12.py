# Write a program to print the matrix with the certain symbol.
'''

( 1 , 1 )  ( 1 , 2 )  ( 1 , 3 )  ( 1 , 4 )  ( 1 , 5 )
( 2 , 1 )  ( 2 , 2 )  ( 2 , 3 )  ( 2 , 4 )  ( 2 , 5 )
( 3 , 1 )  ( 3 , 2 )  ( 3 , 3 )  ( 3 , 4 )  ( 3 , 5 )
( 4 , 1 )  ( 4 , 2 )  ( 4 , 3 )  ( 4 , 4 )  ( 4 , 5 )
( 5 , 1 )  ( 5 , 2 )  ( 5 , 3 )  ( 5 , 4 )  ( 5 , 5 )


'''
def pattern(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            print('(',i,',',j,')  ',end='')
        print()
pattern(5)
