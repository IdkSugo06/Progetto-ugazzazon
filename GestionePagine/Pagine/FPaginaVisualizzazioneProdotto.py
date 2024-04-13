from GestionePagine.FGestorePagine import *

#PaginaVisualizzazioneProdotto sarà una delle molte pagine derivate da PaginaGenerica
#Verranno salvate e caricate quando necessario in una lista nel gestorePagine
#(useremo il polimorfismo)
class PaginaVisualizzazioneProdotto(PaginaGenerica): #Singleton
    #Creo un'istanza statica
    paginaVisualizzazioneProdotto = None

    # INTERFACCE
    @staticmethod
    def Init(): #Inizializzo l'istanza statica (il costruttore aggiungerà l'istanza statica alla lista nel gestorePagine)
        #Se l'istanza non è ancora stata creata, la creo
        if PaginaVisualizzazioneProdotto.paginaVisualizzazioneProdotto == None:
            PaginaVisualizzazioneProdotto.paginaVisualizzazioneProdotto = PaginaVisualizzazioneProdotto()
    @staticmethod
    def GetPaginaVisualizzazioneProdotto(): #Metodo per accedere all'istanza statica
        #Se l'istanza non è ancora stata creata, la creo
        if PaginaVisualizzazioneProdotto.paginaVisualizzazioneProdotto == None:
            PaginaVisualizzazioneProdotto.paginaVisualizzazioneProdotto = PaginaVisualizzazioneProdotto()
        #Ritorno l'istanza statica
        return PaginaVisualizzazioneProdotto.paginaVisualizzazioneProdotto 
    
    # COSTRUTTORE
    def __init__(self): #Definisco il layout e aggiungo la pagina al gestorePagine

        #Aggiungo la pagina al gestorePagine
        GestorePagine.IAddPagina(self)

        #Definisco il layout

        #PRIMA RIGA
        self.fPrimaRiga = ttk.Frame(master = GestorePagine.IGetWindow())

        self.evBarraDiRicerca_str = tk.StringVar() #Creo la variabile associata alla barra di ricerca
        self.evBarraDiRicerca_str.set("Dai spazio alla tua immaginazione") #Setto la variabile per far apparire qualcosa anche se non ancora cercato nulla
        self.eBarraDiRicerca = ttk.Entry(   #Creo la barra di ricerca che si estenderà il più possibile
            master = self.fPrimaRiga, 
            text = "Vai a prova", 
            textvariable = self.evBarraDiRicerca_str, 
            foreground = "#969696") 
        self.eBarraDiRicerca.bind('<FocusIn>', PaginaVisualizzazioneProdotto.BarraDiRicercaSelezionata)
        self.eBarraDiRicerca.bind('<FocusOut>', PaginaVisualizzazioneProdotto.BarraDiRicercaDeselezionata)

        #SECONDA RIGA
        self.fSecondaRiga = ttk.Frame(master = GestorePagine.IGetWindow())
        

    # METODI
    def CaricaPagina(self, *args): #Override metodo virtuale classe PaginaGenerica, visualizzo il contenuto della pagina
        self.tHome.pack()
    def NascondiPagina(self):
        return
    
    #Quando selezionata, imposto il colore della barra di ricerca scuro
    @staticmethod
    def BarraDiRicercaSelezionata(event):
        PaginaVisualizzazioneProdotto.paginaVisualizzazioneProdotto.eBarraDiRicerca.configure(foreground = "#000000")

    #Quando deselezionata, imposto il colore della barra di ricerca piu chiaro
    @staticmethod
    def BarraDiRicercaDeselezionata(event):
        PaginaVisualizzazioneProdotto.paginaVisualizzazioneProdotto.eBarraDiRicerca.configure(foreground = "#969696")

#Inizializzo la pagina di prova
PaginaVisualizzazioneProdotto.Init()
