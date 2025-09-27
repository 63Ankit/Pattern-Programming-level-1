#
'''

      *
      *
      *
* * * * * * *
      *
      *
      *


'''
def pattern(n):
    if n%2==0:
        return print('Enter only odd number of Rows:')
    mid=(n//2)+1
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==mid or j==mid:
                print('* ',end='')
            else:
                print('  ',end='')
        print()
pattern(int(input('Enter the number of Rows: ')))
            