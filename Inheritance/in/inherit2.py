class Animal:
    def __init__(self,Name):
        self.Name = Name
        
    def Speak(self):
        print(f"{self.Name} Makes sound")
        
class Tiger(Animal):
    def Speak(self):
        print(f"{self.Name} Sounds ROAR!")
