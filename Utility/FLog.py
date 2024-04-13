# LOG CONSTANTS
LOG_WARNING = 1
LOG_ERROR = 2
LOG_FATAL_ERROR = 3

#Log sarà una classe singleton che si occuperà di gestire i feedback all'interno del programma
class LOG: #singleton
    #Istanza statica
    __log = None

    #Costruttore
    def __init__(self):
        self.debug = True
    
    # METODI ACCESSO AD ISTANZA STATICA
    @staticmethod
    def Init():
        if LOG.__log == None:
            LOG.__log = LOG()
    @staticmethod
    def GetLog():
        if LOG.__log == None:
            LOG.__log = LOG()
        return LOG.__log
    
    # METODI INTERFACCIA
    @staticmethod 
    def IPrint(testo : str, lvlErrore : int = 0):
        LOG.__log.__Print(testo, lvlErrore)
    @staticmethod 
    def log(testo : str, lvlErrore : int = 0):
        LOG.__log.__Print(testo, lvlErrore)

    # METODI 
    def __Print(self, testo : str, lvlErrore : int = 0):
        if self.debug == False: return 
        avviso = "[UNSPECIFIED]"
        if lvlErrore == 0:    avviso = ""
        elif lvlErrore == 1:  avviso = "[AVVISO]"
        elif lvlErrore == 2:  avviso = "[ERRORE]"
        elif lvlErrore == 3:  avviso = "[ERRORE FATALE]"
        print(avviso, testo)

LOG.Init()