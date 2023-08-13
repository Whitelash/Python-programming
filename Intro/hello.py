#ask user for name
name = input("What's your name? ") #variable, assignment operator, return value

#remove whitespace from str
name = name.strip()

#capitalize username
name = name.capitalize() # just the first letter of the first word
name = name.title()# first letter of each word

#chaining functions together
name = name.strip().title()

#shorter line of code
name = input("What's your name? ").strip().title()

#split username into first and last name
first, last = name.split()

#say hello to user
print("hello, " + name)
print("hi,",name) # parsing multiple arguments to print
print(f"ssup, {name}")

"""Functions"""

def main():
    username = input("What's your name? ")
    hello(username)

# defined function, designed to take value of a parameter->to, 
# to print with variable from user
def hello(to):
    print("hello,",to)

main()# calling the function