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

def listSum(l) :
    if len(l) != 0:
        a=l[0]
        del l[0]
        return a+listSum(l)
    if len(l) == 0:
        return 0

def product(a,b) :
    if b==0 :
        return 0
    if b==1 :
        return a
    else :
        return a+product(a,b-1)


# print(reverseString("")) # ""
# # print(reverseString("bonjour")) # ruojnob
# # print(reverseString("ressasser")) # ressasser
# #
# #
# # print(modulo(6, 13)) # 6
# # print(modulo(37, 10)) # 7
# # print(modulo(8, 2)) # 0
# # print(modulo(50, 7)) # 1
# print(pow(42, 0)) # 1
# print(pow(1, 10)) # 1
# print(pow(2, 5)) # 32
# print(pow(7, 2)) # 49
# print(listSum([])) # 0
# print(listSum([42])) # 42
# print(listSum([3,1,5,2])) # 11
print(product(5,2)) # 10
print(product(9,3)) # 27
print(product(18,0))# 0

