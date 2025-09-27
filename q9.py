#
'''

* * * * * * * * * * *
* *       *       * *
*   *     *     *   *
*     *   *   *     *
*       * * *       *
* * * * * * * * * * *
*       * * *       *
*     *   *   *     *
*   *     *     *   *
* *       *       * *
* * * * * * * * * * *

'''
def pattern(n):
    if n%2==0:
        return print('Please Enter the odd number of rows: ')
    mid=(n//2)+1
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==1 or i==n or j==1 or j==n or i==mid or j==mid or i==j or i+j==n+1:
                print('* ',end='')
            else:
                print('  ',end='')
        print()
pattern(int(input('Enter the number of Rows: ')))
