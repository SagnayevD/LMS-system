class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        self._age = value
        
    def __repr__(self):
        return f"{self.__class__.__name__}('{self._name}', {self._age})"
    
    def __str__(self):
        return f"{self._name}, {self._age} лет"
    
    def __eq__(self, other):
        if isinstance(other, Person):
            return self._name == other._name and self._age == other._age
        return False

    def __hash__(self):
        return hash((self._name, self._age))


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self._subject = subject
    
    @property
    def subject(self):
        return self._subject
    
    @subject.setter
    def subject(self, value):
        self._subject = value
    
    def teach(self):
        return f"{self._name} преподает {self._subject}"
    
    def __repr__(self):
        return f"{self.__class__.__name__}('{self._name}', {self._age}, '{self._subject}')"
    
    def __str__(self):
        return f"Преподаватель: {self._name}, возраст: {self._age}, предмет: {self._subject}"


class Lesson:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
    
    def __repr__(self):
        return f"{self.__class__.__name__}('{self._name}')"
    
    def __str__(self):
        return f"Дисциплина: {self._name}"

    def __eq__(self, other):
        if isinstance(other, Lesson):
            return self._name == other._name
        return False

    def __hash__(self):
        return hash(self._name)


class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self._grades = {}
    
    def add_grade(self, lesson, grade):
        self._grades[lesson] = grade
    
    @property
    def average_grade(self):
        if self._grades:
            return sum(self._grades.values()) / len(self._grades)
        return 0
    
    def __repr__(self):
        return f"{self.__class__.__name__}('{self._name}', {self._age})"
    
    def __str__(self):
        return f"Ученик: {self._name}, возраст: {self._age}, средний балл: {self.average_grade:.2f}"

    def __eq__(self, other):
        if isinstance(other, Student):
            return self._name == other._name and self._age == other._age
        return False

    def __hash__(self):
        return hash((self._name, self._age))


class LMS:
    def __init__(self):
        self._teachers = set()
        self._lessons = set()
        self._students = set()
    
    def add_teacher(self, teacher):
        self._teachers.add(teacher)
    
    def add_lesson(self, lesson):
        self._lessons.add(lesson)
    
    def add_student(self, student):
        self._students.add(student)
    
    def __str__(self):
        return f"LMS: Преподавателей - {len(self._teachers)}, Уроков - {len(self._lessons)}, Учеников - {len(self._students)}"


lms = LMS()

teacher1 = Teacher("Botakoz Suleymenova", 62, "Math")
teacher2 = Teacher("Dauren Sagnayev", 26, "Science")

student1 = Student("Tairkhan Kopeyev", 14)
student2 = Student("Bejnar Matvey", 13)

lesson1 = Lesson("Алгебра")
lesson2 = Lesson("Физика")

lms.add_teacher(teacher1)
lms.add_teacher(teacher2)

lms.add_student(student1)
lms.add_student(student2)

lms.add_lesson(lesson1)
lms.add_lesson(lesson2)

student1.add_grade(lesson1, 95)
student1.add_grade(lesson2, 87)

student2.add_grade(lesson1, 78)
student2.add_grade(lesson2, 92)

def start_menu():
    print("Приветствую, выберите что вы хотите сделать:")
    print("1. Увидеть список преподавателей")
    print("2. Увидеть список учеников и средний балл")
    print("3. Увидеть список дисциплин")
    print("4. Выйти")
    n = int(input('Выберите действие: '))

    if n == 1:
        for teacher in lms._teachers:
            print(teacher)
        print("0. Вернуться в главное меню")
        n = int(input('Выберите действие: '))
        if n == 0:
            start_menu()
        else:
            print('Ошибка! Возвращаем в главное меню')
            start_menu()

    elif n == 2:
        for student in lms._students:
            print(student)
        print("0. Вернуться в главное меню")
        n = int(input('Выберите действие: '))
        if n == 0:
            start_menu()
        else:
            print('Ошибка! Возвращаем в главное меню')
            start_menu()

    elif n == 3:
        for lesson in lms._lessons:
            print(lesson)
        print("0. Вернуться в главное меню")
        n = int(input('Выберите действие: '))
        if n == 0:
            start_menu()
        else:
            print('Ошибка! Возвращаем в главное меню')
            start_menu()
    elif n == 4:
        return
    else:
        print('Ошибка! Возвращаем в главное меню')
        start_menu()

print(lms)
start_menu()
