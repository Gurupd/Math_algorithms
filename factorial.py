def factorial(n):
    res=1
    if n==0:
        return(1)
    else:
        for i in range(1,n+1):
            res=res*i
        return(res)
print(factorial(4))

#Using Recursion
def fact(n):
    
    if n==0:
        return(1)
    else:
        return(n*fact(n-1))
print(fact(5))

#Time complexity O(n)--Linear