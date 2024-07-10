# def reverse(num):
#     ans=0
#     while num>0:
#         rem=num%10
#         ans=ans*10+rem
#         num=num//10
#     return ans
# num=int(input())
# ans=reverse(num)
# print(ans)

num=int(input())
rem=0
ans=0
while num>0:
    rem=num%10
    ans=ans*10+rem
    num=num//10
print(ans)