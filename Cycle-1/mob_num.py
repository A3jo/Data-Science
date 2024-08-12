a=input("Enter a 10 digit number:")
b=sorted(set('0123456789')-set(a))
print(b)