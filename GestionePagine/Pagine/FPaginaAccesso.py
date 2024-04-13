from GestionePagine.FGestorePagine import *

#PaginaAccesso sarà una delle molte pagine derivate da PaginaGenerica
#Verranno salvate e caricate quando necessario in una lista nel gestorePagine
#(useremo il polimorfismo)
class PaginaAccesso(PaginaGenerica): #Singleton
    #Creo un'istanza statica
    __paginaAccesso = None

    # INTERFACCE
    @staticmethod
    def Init(): #Inizializzo l'istanza statica (il costruttore aggiungerà l'istanza statica alla lista nel gestorePagine)
        #Se l'istanza non è ancora stata creata, la creo
        if PaginaAccesso.__paginaAccesso == None:
            PaginaAccesso.__paginaAccesso = PaginaAccesso()
    @staticmethod
    def GetPaginaAccesso(): #Metodo per accedere all'istanza statica
        #Se l'istanza non è ancora stata creata, la creo
        if PaginaAccesso.__paginaAccesso == None:
            PaginaAccesso.__paginaAccesso = PaginaAccesso()
        #Ritorno l'istanza statica
        return PaginaAccesso.__paginaAccesso 
    
    # COSTRUTTORE
    def __init__(self): #Definisco il layout e aggiungo la pagina al gestorePagine
        #Aggiungo poi la pagina al gestorePagine
        PaginaGenerica.AggiungiPagina("accesso")
        GestorePagine.IAddPagina(self)

        COLORE_SFONDO_SCHEDA_ACCESSO = "#EBEBEB"

        #Definisco il layout della pagina
        #Creo il frame principale
        self.fFramePrincipale = ttk.Frame(master = GestorePagine.IGetFramePrincipale())
        self.fFramePrincipale.columnconfigure(0, weight = 1)
        self.fFramePrincipale.columnconfigure(1, weight = 6)
        self.fFramePrincipale.columnconfigure(2, weight = 5)
        self.fFramePrincipale.columnconfigure(3, weight = 8)
        self.fFramePrincipale.rowconfigure(0, weight = 1)
        self.fFramePrincipale.rowconfigure(1, weight = 7)
        self.fFramePrincipale.rowconfigure(2, weight = 16)
        self.fFramePrincipale.rowconfigure(3, weight = 2)
        self.fFramePrincipale.rowconfigure(4, weight = 1)
        self.fFramePrincipale.rowconfigure(5, weight = 6)
        self.fFramePrincipale.grid_propagate(False)

        #Creo il frame per il pulsante Home
        self.bPulsanteHome = ttk.Button(master = self.fFramePrincipale, text = "Home", command = PaginaAccesso.ImpostaPaginaHome)
        self.bPulsanteHome.grid(row = 0, column = 0, sticky = "nsew")
        #Creo pulsante registrazione
        self.bPulsanteRegistrazione = ttk.Button(master = self.fFramePrincipale, text = "Registrazione", command = PaginaAccesso.ImpostaPaginaRegistrazione)
        self.bPulsanteRegistrazione.grid(row = 4, column = 2, sticky = "nsew")
        #Creo frame scheda accesso
        self.fFrameSchedaAccesso = tk.Frame(master = self.fFramePrincipale, background=COLORE_SFONDO_SCHEDA_ACCESSO, relief="ridge")
        self.fFrameSchedaAccesso.grid(row = 2, column = 2, sticky = "nsew")
        self.fFrameSchedaAccesso.columnconfigure(0, weight = 3)
        self.fFrameSchedaAccesso.columnconfigure(1, weight = 1)
        self.fFrameSchedaAccesso.columnconfigure(2, weight = 3)
        self.fFrameSchedaAccesso.columnconfigure(3, weight = 4)
        self.fFrameSchedaAccesso.columnconfigure(4, weight = 1)
        self.fFrameSchedaAccesso.columnconfigure(5, weight = 2)
        self.fFrameSchedaAccesso.rowconfigure(0, weight = 4)
        self.fFrameSchedaAccesso.rowconfigure(1, weight = 3)
        self.fFrameSchedaAccesso.rowconfigure(2, weight = 2)
        self.fFrameSchedaAccesso.rowconfigure(3, weight = 2)
        self.fFrameSchedaAccesso.rowconfigure(4, weight = 1)
        self.fFrameSchedaAccesso.rowconfigure(5, weight = 2)
        self.fFrameSchedaAccesso.rowconfigure(6, weight = 2)
        self.fFrameSchedaAccesso.rowconfigure(7, weight = 2)
        self.fFrameSchedaAccesso.rowconfigure(8, weight = 4)
        self.fFrameSchedaAccesso.rowconfigure(9, weight = 2)
        self.fFrameSchedaAccesso.grid_propagate(False)
        #Creo il logo
        self.tLogo = ttk.Label(master = self.fFrameSchedaAccesso, text = "Logo", background=COLORE_SFONDO_SCHEDA_ACCESSO)
        self.tLogo.grid(row = 0, column=1, columnspan=2, sticky="nsew")
        #Creo la scritta accesso
        self.tScrittaAccesso = ttk.Label(master = self.fFrameSchedaAccesso, text = "Accedi", background=COLORE_SFONDO_SCHEDA_ACCESSO, font = "Merriweather 54 italic")
        self.tScrittaAccesso.grid(row = 0, column=3, columnspan=2, sticky="nsew")
        #Creo la scritta username
        self.tScrittaUsername = ttk.Label(master = self.fFrameSchedaAccesso, text = "Username:", background=COLORE_SFONDO_SCHEDA_ACCESSO)
        self.tScrittaUsername.grid(row = 1, column = 2, columnspan=2, sticky= "nsew")
        #Creo l'entry inserimento username
        self.myeBarraInserimentoUsername = BarraInserimento(master = self.fFrameSchedaAccesso, text = "Username")
        self.myeBarraInserimentoUsername.grid(row = 2, column = 2, columnspan=2, sticky="nsew")
        #Creo la scritta password
        self.tScrittaPassword = ttk.Label(master = self.fFrameSchedaAccesso, text = "Password:", background= COLORE_SFONDO_SCHEDA_ACCESSO)
        self.tScrittaPassword.grid(row = 4, column = 2, columnspan=2, sticky= "nsew")
        #Creo l'entry inserimento password
        self.myeBarraInserimentoPassword = BarraInserimento(master = self.fFrameSchedaAccesso, text = "Password")
        self.myeBarraInserimentoPassword.grid(row = 5, column = 2, columnspan=2, sticky="nsew")
        #Creo pulsante accesso
        self.bPulsanteTentativoAccesso = ttk.Button(master=self.fFrameSchedaAccesso, text = "Accesso", command = PaginaAccesso.TentativoAccesso)
        self.bPulsanteTentativoAccesso.grid(row = 8, column=1, columnspan=4, sticky="nsew")


    # METODI
    #Override metodo virtuale classe PaginaGenerica, visualizzo il contenuto della pagina
    def CaricaPagina(self, *args): 
        self.fFramePrincipale.grid(row = 0, column = 0, sticky = "nsew")

    #Override metodo virtuale classe PaginaGenerica, nascondo il contenuto della pagina
    def NascondiPagina(self):
        self.fFramePrincipale.grid_forget()
    
    @staticmethod
    def ImpostaPaginaHome(): 
        GestorePagine.ICaricaPagina(PaginaGenerica.GetIdPagina("home"))

    @staticmethod
    def ImpostaPaginaRegistrazione(): 
        GestorePagine.ICaricaPagina(PaginaGenerica.GetIdPagina("registrazione"))

    @staticmethod
    def ImpostaPaginaCarrello(): 
        GestorePagine.ICaricaPagina(PaginaGenerica.GetIdPagina("carrello"))    

    #Da implementare
    @staticmethod
    def TentativoAccesso():
        #Legge password e username dalla barra inserimento
        return
    
#Inizializzo la pagina home
PaginaAccesso.Init()

