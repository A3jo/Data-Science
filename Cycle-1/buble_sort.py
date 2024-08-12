a=[]
n=int(input("Enter the size of the array:"))
print("enter the Element:")
for i in range(n):
    ele=int(input())
    a.append(ele)
print("array:",a)
for i in range(n):
    for j in range(0,n-i-1):
        if a[j]>a[j+1]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp

print("Sorted Array:",a)
