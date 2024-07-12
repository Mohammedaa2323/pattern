num=153

nums=len(str(num))

sum=0

temp = num

while temp > 0:

    digit = temp%10

    sum += digit ** int(nums)

    temp //= 10

if num == sum :
    print(f"{sum}==A")
else:
    print(f"{sum}=A")

print(sum)


numer=9

curent=1

prev=0

for i in range(numer):
    next = curent + prev

    prev = curent

    curent = next

    print(prev,end=",")


name = "mohammed"


obj = {}

for n in name:
    if n in obj:
        # print(n,end="")
        obj[n]+=1

    else:
        obj[n]=1
print(obj)

max_char = max(obj, key=obj.get)
max_count = obj[max_char]

print(f"{max_char}={max_count}")