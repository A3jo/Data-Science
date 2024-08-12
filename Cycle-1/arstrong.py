for i in range(1,1000):
    sum = 0
    num =i
    num_str=str(i)
    num_len=len(num_str)
    while i>0:
        b=i%10
        sum=sum+b**num_len
        i=i//10
    if num==sum:
         print(num)
