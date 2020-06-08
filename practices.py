#Important warning: The default value is evaluated only once. This makes a difference 
# when the default is a mutable object such as a list, dictionary, or instances of most classes. 
# For example, the following function accumulates the arguments passed to it on subsequent calls:

def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

#This will print

[1]
[1, 2]
[1, 2, 3]

#If you don’t want the default to be shared between subsequent calls, 
#you can write the function like this instead:

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

#ASK DAD--WHAT IS A TUPLE? what is a dictionary? How can a parameter receive a dictionary? also,
#I don't understand "in" very well

#When a final formal parameter of the form **name is present, it receives a dictionary 
# containing all keyword arguments except for those corresponding to a formal parameter. 
# This may be combined with a formal parameter of the form *name 
# which receives a tuple containing the positional arguments beyond the formal parameter list. 
# (*name must occur before **name.) For example, if we define a function like this:

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

#It could be called like this:

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

#Note that the order in which the keyword arguments are printed is guaranteed to match the order 
#in which they were provided in the function call.