def hello_world():
    print("Hello world!")

hello_world()

# def sum(num1, num2): # parameters
#     print(num1 + num2)

# sum(2,3) # arguments
# sum(1,7)
# sum(100,3)

def sum(num1=0, num2=0): # parameters; setting to zero returns zero if no arguments received
    if(type(num1) is not int or type(num2) is not int):
        return # early return
    return num1 + num2

# total = sum("a", 3) # unexpected type argument returns None
total = sum()
print(total)

def multiple_items(*args):
    print(args)
    print(type(args))

multiple_items("Dave", "John", "Sara")

def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))

mult_named_items(first = "Dave", last = "Gray")
