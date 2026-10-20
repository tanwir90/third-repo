# num = int(input("enter a number:"))

# if is_prime(num):
#     print(f"{num}is a prime number.")
# else:
#     print(f"{num}is not a prime number.")   

a = int(input("enter a number:"))
b = int(input("enter b number:"))
c = int(input("enter c number:"))

if a >= b and a >= c:
    print("largest =", a)
elif b >= a and b >= c:
    print("largest =", b)
else:
    print("largest =", c)




