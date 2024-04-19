from Utility.FUtility import *
from GestioneProdotti.FCaratteristicheProdotto import *


TODO IMPLEMENTARE SOFTMAX E TUTTO QUELLO CHE RIGUARDA LE CARATTERISTICHE PRODOTTO


class Account():

    def __init__(self, 
                 username : str,
                 password : str):
        
        #Creo gli attributi per l'accesso
        self.__username = username
        self.__password = password

        self.__numeroRicerche = 0
        self.__preferenzeProdotti = CaratteristicheProdotto()
        self.__carrello = []
        self.__quantitaProdottiCarrello = []


    # METODI credenziali
    def GetUsername(self):
        return self.__username
    def GetPassword(self):
        return self.__password
    def SetUsername(self, newUsername : str):
        self.__username = newUsername
    def SetPassword(self, newPassword : str):
        self.__password = newPassword

    # METODI preferenze prodotti
    def GetNumeroRicerche(self):
        return self.__numeroRicerche
    def AddNumeroRicerche(self, quantita : int = 0):
        self.__numeroRicerche += quantita
    def GetPreferenzeProdotti(self):
        return CaratteristicheProdotto()

    # METODI carrello
    def GetCarrello(self):
        return (self.__carrello)
    def GetQuantitaCarrello(self):
        return (self.__quantitaProdottiCarrello)
    
    #Aggiungo un prodotto data una quantita
    def AggiungiProdottoCarrello(self, idProdotto : int, quantita : int = 1):
        #Controllo che gia non sia presente nel carrello (la scorro )
        if idProdotto in self.__carrello:
            posizioneProdotto = self.__carrello.index(idProdotto)
            self.__quantitaProdottiCarrello[posizioneProdotto] += quantita
            
        #Salvo il prodotto e la quantita
        self.__carrello.append(idProdotto)
        self.__quantitaProdottiCarrello.append(idProdotto)

    #Rimuovo un prodotto data una quantita
    def RimuoviProdotto(self, idProdotto : int, quantita : int = 1) -> bool:
        #Controllo che il prodotto ci sia, altrimenti printo un avviso
        if not (idProdotto in self.__carrello):
            LOG.IPrint("Il prodotto da rimuovere dal carrello non è stato trovato", LOG_WARNING)

        #Getto la posizione prodotto e diminuisco la quantita del valore specificato
        posizioneProdotto = self.__carrello.index(idProdotto)
        self.__quantitaProdottiCarrello[posizioneProdotto] -= quantita

        #Se minore di 0 lo rimuovo
        if self.__quantitaProdottiCarrello[posizioneProdotto] == 0:
            if self.__quantitaProdottiCarrello[posizioneProdotto] < 0:
                LOG.IPrint("È stata rimossa una quantita non disponibile di prodotti da un carrello utente", LOG_ERROR)
            self.__carrello.pop(posizioneProdotto)
            self.__quantitaProdottiCarrello.pop(posizioneProdotto)
        
