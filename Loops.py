print("\nFor Loops:")
for number in range(3):
    print("attempt")
for number in range(3):
    print("attempt", number + 1, (number + 1) * ".")
for number in range(1, 5):
    print("attempt", number, number * ".")
for number in range(1, 10, 3):
    print("attempt", number, number * ".")


print("\n\nFor...else:")
successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("successful")
        break
else:
    print("Attempted 3 times & failed")


print("\n\nNested Loops:")
for x in range(5):
    for y in range(3):
        print(f"({x},{y})")


print("\n\nIterables:")
print(type(5))
print(type(range(5)))

for x in "Python":
    print(x)
print()  # New Line
for x in [1, 2, 3, 4]:
    print(x)


print("\n\nWhile Loops:")
number = 100
while number > 0:
    print(number, end=" ")
    number //= 2
print()  # New Line
cmd = ""
while cmd.lower() != "quit":
    cmd = input(">")
    print("ECHO", cmd)


print("\n\nInfinite Loops:")
while True:
    cmd = input(">")
    print("ECHO", cmd)
    if cmd.lower() == "quit":
        break
    # if we remove if statement or comment out it
