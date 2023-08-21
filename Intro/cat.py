### Loops ###

# while loop decrementing
i = 3
while i != 0:
    print('meow')
    i = i-1

# while loop incrementing starting with 0
i = 0
while i < 3:
    print('meow')
    i += 1 #increment i


#for loop

for i in [0, 1, 2]:
    print("meow")
    
#more pythonic
print ("meow\n" * 3, end="")

# prompting user
while True: 
    n = int(input("What's n?"))
    if n > 0:
        break

for _ in range(n):
    print("meow")


# creating the meow function

def main():
    number = get_number()
    meow(number)

def get_number():
    while True: 
        n = int(input("What's n?"))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow")


main()