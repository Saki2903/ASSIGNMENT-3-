def factoral(n):
    if n==0 or n==1:
        return 1
    return n*factoral(n-1)

num=int(input("Enter a number: "))
print(f"The factorial of {num} is: {factoral(num)}")
