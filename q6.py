# 
'''
Enter the number or Rows: 9
* * * * * * * * *
* * * * * * * * *
* *           * *
* *           * *
* *           * *
* *           * *
* *           * *
* * * * * * * * *
* * * * * * * * *

'''
def pattern(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==1 or i==n or i==2 or i==n-1 or j==1 or j==n or j==n-1 or j==2:
                print('* ',end='')
            else:
                print('  ',end='')
        print()
pattern(int(input('Enter the number or Rows: ')))
