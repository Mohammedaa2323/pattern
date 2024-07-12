# # palinrome ===================================================

# # number = int(input("enter the numbers"))

# # digit=list(str(number)[::-1])
# # print(digit)
# # num = ''.join(digit)
# # print(num)

# # if int(number) == i(num):
# #     print("p")
# # else:
# #     print("not p")

# word = input("enter the word")

# string=list(word[::-1])
# print(string)
# result = "".join(string)

# if word == result:
#     print("it is p")

# else:
#     print("not p")


# # armstrog ======================================================

# # number = int(input("enter the numbers"))


# # length= len(str(number))
# # sum=0

# # temp =number

# # while temp > 0:  # 153 > 0

# #     digit = temp %10  # 153 >>> 15.3

# #     sum += digit ** int(length) # 3*3*3 =
# #                         #3
# #     temp //= 10

# # if number == sum:
# #         print(number,"is an Armstrong number")
# # else:
# #         print(number,"is not an Armstrong number")


# # fibnocci ==================================================================


# number=int(input("enter the  number"))

# prev = 0
# curent = 1
# # numbers=len(str(number))+1

# for i in range(number):
#     next = curent + prev #1,1
# #     print(next)
#     prev = curent        #1,2
# #     print(prev)
#     curent = next        #1
# #     print(curent)
#     print(prev,end=",")  #1,2


# # n = int(input("enter the number"))



# # print(f"prime"if n%2!=0  else "not prime")


# # factorial ===========================================================

# num = 7

# fact = 1

# for i in range(1,num+1):

#     fact *= i
#     if i%2!=0 :
#      print(i,": prime",end=", ")
#     elif i%2==0:
#       print(i,": not prime",end=", ")

# print(fact)


# # leap year ======================================================================

# # year = int(input("enter the year : "  ))

# # if year%4==0 or year%100!=0 and year%400==0 or year%100==0:
# #     print(year,": leap year")

# # else:
# #     print(year,"not leap year")


# # vowel count ====================================================================


# # name = ["mohammed"]

# # vowels = "a","e","i","o","u"

# # w=str(name)

# # print(w)

# # count =0

# # for i in w:
# #     if i in vowels:
# #         print(i,end=" ")
# #         count+=1
# # print(count)



# # word count =====================================================

# # word = "mohammed"

# # count={}

# # for i in word:
# #     if i in count:
# #         count[i] += 1
# #     else:
# #         count[i] = 1
# # print(count)



# # number =[1, 2, 3, 4, 2, 2, 5, 2]


# # count = {}

# # for i in number:
# #     if i in count:
# #         count[i]+=1
# #     else:
# #         count[i]=1
# # print(count)








# # # while i <= rows:
# # #     j = 1
# # #     while j <= i:
# # #         print("*", end=" ")
# # #         j += 1
# # #     print()
# # #     i += 1

row=5
for i in range(row):
    for j in range(0,i+1):
        print("*",end=" ")
    print()
rows = 5
for i in range(0,rows):
    for j in range(0,rows-1):
        print("",end=" ")
    rows=rows-1
    for j in range(0,i+1):
        print("+",end=" ")
    print()
# # n=5
# # # 4
# # for i in range(0, n):
# #     for j in range(0, n-1):
# #         print("",end=" ")
# #     n=n-1
# #     for j in range(0, i+1):
# #         print("*", end=" ")
# #     print()

n = 5
num=1
for i in range(n):
    # num = 1
    for j in range(i+1):
        print(num, end=" ")
        num = num + 1
    print()



num = 5 

for i in range(0,num):
    for j in range(0,num-1):

        print("",end=" ")

    num=num-1

    for j in range(0,i+1):
        print("*",end=" ")


    print()

k=5

for i in range(0,k):
    for j in range(0,i+1):

        print("",end=" ")

    k=k-1

    for j in range(0,k):
        print("*",end=" ")


    print()

# num = 153

# length=len(str(num))

# temp = num

# sum=0

# while temp > 0:
#     digit = temp%10

#     sum += digit ** int(length)

#     temp //=10

#     print(temp)

# if num == sum:

#     print("A")
# else:
#     print("NA")
# print(sum)


lst=[1,2,3,4,5,6,7,8,9]

# lst=["mohammed","new","now","add"]

# length=len(lst)

# temp = lst[0]  #mohammed

# lst[0]=lst[length-1] #mohammed=add

# lst[length-1]=temp #add=mohammed
# # print(n)
# print(lst)

post1=1

post2=3

first=lst.pop(post1)

second=lst.pop(post2)

lst.insert(post1,second)

lst.insert(post2,first)

print(lst)