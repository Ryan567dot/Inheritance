class departmentA:
    def __init__(self,Name,ID,Bonus=3000):
        self.Name = Name
        self.ID = ID
        self.Bonus = Bonus
        
class departmentB(departmentA):
    def __init__(self,Name,ID,Bonus=4000):
        super().__init__(Name,ID,Bonus)
        
Ishaan = departmentA("Ishaan",1234)

print(Ishaan.Bonus)
