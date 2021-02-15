class student:
    def __init__(self, student_name):
        self.student_name = student_name
    def show_student(self):
        print("Name: ", self.student_name)

class registered_classes(student):
    def __init__(self, student_name, classes):
        self.classes = classes
        student.__init__(self, student_name)

class subject:
    def __init__(self):
        self.sub_name = ['C++', 'Java', 'Python', 'Writing Skills']
        self.sub_code = ['csc123', 'csc456', 'csc1122', 'mpu101']

        self.w = {}
        for i in range(len(self.sub_name)):
            self.w[self.sub_code[i]] = self.sub_name[i]
    def display(self):
        print("Course Code: ", self.sub_code)
        print("Course Name: ", self.sub_name)

c = subject()
c.display()

print('\n')
print('\n')

classes = []
student_name = input("Enter Name: ")
while True:
    sub_code = input("Enter code to register: ")

    if sub_code in  c.sub_code:
        print("***", sub_code, "is successfully registered!")
        classes.append(sub_code)
        print()
        print()
        next = input("Add more subjects?: (y/n) ")
        if next == 'y':
            continue
        else:
            break
    else:
        print("Wrong Code OR code is selected.")
        again = input("Enter code again (or 'x' to stop): ")
        print()
        print()
        next = input("Add more subjects?: (y/n) ")
        if next == 'y':
            continue
        else:
            break

s = student(student_name)
s.show_student()
print("Subjects registered: ")
for i in classes:
    print("**", i, c.w[i])

