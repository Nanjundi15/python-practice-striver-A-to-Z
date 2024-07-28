
# function method

'''def numdivisor(num):
    for i in range(1,num+1):
        if num%i==0:
            print(i)
numdivisor(12)'''

# normal method
n=int(input())
# for i in range(1,n+1):
#     if n%i==0:
#        print(i)
k=1
while k*k<=n:
    if n%k==0:
        print(k)
        if k!=(n//k):
            print(n//k)
    
    k+=1
    