
# converting from binary to base 10

import random
''' using a for loop to generate the four digit binary digits'''
rand_num=[]
for i in range(4):
    a = random.randint(0, 1)
    b= str(a)
    rand_num.append(b)
print(rand_num)
'''reversing the binary digits'''
rev_rand_num=rand_num[::-1]

# print(rev_rand_num)

Base_10=0
# for integers in rand_num:
for j in range(4):
    for integers in rev_rand_num[j]:
        p=int(integers)*(2**j)
        Base_10+=p
print(rand_num,"in binary form is equal to =",Base_10, ",in base 10")