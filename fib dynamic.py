# #1,1,2,3,5,8... 

def fib_dynamic(n):
    
    if n<2:
        return n
    empty_list=[0,1]
    for i in range(2,n):
        sum=empty_list[i-3]+empty_list[i-2]
        empty_list.append(sum)

    return empty_list
n=2
print(fib_dynamic(n))

# Recursive
def recursiveFib(n):
    if n<2:
        return n
    else:
        return(recursiveFib(n-1)+recursiveFib(n-2))
print("hi",recursiveFib(3))


# Time complexity is O(n)---iterative
#Time complexity is O(2^n)---recursive --not suitable

#n=32
# for i in range(1,n+1):
#     print(i)
#while n >=1 :
    
    #print(n)
    #n=n/2
    
#8
# 8= log2(n)
#           
#16=4         
#32=5