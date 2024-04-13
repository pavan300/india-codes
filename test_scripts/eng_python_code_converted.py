variable = 5
condition = నిజం
ఐతే condition:
    ముద్రించు("Variable:", variable)
    ముద్రించు("Condition:", condition)
లేదా:
    ముద్రించు("False: incorrect")

numbers = [1, 2, 3, 4, 5]
total = 0
ప్రతి num లో numbers:
    total += num
    ముద్రించు("Sum of numbers:", total)

count = 10
ప్రతి num లో శ్రేణి(count):
    ముద్రించు(num)
    count += 1


వర్గం MyClలాs:
    message = "This is a class"

    నిర్వచనం ముద్రించు_message(self):
        ముద్రించు(self.message)


path = "/class/example/path/file.txt"
ప్రయత్నించు:
    తో open(path) లా file:
        కానివ్వు
తప్ప:
    ముద్రించు("File not found")
