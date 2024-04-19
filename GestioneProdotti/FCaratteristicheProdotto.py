from Utility.FUtility import *

#Creo un file che gestisca 
class CaratteristicheProdotto:
    tipiCaratteristiche = [] #list[str] dei tipi di caratteristiche
    dicts_caratteristiche_intToStr = [] #lista di dizionari delle caratteristiche

    def __init__(self, _bool : bool = False):
        self.__caratteristiche = [] #list[list[bool]]
        
        #Per ogni tipo caratteristica aggiungo una lista contenente False per tutte le caratteristiche possibili 
        for tipoCaratteristica in CaratteristicheProdotto.dicts_caratteristiche_intToStr:
            self.__caratteristiche.append([_bool] * len(tipoCaratteristica))    

    #Lettura caratteristiche da file
    @staticmethod
    def Init():
        try:
            #Apro il file
            fileStream = open(DATABASE_FILE_CARATTERISTICHE_PRODOTTO_PATH)
            
            #Leggo i tipiCaratteristiche e li ciclo per processarne uno alla volta
            tipoCaratteristiche_str = fileStream.readlines()
            for tipoCaratteristica_str in tipoCaratteristiche_str:
                
                #Splitto caratteristiche dal nome del tipoCaratteristica
                temp = tipoCaratteristica_str.split('{')
                nomeTipoCaratteristica = temp[0]
                tipoCaratteristica_str = '{' + temp[1]
                CaratteristicheProdotto.tipiCaratteristiche.append(nomeTipoCaratteristica)

                #Creo il dizionario che conterra il tipoCaratteristica analizzato
                tipoCaratteristica = {}

                #Per ogni tipoCaratteristica ne distinguo le diverse caratteristiche e le ciclo           
                caratteristiche_str = tipoCaratteristica_str[1:-2].split(",") #[1:-2] per rimuovere {}\n
                for caratteristica_str in caratteristiche_str:
                    
                    #Distinguo le coppie key-value e le aggiungo al dizionario creato
                    keyValue = caratteristica_str.split(":") #splitto in array [key : str, value : str] 
                    tipoCaratteristica[int(keyValue[0])] = str(keyValue[1][1:-1])
                    
                #Aggiungo infine tutti i tipiCaratteristica analizzati
                CaratteristicheProdotto.dicts_caratteristiche_intToStr.append(tipoCaratteristica)
            fileStream.close()
        except:
            LOG.IPrint("Errore critico durante la lettura delle caratteristiche di un prodotto", 3)
            MyEventHandler.Throw(MyEvent(3,"Errore durante la lettura del file caratteristicheProdotto ì"))


    # GETTER
    def GetCaratteristiche(self):
        return self.__caratteristiche
    def GetCaratteristica(self, idTipoCaratteristica : int, idCaratteristica : int):
        return self.__caratteristiche[idTipoCaratteristica][idCaratteristica]
    def SetCaratteristica(self, idTipoCaratteristica : int, idCaratteristica : int, value : bool):
        self.__caratteristiche[idTipoCaratteristica][idCaratteristica] = value
    def InvertCaratteristica(self, idTipoCaratteristica : int, idCaratteristica : int):
        self.__caratteristiche[idTipoCaratteristica][idCaratteristica] = not self.__caratteristiche[idTipoCaratteristica][idCaratteristica]

CaratteristicheProdotto.Init()

#leggi il file, path su gestorevariabiliglobali.py
#(esempio da cancellare):   CaratteristicheProdotto.dicts_caratteristiche_intToStr[0].append({0 : "uomo", 1 : "donna"}) 