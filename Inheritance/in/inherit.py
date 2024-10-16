class Parent:
    def __init__(self,Eyes,Hair):
        self.Eyes = Eyes
        self.Hair = Hair
        
class child(Parent):
    def __init__(self,Parent):
        super().__init__(Parent.Eyes,Parent.Hair)
        
Father = Parent("Brown","Black")
Son = child(Father)

print(Son.Eyes)