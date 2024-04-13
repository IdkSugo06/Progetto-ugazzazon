class c1:

    def __init__(self):
        self.ciao = "c"
    
    def funzione(self):
        print(self.ciao)
    
    def a(self):
        self.funzione()

class c2(c1):

    def __init__(self):
        super().__init__()
        self.funzione()
    
    def funzione(self):
        print("ah")

class c3(c2):
    def __init__(self):
        super().__init__()

c = c3()
c.funzione()
c.a()

