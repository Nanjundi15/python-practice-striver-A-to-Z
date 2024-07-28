def gcd(a,b):
    divisor=min(a,b)
    dividend=max(a,b)
    
    while dividend%divisor!=0:
        temp=dividend
        dividend=divisor
        divisor=temp%divisor
    return divisor
ans=gcd(12,10)
print(ans)