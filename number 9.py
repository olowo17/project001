# number 9
''' To sum the first nth series of a fibonacci sequence, sum= f(n+2)-1'''
n=int(input("These are the first 5 sequence of fibonacci series of the"))

#computing value of first fibonacci series
def Calculate_fibo_sum(n):
    if (n<=0):
        return 0
    fibo=[0]*(n+1)
    fibo[1]=1

    # initialize result
    sum_total=fibo[0]+fibo[1]

    #     add remaining terms
    for i in range(2,n+1):
        fibo[i]=fibo[i-1]+fibo[i-2]
        sum_total+=fibo[i]
    return sum_total
print("the sum of the  first nth term of the Fibonacci sequence is :",Calculate_fibo_sum(n))
