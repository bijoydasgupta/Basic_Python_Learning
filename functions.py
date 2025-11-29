print("\nFunctions:")


def greet():
    print("Hi there !")
    print("Welcome abord")


greet()

print("\n\narguments:")


def greet2(first_name, last_name):
    print(f"Hi {first_name} {last_name}!")
    print("Welcome abord")


greet2("Bijoy", "Das Gupta")
greet2("Joy", "Das Gupta")

print("\n\nReturn a value:")


def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Bijoy")
# print(message)
file = open("content.txt", "w")
file.write(message)


print("\n\nKeyword arguments:")


def increment(number, by):
    return number+by


print(increment(2, by=1))
