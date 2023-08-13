"""
x = input("What's x? ")
y = input("What's y? ")

z = int(x) + int(y)

"""

x = int(input("What's x? "))
y = int(input("What's y? "))

print(x + y)

a = float(input("What's a? "))
b = float(input("What's b? "))

"""
c = round(a + b)

print(f"{z:,}") # 1,000
"""

c = round(a / b, 2)# rounds off to 2 decimal places
print(c)

print(f"{c:.2f}") # rounds off to 2 decimal places

"""Functions"""

def main():
    p = int(input("What's p? "))
    print("p squared is", square(p))

def square(n):
    return n * n

main()