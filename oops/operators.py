def sub_num(fn):
    def wrapper(n1,n2):
        if n1<n2:
            (n1,n2)=(n2,n1)
        return fn(n1,n2)
    return wrapper

@sub_num
def sum(n1,n2):
    return n1-n2
@sub_num
def div(n1,n2):
    return n1/n2
@sub_num
def add(n1,n2):
    return n1+n2

print(sum(8,10))
print(div(2,5))
print(add(4,6))