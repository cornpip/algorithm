alpha = []
num = 0
def filter(n):
    global num, alpha
    if n.isalpha():
        alpha.append(n)
        return 
    else :
        num += int(n)
        return 

list(map(filter, input()))

alpha.sort()

yap = ""
for i in alpha:
    yap += i
print(yap + str(num))

# a = "AD45A"
# b = map(filter,a)
# print(b)