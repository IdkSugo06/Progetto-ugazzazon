
class MyEvent:
    def __init__(self, lvlErrore : int = 0, descrizione : str = ""):
        self.lvlErrore = lvlErrore
        self.descrizione = descrizione
    

#Singleton
class MyEventHandler:
    __myEventHandler = None

    # COSTRUTTORE
    def __init__(self):
        self.fatalErrorOccurred = False
        self.errors = []
    
    # METODI
    def __throw(self, event : MyEvent):
        if event.lvlErrore > 0:
            self.errors.append(event)
            if event.lvlErrore == 3:
                self.fatalErrorOccurred = True

    # METODI INTERFACCIA
    @staticmethod
    def Init():
        if MyEventHandler.__myEventHandler == None:
            MyEventHandler.__myEventHandler = MyEventHandler()

    @staticmethod
    def GetMyEventHandler():
        if MyEventHandler.__myEventHandler == None:
            MyEventHandler.__myEventHandler = MyEventHandler()
        return MyEventHandler.__myEventHandler
    
    @staticmethod
    def Throw(event : MyEvent):
        MyEventHandler.__myEventHandler.__throw(event)
    @staticmethod
    def CheckFatalErrorOccurred():
        return MyEventHandler.__myEventHandler.fatalErrorOccurred
    @staticmethod
    def GetErrors():
        return MyEventHandler.__myEventHandler.errors

MyEventHandler.Init()