#file not found error
try:
    with open("texta.txt") as file:
       file.read()
    a_dictionery = {"key": "value"}
    print(a_dictionery["key"])
except FileNotFoundError:
    with open("texta.txt","a") as file:
        file.read()
except KeyError as error_message:
    print(f"This key {error_message} does not exist.")
else:
    file = open("texta.txt")
    content = file.read()
    print(content)
finally:
    raise TypeError("This is an error.")
