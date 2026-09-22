import pickle


class CustomObject():
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}\nAge: {self.age}\nIs Student: {self.is_student}")

    def serialize(self, filename):
        with open(filename, "wr") as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        with open(filename, "rb") as f:
            pickle.load(f)
