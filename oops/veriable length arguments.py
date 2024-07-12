# def add_num(*args):
#     return sum(args)

# print(add_num(10,20))
# print(add_num(20,30,10))

# def mul_num(*args):
#     result=1
#     for n in args:
#         result=result*n

#     print(result)

# mul_num(20,20)

# reamainder

# def lst_num(*args):
#     sum=0
#     for n in args:
#         num=n%10
#         sum+=num
    # return sum
    # digit=[n%10 for n in args]
    # return sum(digit)
# print(lst_num(123,345,567,678))

# # max digit

# def max_num(*args):
#     digit=[n%10 for n in args]
#     return max(digit)
# print(max_num(12,14,17,18,19,20))




# for calling purpose key words

# def add_employee(**kwargs):

#     print(kwargs.get("id"))
#     print(kwargs.get("name"))
# add_employee(id=10,name="mohammed",place="ekm",salary=10000000)


# reverse true \ or false


# def las_digit_num(*args,**kwargs):
#     digit=[n%10 for n in args]
#     value=kwargs.get("reverse")

#     if value==True:
#         digit.sort(reverse=True)
#     else:
#         digit.sort(reverse=False)
#     return digit
# print(las_digit_num(12,13,14,17,15,reverse=False))   