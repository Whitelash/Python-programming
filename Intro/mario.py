def main():
    #vertical
    print_column(3)

def print_column(height):
    for _ in range(height):
        print("#")

#horizontal
    print_row(4)

def print_row(width):
    print("?" * width)

#square
    print_square(3)

def print_square(size):
    #for each row in square
    for i in range(size):
        #for each brick in row
        for j in range(size):
            #print brick
            print("#", end="") 
        #go to new line after row
        print()

#shorter version
def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#" * size)

main()