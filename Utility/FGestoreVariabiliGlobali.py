# PATH DATABASE
DATABASE_PATH = "DatabaseProdotti\\"
DATABASE_PRODOTTI_PATH = "DatabaseProdotti\\Prodotti\\"
DATABASE_IMMAGINI_PATH = "DatabaseProdotti\\Immagini\\"
DATABASE_FILE_CARATTERISTICHE_PRODOTTO_PATH = DATABASE_PRODOTTI_PATH + "CaratteristicheProdotto.txt"

IMMAGINE_DEFAULT_ANTEPRIMA = DATABASE_IMMAGINI_PATH + "IMG_DEFANTEPRIMA.jpeg"


# IMPOSTAZIONI INIZIALI FINESTRA
LARGHEZZA_SCHERMO_INIZIALE = 1200
ALTEZZA_SCHERMO_INIZIALE = 700
MIN_LARGHEZZA_SCHERMO = 700
MIN_ALTEZZA_SCHERMO = 394
MAX_LARGHEZZA_SCHERMO = 2560
MAX_ALTEZZA_SCHERMO = 1440
OFFSET_ORIZZONTALE_SCHERMO = (int((1/20) * LARGHEZZA_SCHERMO_INIZIALE))
OFFSET_VERTICALE_SCHERMO = ((int(1/20) * ALTEZZA_SCHERMO_INIZIALE))


# IMPOSTAZIONI ESECUZIONE CODICE
class GestoreVariabiliGlobali(): #Singleton
    #Istanza statica 
    gestoreVariabiliGlobali = None
    
    #Costruttore
    def __init__(self):
        self.running = True
        self.dimensioniFinestra = [LARGHEZZA_SCHERMO_INIZIALE, ALTEZZA_SCHERMO_INIZIALE]
        self.mousePosFrameCorrente = [0,0]
        self.mousePosFramePrecedente = [0,0]

    # GET E INIT ISTANZA STATICA
    @staticmethod
    def GetGestoreVariabiliGlobali(): #Ritorno l'istanza statica 
        if GestoreVariabiliGlobali.gestoreVariabiliGlobali == None:
            GestoreVariabiliGlobali.gestoreVariabiliGlobali = GestoreVariabiliGlobali()
        return GestoreVariabiliGlobali.gestoreVariabiliGlobali
    
    @staticmethod
    def Init(): #Inizializzo l'istanza statica
        if GestoreVariabiliGlobali.gestoreVariabiliGlobali == None:
            GestoreVariabiliGlobali.gestoreVariabiliGlobali = GestoreVariabiliGlobali()
    
    # INTERFACCE
    @staticmethod
    def IGetRunning():
        return GestoreVariabiliGlobali.gestoreVariabiliGlobali.running
    @staticmethod
    def ISetRunning(_bool : bool):
        GestoreVariabiliGlobali.gestoreVariabiliGlobali.running = _bool

    @staticmethod
    def IGetDimensioniFinestra():
        return GestoreVariabiliGlobali.gestoreVariabiliGlobali.dimensioniFinestra
    @staticmethod
    def ISetDimensioniFinestra(dimensioniFinestra : list[int]):
        GestoreVariabiliGlobali.gestoreVariabiliGlobali.dimensioniFinestra = dimensioniFinestra

    #La posizione del mouse sarà salvata qua per permettere a tutte le classi di accederci in qualsiasi momento
    #Sarà anche possibile calcolarsi il deltaPos
    @staticmethod
    def IGetMousePosFrameCorrente():
        return GestoreVariabiliGlobali.gestoreVariabiliGlobali.mousePosFrameCorrente
    @staticmethod
    def IGetMousePosFramePrecedente():
        return GestoreVariabiliGlobali.gestoreVariabiliGlobali.mousePosFramePrecedente
    @staticmethod
    def IGetDeltaMousePos():
        mousePosFrameCorrente = GestoreVariabiliGlobali.IGetMousePosFrameCorrente()
        mousePosFramePrecedente = GestoreVariabiliGlobali.IGetMousePosFramePrecedente()
        return [mousePosFrameCorrente[0] - mousePosFramePrecedente[0], mousePosFrameCorrente[1] - mousePosFramePrecedente[1]]
    @staticmethod
    def IUpdateMousePos(newMousePosx : float, newMousePosy : float):
        GestoreVariabiliGlobali.gestoreVariabiliGlobali.mousePosFramePrecedente = GestoreVariabiliGlobali.gestoreVariabiliGlobali.mousePosFrameCorrente
        GestoreVariabiliGlobali.gestoreVariabiliGlobali.mousePosFrameCorrente = [newMousePosx, newMousePosy]

GestoreVariabiliGlobali.Init()