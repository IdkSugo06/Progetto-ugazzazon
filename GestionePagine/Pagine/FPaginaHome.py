from GestionePagine.FGestorePagine import *

#PaginaHome sarà una delle molte pagine derivate da PaginaGenerica
#Verranno salvate e caricate quando necessario in una lista nel gestorePagine
#(useremo il polimorfismo)
class PaginaHome(PaginaGenerica): #Singleton
    #Creo un'istanza statica
    paginaHome = None
    UPDATE_FISICI_OGNI_UPDATE_GRAFICO = 8

    # INTERFACCE
    @staticmethod
    def Init(): #Inizializzo l'istanza statica (il costruttore aggiungerà l'istanza statica alla lista nel gestorePagine)
        #Se l'istanza non è ancora stata creata, la creo
        if PaginaHome.paginaHome == None:
            PaginaHome.paginaHome = PaginaHome()
    @staticmethod
    def GetPaginaHome(): #Metodo per accedere all'istanza statica
        #Se l'istanza non è ancora stata creata, la creo
        if PaginaHome.paginaHome == None:
            PaginaHome.paginaHome = PaginaHome()
        #Ritorno l'istanza statica
        return PaginaHome.paginaHome 
    
    # COSTRUTTORE
    def __init__(self): #Definisco il layout e aggiungo la pagina al gestorePagine
        #Aggiungo poi la pagina al gestorePagine
        PaginaGenerica.AggiungiPagina("home")
        GestorePagine.IAddPagina(self)
        self.physicsUpdateSinceGraphicUpdate = PaginaHome.UPDATE_FISICI_OGNI_UPDATE_GRAFICO

        #Definisco il layout della pagina
        #Creo il frame principale
        self.fFramePrincipale = ttk.Frame(master = GestorePagine.IGetFramePrincipale())
        self.fFramePrincipale.columnconfigure(0, weight = 1)
        self.fFramePrincipale.bind("<Motion>", self.MotionDetected)
        self.fFramePrincipale.rowconfigure(0, weight = 1)
        self.fFramePrincipale.rowconfigure(1, weight = 9)
        self.fFramePrincipale.grid_propagate(False)

        #PARTE SUPERIORE SCHERMO (1/8 schermo)
        #Creo il frame per contenerla, sarà diviso a griglia
        self.fParteSuperioreSchermo = ttk.Frame(master = self.fFramePrincipale)
        self.fParteSuperioreSchermo.grid(row = 0, column = 0, sticky = "nsew")
        self.fParteSuperioreSchermo.columnconfigure(0, weight = 4)
        self.fParteSuperioreSchermo.columnconfigure(1, weight = 16)
        self.fParteSuperioreSchermo.columnconfigure(2, weight = 1)
        self.fParteSuperioreSchermo.columnconfigure(3, weight = 3)
        self.fParteSuperioreSchermo.rowconfigure(0, weight = 1)
        self.fParteSuperioreSchermo.grid_propagate(False)
        
        #Definisco i widget che mi serviranno
        #Un logo
        self.tLogo = ttk.Label(master = self.fParteSuperioreSchermo, text="Search") #Creo il logo in alto a sinistra
        #Ancoro il logo al frameParteSuperioreSchermo
        self.tLogo.grid(row = 0, column = 0, sticky = "nsew") 

        #Un frame per contenere la barra di ricerca, sarà suddiviso a griglie
        self.fFrameBarraRicerca = ttk.Frame(master = self.fParteSuperioreSchermo)
        self.fFrameBarraRicerca.grid(row = 0, column = 1, sticky = "nsew")
        self.fFrameBarraRicerca.columnconfigure(0, weight = 1)
        self.fFrameBarraRicerca.columnconfigure(1, weight = 18)
        self.fFrameBarraRicerca.columnconfigure(2, weight = 1)
        self.fFrameBarraRicerca.rowconfigure(0, weight = 2)
        self.fFrameBarraRicerca.rowconfigure(1, weight = 1)
        self.fFrameBarraRicerca.rowconfigure(2, weight = 2)
        #Una barra di ricerca e la barra di ricerca al frame dedicato
        self.eBarraRicerca = BarraInserimento(self.fFrameBarraRicerca, text="Dai spazio alla tua immaginazione")
        self.eBarraRicerca.grid(row = 1, column = 1, sticky = "nsew")

        #Creo un frame per il pulsante di accesso
        self.fFramePulsanteAccesso = ttk.Frame(master = self.fParteSuperioreSchermo)
        self.fFramePulsanteAccesso.grid(row = 0, column = 2, sticky = "nsew")
        self.fFramePulsanteAccesso.columnconfigure(0, weight = 1)
        self.fFramePulsanteAccesso.columnconfigure(1, weight = 10)
        self.fFramePulsanteAccesso.columnconfigure(2, weight = 1)
        self.fFramePulsanteAccesso.rowconfigure(0, weight = 2)
        self.fFramePulsanteAccesso.rowconfigure(1, weight = 1)
        self.fFramePulsanteAccesso.rowconfigure(2, weight = 2)
        #Creo il pulsante di accesso e lo ancoro
        self.bPulsanteAccesso = ttk.Button(master = self.fFramePulsanteAccesso, command = PaginaHome.ImpostaPaginaAccesso)
        self.bPulsanteAccesso.grid(row = 1, column = 1, sticky = "nsew")

        #Creo un frame per il pulsante carrello
        self.fFramePulsanteCarrello = ttk.Frame(master = self.fParteSuperioreSchermo)
        self.fFramePulsanteCarrello.grid(row = 0, column = 3, sticky = "nsew")
        self.fFramePulsanteCarrello.columnconfigure(0, weight = 1)
        self.fFramePulsanteCarrello.columnconfigure(1, weight = 10)
        self.fFramePulsanteCarrello.columnconfigure(2, weight = 1)
        self.fFramePulsanteCarrello.rowconfigure(0, weight = 1)
        self.fFramePulsanteCarrello.rowconfigure(1, weight = 2)
        self.fFramePulsanteCarrello.rowconfigure(2, weight = 1)
        #Creo il pulsante di accesso e lo ancoro
        self.bPulsanteCarrello = ttk.Button(master = self.fFramePulsanteCarrello, command = PaginaHome.ImpostaPaginaCarrello)
        self.bPulsanteCarrello.grid(row = 1, column = 1, sticky = "nsew")


        #PARTE INFERIORE SCHERMO (7/8 schermo)
        #Creo il frame per contenerla, sarà diviso a griglia, 3 colonne principali
        self.fParteInferioreSchermo = ttk.Frame(master = self.fFramePrincipale)
        self.fParteInferioreSchermo.grid(row = 1, column = 0, sticky = "nsew")
        self.fParteInferioreSchermo.columnconfigure(0, weight = 1)
        self.fParteInferioreSchermo.rowconfigure(0, weight = 1)
        self.fParteInferioreSchermo.grid_propagate(False)

        #Creo il canvas che coprirà la parte inferiore
        self.cCanvasParteInferiore = tk.Canvas(master = self.fParteInferioreSchermo, 
                                               scrollregion=(0,0,GestoreVariabiliGlobali.IGetDimensioniFinestra()[0], 
                                                             GestoreVariabiliGlobali.IGetDimensioniFinestra()[1] * 3))
        self.cCanvasParteInferiore.grid(row = 0, column = 0, sticky = "nsew")
        self.cCanvasParteInferiore.columnconfigure(0, weight = 1)
        self.cCanvasParteInferiore.rowconfigure(0, weight = 1)
        self.cCanvasParteInferiore.grid_propagate(False)

        #Creo un frame per rendere il canvas scorrevole
        self.fFrameScorrevoleCanvasInferiore = tk.Frame(master = self.fParteInferioreSchermo, bg = "red")
        self.fFrameScorrevoleCanvasInferiore.grid(row = 0, column = 0, sticky = "nsew")
        self.fFrameScorrevoleCanvasInferiore.columnconfigure(0, weight = 1)
        self.fFrameScorrevoleCanvasInferiore.rowconfigure(0, weight = 1)
        self.fFrameScorrevoleCanvasInferiore.grid_propagate(False)
        self.cCanvasParteInferiore.create_window((0,0),
                                                window = self.fFrameScorrevoleCanvasInferiore,
                                                anchor = "nw", 
                                                width = GestoreVariabiliGlobali.IGetDimensioniFinestra()[0],
                                                height = GestoreVariabiliGlobali.IGetDimensioniFinestra()[1] * 3)

        #Creo il gestore dei prodotti novita
        self.gestoreProdottiNovita = GestoreProdottiNovita(master = self.fFrameScorrevoleCanvasInferiore, 
                                            numeroProdotti = 6,
                                            centerx = (1/2) * GestoreVariabiliGlobali.IGetDimensioniFinestra()[0], 
                                            centery = (1/4) * GestoreVariabiliGlobali.IGetDimensioniFinestra()[1],
                                            width = (1/4.5) * GestoreVariabiliGlobali.IGetDimensioniFinestra()[0],
                                            height = (1/2.8) * GestoreVariabiliGlobali.IGetDimensioniFinestra()[1],
                                            padx = (1/23) * GestoreVariabiliGlobali.IGetDimensioniFinestra()[0])
        
        #Creo il gestore dei prodotti novita
        self.gestoreRiquadriProdotti = GestoreRiquadriProdotti(master = self.fFrameScorrevoleCanvasInferiore, 
                                            numeroColonne = 4,
                                            numeroRighe = 6,
                                            centerx = (1/2) * GestoreVariabiliGlobali.IGetDimensioniFinestra()[0], 
                                            topy = (2/3) * GestoreVariabiliGlobali.IGetDimensioniFinestra()[1],
                                            width = (1/7.5) * GestoreVariabiliGlobali.IGetDimensioniFinestra()[0],
                                            height = (1/4.2) * GestoreVariabiliGlobali.IGetDimensioniFinestra()[1],
                                            padx = (1/25) * GestoreVariabiliGlobali.IGetDimensioniFinestra()[0],
                                            pady = (1/25) * GestoreVariabiliGlobali.IGetDimensioniFinestra()[1])

        #Bindo gli eventi per scorrere
        self.cCanvasParteInferiore.bind("<MouseWheel>", lambda event : self.cCanvasParteInferiore.yview_scroll(int(-event.delta / 60), "units"))
        self.fFrameScorrevoleCanvasInferiore.bind("<MouseWheel>", lambda event : self.cCanvasParteInferiore.yview_scroll(int(-event.delta / 60), "units"))
        self.gestoreProdottiNovita.myBind("<MouseWheel>", lambda event : self.cCanvasParteInferiore.yview_scroll(int(-event.delta / 60), "units"))
        self.gestoreRiquadriProdotti.myBind("<MouseWheel>", lambda event : self.cCanvasParteInferiore.yview_scroll(int(-event.delta / 60), "units"))
    
    # METODI
    #Metodi base o aggiornamento
    def CaricaPagina(self, *args):
        self.fFramePrincipale.grid_propagate(True) #Causes the frame to disappear after the forget and not appear anymore....
        self.fFramePrincipale.grid(row = 0, column = 0, sticky = "nsew")
        self.fFramePrincipale.grid_propagate(False)
    def NascondiPagina(self):
        self.fFramePrincipale.grid_forget()
    def UpdatePagina(self, deltaTime):
        #Update the physics
        self.gestoreProdottiNovita.UpdatePhysics(deltaTime)
        self.gestoreRiquadriProdotti.UpdatePhysics(deltaTime)

        #Every 8 updates update the graphics
        if self.physicsUpdateSinceGraphicUpdate >= PaginaHome.UPDATE_FISICI_OGNI_UPDATE_GRAFICO:
            self.physicsUpdateSinceGraphicUpdate = 0

            #Update the graphics
            self.gestoreProdottiNovita.UpdateGraphics()
            self.gestoreRiquadriProdotti.UpdateGraphics()
        self.physicsUpdateSinceGraphicUpdate += 1

    @staticmethod
    def MotionDetected(event):
        return
    
    #Cambio pagine
    @staticmethod
    def ImpostaPaginaProva():
        GestorePagine.ICaricaPagina(PaginaGenerica.GetIdPagina("prova"))  
    @staticmethod
    def ImpostaPaginaAccesso(): 
        GestorePagine.ICaricaPagina(PaginaGenerica.GetIdPagina("accesso"))
    @staticmethod
    def ImpostaPaginaRegistrazione(): 
        GestorePagine.ICaricaPagina(PaginaGenerica.GetIdPagina("registrazione"))
    @staticmethod
    def ImpostaPaginaCarrello(): 
        GestorePagine.ICaricaPagina(PaginaGenerica.GetIdPagina("carrello"))    

    #Altre funzioni
    #Da implementare
    def AggiornaArticoliConsigliati(self): 
        self.gestoreRiquadriProdotti.AggiornaArticoliConsigliati()
        self.gestoreProdottiNovita.AggiornaArticoliConsigliati()
    
#Inizializzo la pagina home
PaginaHome.Init()

