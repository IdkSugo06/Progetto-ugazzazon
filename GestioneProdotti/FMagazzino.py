from GestioneProdotti.FProdotto import *
from GestioneProdotti.FCaratteristicheProdotto import *

class Magazzino:
    def __init__(self):
        pass

    def GetProdotto(self, idProdotto : int) -> Prodotto: #-1 se non trovato
        return 