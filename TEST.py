def modulo(x,y) :
    if x<y :
        return x
    else :
        return modulo(x-y,y)
def reverseString(s, i = 0,k='') :
    if i == len(s):
       return k

    return reverseString(s, i+1,k+str(s[len(s)-i-1]))


print(reverseString("")) # ""
print(reverseString("bonjour")) # ruojnob
print(reverseString("ressasser")) # ressasser


print(modulo(6, 13)) # 6
print(modulo(37, 10)) # 7
print(modulo(8, 2)) # 0
print(modulo(50, 7)) # 1
