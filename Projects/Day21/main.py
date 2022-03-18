#Class Inheritance

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("Doing this under water")

    def swim(self):
        print("moving under water")

nemo = Fish()

print(nemo.breathe())