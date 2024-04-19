from GestionePagine.MyWidgets.FTKmodules import *
from GestioneProdotti.FCaratteristicheProdotto import *

#Questa classe gestirà dei frame che permetteranno la modifica delle caratteristiche
class GestoreFiltri:
    
    # COSTRUTTORE
    def __init__(self,
                 master : tk.Frame,
                 leftmostpoint : int,
                 topy : int,
                 width : int,
                 height : int
                 ):
        
        #Salvo le caratteristiche modificate dal gestore
        self.__caratteristicheProdotto = CaratteristicheProdotto(True)
        
        #Salvo gli attributi che mi serviranno
        #Calcolo l'altezza totale
        altezzaTotale = len(CaratteristicheProdotto.dicts_caratteristiche_intToStr) * height
        for tipoCaratteristica in CaratteristicheProdotto.dicts_caratteristiche_intToStr: altezzaTotale += len(tipoCaratteristica) * height
        self.__topnw = [leftmostpoint, topy]
        self.__dim = [width, altezzaTotale]
        

        # INTERFACCIA
        #Creo il frame principale
        self.__fFramePrincipale = tk.Frame(master = master, bg = "blue")
        self.__fFramePrincipale.grid_propagate(False)
        self.__fFramePrincipale.pack_propagate(True)

        #Creo il frame di supporto per la scritta "Filtri"
        self.__fFrameScrittaFiltri = tk.Frame(master = self.__fFramePrincipale)
        self.__fFrameScrittaFiltri.pack(expand = True, side = "top", fill = "both")
        self.__fFrameScrittaFiltri.columnconfigure(0, weight=1)
        self.__fFrameScrittaFiltri.rowconfigure(0, weight=1)
        self.__fFrameScrittaFiltri.grid_propagate(False)
        #Creo la label per la scritta "Filtri"
        self.__lScrittaFiltri = tk.Label(master = self.__fFramePrincipale, text = "Filtri:", font = "Arial 24 italic")
        self.__lScrittaFiltri.grid(row = 0, column = 0, sticky = "nsew")


        # CREAZIONE BOTTONI E SCRITTE FILTRI
        #Per ogni caratteristica
        self.__afFrameScritteCaratteristiche = []
        self.__alScritteCaratteristiche = []
        self.__acbBottoniCaratteristiche = []
        self.__acbBottoniCaratteristiche_abool = []

        contatoreScritte = 0
        numTipoCaratteristica = 0
        for tipoCaratteristica in self.__caratteristicheProdotto.GetCaratteristiche():
            #Creo il frame di supporto e la scritta dei tipiCaratteristica
            self.__afFrameScritteCaratteristiche.append(tk.Frame(master = self.__fFramePrincipale, bg = "pink"))
            self.__afFrameScritteCaratteristiche[contatoreScritte].pack(expand = True, side = "top", fill = "both")
            self.__afFrameScritteCaratteristiche[contatoreScritte].columnconfigure(0, weight = 1)
            self.__afFrameScritteCaratteristiche[contatoreScritte].rowconfigure(0, weight = 1)
            self.__afFrameScritteCaratteristiche[contatoreScritte].grid_propagate(False)
            self.__alScritteCaratteristiche.append(tk.Label(master = self.__afFrameScritteCaratteristiche[contatoreScritte],
                                                            text = CaratteristicheProdotto.tipiCaratteristiche[numTipoCaratteristica] + ":",
                                                            font = "Arial 18 italic",
                                                            anchor = "w"))
            self.__alScritteCaratteristiche[contatoreScritte].grid(row = 0, column = 0, sticky = "nsew")
            contatoreScritte += 1


            #Per ogni caratteristica
            numCaratteristica = 0
            for caratteristica in tipoCaratteristica:
                #Creo il frame di supporto e la scritta delle caratteristiche e dei bottoni
                self.__afFrameScritteCaratteristiche.append(tk.Frame(master = self.__fFramePrincipale, bg = "blue"))
                self.__afFrameScritteCaratteristiche[contatoreScritte].pack(expand = True, side = "top", fill = "both")
                self.__afFrameScritteCaratteristiche[contatoreScritte].columnconfigure(0, weight = 5)
                self.__afFrameScritteCaratteristiche[contatoreScritte].columnconfigure(1, weight = 1)
                self.__afFrameScritteCaratteristiche[contatoreScritte].rowconfigure(0, weight = 1)
                self.__afFrameScritteCaratteristiche[contatoreScritte].grid_propagate(False)
                self.__alScritteCaratteristiche.append(tk.Label(master = self.__afFrameScritteCaratteristiche[contatoreScritte],
                                                                text = CaratteristicheProdotto.dicts_caratteristiche_intToStr[numTipoCaratteristica][numCaratteristica],
                                                                font = "Arial 16",
                                                                anchor = "w"))
                self.__alScritteCaratteristiche[contatoreScritte].grid(row = 0, column = 0, sticky = "nsew")

                #Creo i bottoni
                self.__acbBottoniCaratteristiche_abool.append(tk.BooleanVar(value = True))
                self.__acbBottoniCaratteristiche.append(tk.Checkbutton(master = self.__afFrameScritteCaratteristiche[contatoreScritte],
                                                                       variable = self.__acbBottoniCaratteristiche_abool[contatoreScritte - numTipoCaratteristica - 1],
                                                                       command = self.UpdateCaratteristicheProdotto))
                self.__acbBottoniCaratteristiche[contatoreScritte - numTipoCaratteristica - 1].grid(row = 0, column = 1, sticky = "nsew")

                #Incremento le variabili di iterazione
                contatoreScritte += 1
                numCaratteristica += 1
            numTipoCaratteristica += 1
    

    # Getter
    def UpdateCaratteristicheProdotto(self) -> None:
        #Salvo le caratteristiche per non chiamare la funzione piu volte
        _caratteristiche = self.GetCaratteristiche()

        #Per ogni caratteristica la setto al valore della variabile associata al bottone
        idTot = 0
        for idTipoCaratteristica in range(len(_caratteristiche)):
            
            #Variabile utilizzata per confermare che ci sia almeno una categoria di prodotti selezionata
            trueTrovato = False 
            for idCaratteristica in range(len(_caratteristiche[idTipoCaratteristica])):
                
                #Check se il booleano è true
                _bool = self.__acbBottoniCaratteristiche_abool[idTot].get()
                if _bool: trueTrovato = True

                self.__caratteristicheProdotto.SetCaratteristica(idTipoCaratteristica, idCaratteristica, _bool)
                idTot += 1
            
            #Imposto la prima a true se nessuno lo è
            if not trueTrovato: 
                self.__caratteristicheProdotto.SetCaratteristica(idTipoCaratteristica, 0, True)
                self.__acbBottoniCaratteristiche_abool[idTot - idCaratteristica - 1].set(True)
                LOG.IPrint("È stato tentata la rimozione di tutte le caratteristiche di uno stesso tipo durante l'impostazione di un filtro", 1)

    def GetCaratteristicheProdotto(self) -> CaratteristicheProdotto:
        return self.__caratteristicheProdotto
    def GetCaratteristiche(self) -> list[list[bool]]:
        return self.__caratteristicheProdotto.GetCaratteristiche()
    def GetCaratteristica(self, idTipoCaratteristica : int, idCaratteristica : int) -> bool:
        return self.__caratteristicheProdotto.GetCaratteristica(idTipoCaratteristica, idCaratteristica)
    
    # METODI
    def UpdateGraphics(self):
        self.__fFramePrincipale.place(x = self.__topnw[0], y = self.__topnw[1],
                                      width = self.__dim[0], height = self.__dim[1],
                                      anchor = "nw")
        
    def myBind(self, event : str, function):
        self.__fFramePrincipale.bind(event, function)
        self.__fFrameScrittaFiltri.bind(event, function)
        self.__lScrittaFiltri.bind(event, function)

        for widget in self.__afFrameScritteCaratteristiche:
            widget.bind(event, function)
        for widget in self.__alScritteCaratteristiche:
            widget.bind(event, function)
        for widget in self.__acbBottoniCaratteristiche:
            widget.bind(event, function)

