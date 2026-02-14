import math
n = int(input("Enter a number: "))
if(0 <= n < 9):
    print(f"Square of {n} : {n**2}")
elif(10 <= n < 100):
    print(f"Squareroot of {n} : {math.sqrt(n):.2f}")
elif(100<= n < 100):
    print(f"Cuberoot of {n} : {n**(1/3):.2f}")
else:
    print("Please enetr a number between 0 to 999")