class StudentData:
    def __init__(self):  # Default Constructor.
        print("I am a student")
        self.m1 = 0
        self.m2 = 0
        self.m3 = 0

    def enterMarks(self):
        self.m1 = int(input('Enter marks of sub. 1: '))
        self.m2 = int(input('Enter marks of sub. 2: '))
        self.m3 = int(input('Enter marks of sub. 3: '))
    def calc_percent(self):
        return ('Pass' if (self.m1 + self.m2 + self.m3) > 90 else 'Fail')

class Engineer(StudentData): # Inherit the StudentData Class
    def __init__(self):
        print("I am an engineer!")
        super().__init__()

    pass  # Python does not allow empty class so pass used

class Doctor(StudentData):
    # def __init__(self):
    #     print('I am a doctor')
    def talk(self):
        print('I am a doctor!')

obj1 = Doctor()
obj2 = Engineer()
obj1.enterMarks()
print(obj1.calc_percent())
obj1.talk()

