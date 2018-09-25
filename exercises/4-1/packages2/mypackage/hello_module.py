class Hello:
    def __init__(self):
        self.version="1.0"

    def askName(self):
        name = input("What's your name?")
        return name
        
    def sayHello(self):
        print("hello %s" % self.askName())