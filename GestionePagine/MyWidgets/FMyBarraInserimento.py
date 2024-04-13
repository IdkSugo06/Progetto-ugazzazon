from GestionePagine.MyWidgets.FTKmodules import * 

#Barra di inserimento personalizzata, contiene metodi per leggere e scrivere in qualsiasi momento
#Classe derivata da una classe di tkInter
class BarraInserimento(ttk.Entry):
    def __init__(self, master, text : str = "", coloreSelezione :str = "#000000", coloreDeselezione : str = "#969696"):
        #Salvo i colori selezione e deselezione passati come parametro
        self.coloreSelezione = coloreSelezione
        self.coloreDeselezione = coloreDeselezione

        #Creo una variabile di supporto per settare e leggere il valore della barra di ricerca
        self.barraInserimento_str = tk.StringVar() 
        self.barraInserimento_str.set(text)

        #Inizializzo la barra di ricerca
        super().__init__(master = master,
                        text = text, 
                        textvariable = self.barraInserimento_str, 
                        foreground = self.coloreDeselezione
                        )
        
        #Associo gli eventi focus in e out con i metodi
        self.bind('<FocusIn>', lambda event, _self = self  : BarraInserimento.BarraRicercaSelezionata(_self, event))
        self.bind('<FocusOut>', lambda event, _self = self : BarraInserimento.BarraRicercaDeselezionata(_self, event))

    def BarraRicercaSelezionata(self, event):
        self.configure(foreground = self.coloreSelezione)
    
    def BarraRicercaDeselezionata(self, event):
        self.configure(foreground = self.coloreDeselezione)

    def GetContenuto(self):
        return self.barraInserimento_str.get()
    
    def SetContenuto(self, text : str):
        self.barraInserimento_str.set(text)