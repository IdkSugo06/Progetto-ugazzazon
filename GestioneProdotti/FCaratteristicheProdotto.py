class CaratteristicheProdotto:
    dicts_caratteristiche_intToStr = []

    def __init__(self):
        self.__caratteristiche = [] #list[list[bool]]
        
        #Per ogni tipo caratteristica aggiungo una lista contenente False per tutte le caratteristiche possibili 
        for tipoCaratteristica in CaratteristicheProdotto.dicts_caratteristiche_intToStr:
            self.__caratteristiche.append([[False] * len(tipoCaratteristica)])    

    # GETTER
    def GetCaratteristica(self, idTipoCaratteristica : int, idCaratteristica : int):
        return self.__caratteristiche[idTipoCaratteristica][idCaratteristica]
    def SetCaratteristica(self, idTipoCaratteristica : int, idCaratteristica : int, value : bool):
        self.__caratteristiche[idTipoCaratteristica][idCaratteristica] = value


#leggi il file, path su gestorevariabiliglobali.py
#(esempio da cancellare)
CaratteristicheProdotto.dicts_caratteristiche_intToStr[0].append({0 : "uomo", 1 : "donna"}) 