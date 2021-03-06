# coding=UTF-8
class SchoolMember:
    """代表任何学校里的成员"""
    def __init__(self,name,age):
        self.name = name;
        self.age = age
        print('Initialized SchoolMember :{}'.format(self.name))

    def tell(self):
        """告诉我有关细节"""
        print('Name :"{}" Age : "{}"'.format(self.name,self.age),end=" ")


class Teacher(SchoolMember):
    """代表老师"""
    def __init__(self,name,age,salary):
        SchoolMember.__init__(self,name,age)
        self.salary = salary
        print('Initialized Teacher :{}'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('salary :"{:d}"'.format(self.salary))


class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self,name,age)
        self.marks = marks
        print('Initialized Student: {}'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}'.format(self.marks))


t = Teacher('Mr.shricidya', 30, 3000)

s = Student('Swaroop',25,75)

print()

members = [t, s]

for member in members:
    member.tell()
