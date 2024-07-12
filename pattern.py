
x= int(input("enter number of rows : "))
y= int(input("enter number of columns : "))



print(" ",end="")
for i in range(1,(x*2)+2):
    for j in range (1,y+1):
        if i ==1 and j%2!=0:
            print("___",end="")
        elif i ==1 and j%2==0:
            print("     ",end="")
        elif i %2!=0 and j%2!=0:
            print("\\___/",end="")
        elif i%2!=0 and j%2==0:
            print("   ",end="")    
        elif i%2==0 and j%2!=0:
            print("/   \\",  end="")
        elif i%2==0 and j%2==0:
            print("___",end="")
    print()