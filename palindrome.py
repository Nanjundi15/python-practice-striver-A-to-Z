def reverse(num):
    ans=0
    while num>0:
        rem=num%10
        ans=ans*10+rem
        num=num//10
    return ans

def palindrome(num):
    return num==reverse(num)
num=int(input())
ans=palindrome(num)
print(ans)