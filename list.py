lst=[8,4,5,6,8,6,8,8]

count = 0

tg=8

for n in lst:
    if n == tg:
        count+=n
average=count/len(lst)
print(count)

print(average)



lst=[11,25,33,452,54,24,62,4,24]
lst2=[3,2,1]

# result=1

# for i in lst:
#    result= result * i


# print(result)

# a=min(lst)
# print(a)

# lst.sort()

# print(lst[0])

# print(lst[-2])

# for c in lst:
#    if c%2==0:
#       print(c,end=",")

even=0
odd=0

for h in lst2:
    if h%2==0:
      even+=1
    else:
        odd+=1
print(f"odd = {odd} even={even}")


a=[10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]

num=[]

n=[]

for c in a:
   if c not in num:
        num.append(c)
   else:
       n.append(c)

print(num)
print(set(n))

test_list = ["geeks", "for", "geeks", "is", "best"]

lst=[]

for n in test_list:
    m=n[::-1]
    lst.append(m)
print(lst)
    
