print("Starting the first stuff\n")

six = 6
a = 2 +2 
b = 50 - 5*6
c = (50 - 5*six) / 4
d = 8 / 5

print(a)

print(b)

print(c)

print(d) 

print("\nStarting the second stuff\n")
e = 17 / 3  # classic division returns a float

f = 17 // 3  # floor division discards the fractional part

g = 17 % 3  # the % operator returns the remainder of the division

h = 5 * 3 + 2  # result * divisor + remainder

print(e)
print(f)
print(g)
print(h)

print("\nThird stuff now\n")

tax = 12.5 / 100
price = 100.50
print(price * tax)

print(price + price * tax)

print(round(price + price * tax, 2))

# String stuff 

print("The manager\'s words were: When I say \"immediately\" I mean sometime before August.")
print("The manager's words were: When I say 'immediately' I mean sometime before August.")

# Indices practice
name = "Elisabeth"
print(name[5:9])

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
x

print(x[0])

print(x[0][1])

# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while a < 20:
    print(a)
    a, b = b, a+b

x, y, z = 1, 2, 3
while x < 25:
    print(f"{x}, {y}, {z}")
    x, y, z = z, y + x, z + y

