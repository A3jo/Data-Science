import math
a=int(input("enter the value for a:"))
b=int(input("enter the value for b:"))
c=int(input("enter the value for c:"))
d=b*b-4*a*c

if d<0:
    real=b/2*a
    img=math.sqrt(abs(d))/2*a
    root1=complex(real,img)
    root2=complex(real,-img)
else:
    root1 =(-b-math.sqrt(d))/(2*a)
    root2 =(-b+math.sqrt(d))/(2*a)

print("Root1:",root1,"and Root2:",root2)