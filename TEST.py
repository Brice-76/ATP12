def modulo(x,y) :
    if x<y :
        return x
    else :
        return modulo(x-y,y)
def reverseString(s, i = 0,k='') :
    if i == len(s):
       return k

    return reverseString(s, i+1,k+str(s[len(s)-i-1]))

def pow(x,n,r=1) :
    if n ==0 :
        return 1
    if n==1 :
        return x
    else :
        return x*pow(x,n-1)


# print(reverseString("")) # ""
# # print(reverseString("bonjour")) # ruojnob
# # print(reverseString("ressasser")) # ressasser
# #
# #
# # print(modulo(6, 13)) # 6
# # print(modulo(37, 10)) # 7
# # print(modulo(8, 2)) # 0
# # print(modulo(50, 7)) # 1
print(pow(42, 0)) # 1
print(pow(1, 10)) # 1
print(pow(2, 5)) # 32
print(pow(7, 2)) # 49

