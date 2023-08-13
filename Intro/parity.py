
"""
# %
if x % 2 == 0:
    print("This is an even number")
else:
    print("This is an odd number")
"""

def main():
    x = int(input("What's x? "))

    if is_even(x):
        print("This is an even number")
    else:
        print("This is an odd number")

def is_even(n):
    """
    if n % 2 == 0:
        return True
    else:
        return False
    
    """
    
    """ 
    return True if n % 2 == 0 else False
     
    """

    return n % 2 == 0

main()