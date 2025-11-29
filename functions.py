def greet():
    print("\nHi there !")
    print("Welcome abord")


greet()


def greet2(first_name, last_name):
    print(f"\nHi {first_name} {last_name}!")
    print("Welcome abord")


greet2("Bijoy", "Das Gupta")
greet2("Joy", "Das Gupta")


def get_greeting(name):
    return f"\n\nHi {name}"


message = get_greeting("Bijoy")
# print(message)
file = open("content.txt", "w")
file.write(message)
