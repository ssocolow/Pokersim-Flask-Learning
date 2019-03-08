class User:
    def __init__(self,name,password):
        self.chips = 1000
        self.name = name
        self.password = password
    def show(self):
        print(self.chips, self.name)
