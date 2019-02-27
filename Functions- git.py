# 4.13.3: Greetings
# Caleb Taylor
# 2.5.19


name = input("What's your name: ")

def greeting():
    print("Hi there " + name + "!")
    print("Nice to meet you")

greeting()


# 4.13.4: Functions and Variables
# Caleb Taylor
# 2.11.18

x = 10

def print_something():
    x = 3
    print('\n', x)

print('\n',x)
print_something()


#4.13.6: Functions and Variables, Part 3
# Caleb Taylor
# 2.18.19


def print_number(x):
    print('\n', x)

print_number(13)
print_number(23)