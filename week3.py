def largePower(base, exponent):
    result=base**exponent
    if result>5000:
        return True
    else:
        return False
    
#Test the function
print(largePower(10,3))
print(largePower(10,10))

def divisibleByTen(num):
    if num%10==0:
        return True
    else:
        return False

#test
print(divisibleByTen(100))
print(divisibleByTen(102))