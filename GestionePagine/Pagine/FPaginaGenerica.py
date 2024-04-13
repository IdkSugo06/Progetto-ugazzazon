from GestionePagine.MyWidgets.FMyWidgets import *

#PaginaGenerica sarà una classe padre per derivare
#le pagine con un ruolo specifico in seguito
class PaginaGenerica():
    #Creo un dizionario per facilitare e generalizzare l'id delle pagine
    numOf_pagineEsistenti = 0
    PagNameToId_dict = dict()

    def __init__(self, _istanzaGestorePagine):
        #Salviamo una referenza al gestorePagine (singleton) 
        self.gestorePagine = _istanzaGestorePagine
    
    # METODI STATICI
    @staticmethod
    def AggiungiPagina(nomePagina : str):
        PaginaGenerica.PagNameToId_dict[nomePagina] = PaginaGenerica.numOf_pagineEsistenti
        PaginaGenerica.numOf_pagineEsistenti += 1
        return (PaginaGenerica.numOf_pagineEsistenti - 1)
        
    @staticmethod
    def GetIdPagina(nomePagina : str):
        try:
            return PaginaGenerica.PagNameToId_dict[nomePagina]
        except:
            LOG.log("Errore nella chiamata PaginaGenerica.GetIdPagina, nomePagina non trovato : " + str(nomePagina), LOG_ERROR)
            return 0

    # METODI VIRTUALI (verrà eseguito l'override)
    def CaricaPagina(self, *args): #Metodo virtuale
        return
    def NascondiPagina(self): #Metodo virtuale
        return
    def UpdatePagina(self, deltaTime): #Metodo virtuale
        return