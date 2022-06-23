def power_of_two(n):
    if n<1:
        return False
    else:
        while(n>1):
            if (n%2!=0):
                return False
            n=n/2
    return True

print(power_of_two(1))
print(power_of_two(2))
print(power_of_two(8))
print(power_of_two(10))

# Time complexity O(logn) -- input size is reduced by half

# using bit-wise and operator

# we we multiply number with previous number we get 0
# 1-0001    2-0010
# 0-0000    1-0001
# ------    -----
# 0-0000    0-0000

def bit_wise(n):
    if (n<1):
        return False
    else:
        if (n & n(n-1))==0:
            return True
bit_wise(2)