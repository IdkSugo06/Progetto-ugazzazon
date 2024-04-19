class Prodotto:
    def __init__(self,nome,tipoProdotto,prezzo,caratteristiche,popolarità,pathImmagine,pathImmagineanteprima):
        self.__nome=nome
        self.__tipoProdotto=tipoProdotto
        self.__prezzo=prezzo
        self.__caratteristiche=caratteristiche
        self.__popolarità=popolarità
        self.__pathImmagine=pathImmagine
        self.__pathImmagineanteprima=pathImmagineanteprima


    def GetNome(self):
        return self.__nome
    def GetTipo(self):
        return self.__tipoProdotto
    def GetPrezzo(self):
        return self.__prezzo
    def GetCaratteristiche(self):
        return self.__caratteristiche
    def GetPopolarità(self):
        return self.__popolarità
    def GetPathImmagine(self):
        return self.__pathImmagine
    def GetPathImmagineAnteprima(self):
        return self.__pathImmagineanteprima
    

class CaratteristicheProdotto(Prodotto):
    def __init__(self,diz_caratteristiche,caratteristiche):
        self.diz_caratteristiche=diz_caratteristiche
        self.__caratteristiche=caratteristiche

    def GetCaratteristiche(self):
        return self.__caratteristiche
    
    def GetCorrispondenzaDescrizione(self):
        pass
    def GetCorrispondenzaCaratterisitche(self,carattristica):
        pass 