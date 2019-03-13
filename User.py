class User:
    def __init__(self,name,password):
        self.chips = 1000
        self.name = name
        self.password = password
        self.show_browser = self.name + " has " + str(self.chips) + " chips"
    def show_server(self):
        print(self.chips, self.name)

