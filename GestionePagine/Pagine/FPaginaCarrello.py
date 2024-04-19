from GestionePagine.FGestorePagine import *

#PaginaCarrello sarà una delle molte pagine derivate da PaginaGenerica
#Verranno salvate e caricate quando necessario in una lista nel gestorePagine
#(useremo il polimorfismo)
class PaginaCarrello(PaginaGenerica): #Singleton
    #Creo un'istanza statica
    __paginaCarrello = None

    # INTERFACCE
    @staticmethod
    def Init(): #Inizializzo l'istanza statica (il costruttore aggiungerà l'istanza statica alla lista nel gestorePagine)
        #Se l'istanza non è ancora stata creata, la creo
        if PaginaCarrello.__paginaCarrello == None:
            PaginaCarrello.__paginaCarrello = PaginaCarrello()
    @staticmethod
    def GetPaginaCarrello(): #Metodo per accedere all'istanza statica
        #Se l'istanza non è ancora stata creata, la creo
        if PaginaCarrello.__paginaCarrello == None:
            PaginaCarrello.__paginaCarrello = PaginaCarrello()
        #Ritorno l'istanza statica
        return PaginaCarrello.__paginaCarrello 
    
    # COSTRUTTORE
    def __init__(self): #Definisco il layout e aggiungo la pagina al gestorePagine
        #Aggiungo poi la pagina al gestorePagine
        PaginaGenerica.AggiungiPagina("carrello")
        GestorePagine.IAddPagina(self)

        COLORE_SFONDO_SCHEDA_ACCESSO = "#EBEBEB"

        #Definisco il layout della pagina
        #Creo il FRAME PRINCIPALE
        self.__fFramePrincipale = ttk.Frame(master = GestorePagine.IGetFramePrincipale())
        self.__fFramePrincipale.columnconfigure(0, weight = 2)
        self.__fFramePrincipale.columnconfigure(1, weight = 5)
        self.__fFramePrincipale.columnconfigure(2, weight = 5)
        self.__fFramePrincipale.rowconfigure(0, weight = 1)
        self.__fFramePrincipale.rowconfigure(1, weight = 2)
        self.__fFramePrincipale.rowconfigure(2, weight = 1)
        self.__fFramePrincipale.rowconfigure(3, weight = 1)
        self.__fFramePrincipale.grid_propagate(False)


        #Creo il BOTTONE HOME
        self.__fFrameBottoneHome = ttk.Frame(master = self.__fFramePrincipale)
        self.__fFrameBottoneHome.grid(row=0, column=0,sticky="nsew")
        self.__fFrameBottoneHome.columnconfigure(0, weight = 4)
        self.__fFrameBottoneHome.columnconfigure(1, weight = 1)
        self.__fFrameBottoneHome.rowconfigure(0, weight = 1)
        self.__fFrameBottoneHome.rowconfigure(1, weight = 2)
        self.__fFrameBottoneHome.grid_propagate(False)
        #Creo un ulteriore frame per contenere completamente il bottone, il frame principale è solo per semplicità
        self.__fFrameBottoneHomeMinore = ttk.Frame(master = self.__fFrameBottoneHome)
        self.__fFrameBottoneHomeMinore.grid(row=0, column=0,sticky="nsew")
        self.__fFrameBottoneHomeMinore.columnconfigure(0, weight = 1)
        self.__fFrameBottoneHomeMinore.rowconfigure(0, weight = 1)
        self.__fFrameBottoneHomeMinore.grid_propagate(False)
        #Creo il bottone
        self.__bBottoneHome = ttk.Button(master=self.__fFrameBottoneHomeMinore, text="Home", command=self.ImpostaPaginaHome)
        self.__bBottoneHome.grid(row=0, column=0,sticky="nsew")


        #Creo il CANVAS CENTRALE SCORRIBILE
        self.__fFrameCanvasCentrale = ttk.Frame(master = self.__fFramePrincipale)
        self.__fFrameCanvasCentrale.grid(row=1, column=1,sticky="nsew")
        self.__fFrameCanvasCentrale.columnconfigure(0, weight = 1)
        self.__fFrameCanvasCentrale.rowconfigure(0, weight = 1)
        self.__fFrameCanvasCentrale.grid_propagate(False)
        #Creo il canvas scorribile
        self.__cCanvasCentrale = tk.Canvas(master = self.__fFrameCanvasCentrale,
                                           scrollregion=(0,0,GestoreVariabiliGlobali.IGetDimensioniFinestra()[0], 
                                                             GestoreVariabiliGlobali.IGetDimensioniFinestra()[1] * 3))
        self.__cCanvasCentrale.grid(row=0,column=0,sticky="nsew")
        #Creo un frame per rendere il canvas scorrevole
        self.__fFrameInternoCanvasCentrale = tk.Frame(master = self.__fFrameCanvasCentrale, bg = "red")
        self.__fFrameInternoCanvasCentrale.grid(row = 0, column = 0, rowspan=2, sticky = "nsew")
        self.__fFrameInternoCanvasCentrale.columnconfigure(0, weight = 1)
        self.__fFrameInternoCanvasCentrale.rowconfigure(0, weight = 1)
        self.__fFrameInternoCanvasCentrale.grid_propagate(False)
        self.__cCanvasCentrale.create_window((0,0),
                                                window = self.__fFrameInternoCanvasCentrale,
                                                anchor = "nw", 
                                                width = GestoreVariabiliGlobali.IGetDimensioniFinestra()[0],
                                                height = GestoreVariabiliGlobali.IGetDimensioniFinestra()[1] * 3)


        #Creo il gestore della lista carrello
        self.__gestoreListaCarrello = GestoreRiquadriCarrello(master=self.__fFrameInternoCanvasCentrale)

    # METODI
    #Override metodo virtuale classe PaginaGenerica, visualizzo il contenuto della pagina
    def CaricaPagina(self, *args): 
        self.__fFramePrincipale.grid(row = 0, column = 0, sticky = "nsew")

        #Popola lista carrello
        self.__gestoreListaCarrello.AggiornaCarrello([])

    #Override metodo virtuale classe PaginaGenerica, nascondo il contenuto della pagina
    def NascondiPagina(self):
        self.__fFramePrincipale.grid_forget()
    
    @staticmethod
    def ImpostaPaginaHome(): 
        GestorePagine.ICaricaPagina(PaginaGenerica.GetIdPagina("home"))
 
    
#Inizializzo la pagina home
PaginaCarrello.Init()

