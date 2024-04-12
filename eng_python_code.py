variable = 5
condition = True
if condition:
    print("Variable:", variable)
    print("Condition:", condition)
else:
    print("False: incorrect")

numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
    print("Sum of numbers:", total)

count = 10
for num in range(count):
    print(num)
    count += 1


class MyClass:
    message = "This is a class"

    def print_message(self):
        print(self.message)


path = "/class/example/path/file.txt"
try:
    with open(path) as file:
        pass
except:
    print("File not found")
