for i in range(1,10):
    print(i, end=',')

print("---------------------")

'''
*
**
***
****
*****
'''
for i in range(1,6):
    print('*' * i)

'''
    *
   ***
  *****
 *******
*********
'''
for i in range(10):
    print(' ' * (10 - i) + '*' * (2*i + 1))











