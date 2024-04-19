from GestionePagine.FGestorePagine import *

#PaginaRicercaProdotto sarà una delle molte pagine derivate da PaginaGenerica
#Verranno salvate e caricate quando necessario in una lista nel gestorePagine
#(useremo il polimorfismo)
class PaginaRicercaProdotto(PaginaGenerica): #Singleton
    #Creo un'istanza statica
    paginaRicercaProdotto = None
    UPDATE_FISICI_OGNI_UPDATE_GRAFICO = 8

    # INTERFACCE
    @staticmethod
    def Init(): #Inizializzo l'istanza statica (il costruttore aggiungerà l'istanza statica alla lista nel gestorePagine)
        #Se l'istanza non è ancora stata creata, la creo
        if PaginaRicercaProdotto.paginaRicercaProdotto == None:
            PaginaRicercaProdotto.paginaRicercaProdotto = PaginaRicercaProdotto()
    @staticmethod
    def GetPaginaRicercaProdotto(): #Metodo per accedere all'istanza statica
        #Se l'istanza non è ancora stata creata, la creo
        if PaginaRicercaProdotto.paginaRicercaProdotto == None:
            PaginaRicercaProdotto.paginaRicercaProdotto = PaginaRicercaProdotto()
        #Ritorno l'istanza statica
        return PaginaRicercaProdotto.paginaRicercaProdotto 
    
    # COSTRUTTORE
    def __init__(self): #Definisco il layout e aggiungo la pagina al gestorePagine
        #Aggiungo poi la pagina al gestorePagine
        PaginaGenerica.AggiungiPagina("ricercaProdotto")
        GestorePagine.IAddPagina(self)
        self.physicsUpdateSinceGraphicUpdate = PaginaRicercaProdotto.UPDATE_FISICI_OGNI_UPDATE_GRAFICO

        #Definisco il layout della pagina
        #Creo il frame principale
        self.fFramePrincipale = ttk.Frame(master = GestorePagine.IGetFramePrincipale())
        self.fFramePrincipale.columnconfigure(0, weight = 1)
        self.fFramePrincipale.bind("<Motion>", lambda event: self.MotionDetected)
        self.fFramePrincipale.rowconfigure(0, weight = 1)
        self.fFramePrincipale.rowconfigure(1, weight = 9)
        self.fFramePrincipale.grid_propagate(False)

        #PARTE SUPERIORE SCHERMO (1/8 schermo)
        #Creo il frame per contenerla, sarà diviso a griglia
        self.fParteSuperioreSchermo = ttk.Frame(master = self.fFramePrincipale)
        self.fParteSuperioreSchermo.grid(row = 0, column = 0, sticky = "nsew")
        self.fParteSuperioreSchermo.columnconfigure(0, weight = 2)
        self.fParteSuperioreSchermo.columnconfigure(1, weight = 16)
        self.fParteSuperioreSchermo.columnconfigure(2, weight = 1)
        self.fParteSuperioreSchermo.columnconfigure(3, weight = 3)
        self.fParteSuperioreSchermo.rowconfigure(0, weight = 1)
        self.fParteSuperioreSchermo.grid_propagate(False)
        self.fParteSuperioreSchermo.pack_propagate(False)
    

        # LOGO
        self.fFrameLogo = tk.Frame(master = self.fParteSuperioreSchermo) #Creo il logo in alto a sinistra
        self.fFrameLogo.grid(row = 0, column = 0, sticky = "nsew") 
        self.fFrameLogo.columnconfigure(0, weight = 1)
        self.fFrameLogo.rowconfigure(0, weight = 1)
        self.fFrameLogo.grid_propagate(False)

        self.cCanvasLogo = tk.Canvas(master = self.fFrameLogo) #Creo il logo in alto a sinistra
        self.cCanvasLogo.grid(row = 0, column = 0, sticky = "nsew") 
        self.myImgLogo = MyImageButton(self.cCanvasLogo, command = self.ImpostaPaginaHome, path = LOGO_PATH)        
        self.myImgLogo.Resize((1/18) * GestoreVariabiliGlobali.IGetDimensioniFinestra()[0],
                              (1/18) * GestoreVariabiliGlobali.IGetDimensioniFinestra()[0])
        self.myImgLogo.Show()
        #Ancoro il logo al frameParteSuperioreSchermo


        # BARRA RICERCA
        #Un frame per contenere la barra di ricerca, sarà suddiviso a griglie
        self.fFrameBarraRicerca = ttk.Frame(master = self.fParteSuperioreSchermo)
        self.fFrameBarraRicerca.grid(row = 0, column = 1, sticky = "nsew")
        self.fFrameBarraRicerca.columnconfigure(0, weight = 1)
        self.fFrameBarraRicerca.columnconfigure(1, weight = 3)
        self.fFrameBarraRicerca.columnconfigure(2, weight = 1)
        self.fFrameBarraRicerca.columnconfigure(3, weight = 48)
        self.fFrameBarraRicerca.columnconfigure(4, weight = 1)
        self.fFrameBarraRicerca.rowconfigure(0, weight = 2)
        self.fFrameBarraRicerca.rowconfigure(1, weight = 1)
        self.fFrameBarraRicerca.rowconfigure(2, weight = 2)
        self.fFrameBarraRicerca.grid_propagate(False)
        #Una barra di ricerca e la barra di ricerca al frame dedicato
        self.eBarraRicerca = BarraInserimento(self.fFrameBarraRicerca, text="Dai spazio alla tua immaginazione")
        self.eBarraRicerca.grid(row = 1, column = 3, sticky = "nsew")
        #Un immagine bottone per confermare la ricerca
        self.fFrameBottoneConfermaRicerca = tk.Frame(master = self.fFrameBarraRicerca, bg = "blue")
        self.fFrameBottoneConfermaRicerca.grid(row = 1, column = 1, sticky = "nsew")
        self.fFrameBottoneConfermaRicerca.columnconfigure(0, weight = 1)
        self.fFrameBottoneConfermaRicerca.rowconfigure(0, weight = 1)
        self.fFrameBottoneConfermaRicerca.grid_propagate(False)
        self.cCanvasImgLenteIngrandimento = tk.Canvas(master = self.fFrameBottoneConfermaRicerca, highlightbackground="#969696", highlightthickness=1)
        self.cCanvasImgLenteIngrandimento.grid(row = 0, column = 0, sticky = "nsew")
        self.myImgLenteIngrandimento = MyImageButton(canvas = self.cCanvasImgLenteIngrandimento, command = self.ConfermaRicerca, path = LENTE_INGRANDIMENTO_PATH)
        self.myImgLenteIngrandimento.Resize(((1/37) * GestoreVariabiliGlobali.IGetDimensioniFinestra()[0]),
                                            ((1/36) * GestoreVariabiliGlobali.IGetDimensioniFinestra()[0]))
        self.myImgLenteIngrandimento.Show()


        # BOTTONE ACCESSO
        #Creo un frame per il pulsante di accesso
        self.fFramePulsanteAccesso = ttk.Frame(master = self.fParteSuperioreSchermo)
        self.fFramePulsanteAccesso.grid(row = 0, column = 2, sticky = "nsew")
        self.fFramePulsanteAccesso.columnconfigure(0, weight = 1)
        self.fFramePulsanteAccesso.columnconfigure(1, weight = 1)
        self.fFramePulsanteAccesso.columnconfigure(2, weight = 2)
        self.fFramePulsanteAccesso.columnconfigure(3, weight = 8)
        self.fFramePulsanteAccesso.columnconfigure(4, weight = 1)
        self.fFramePulsanteAccesso.rowconfigure(0, weight = 15)
        self.fFramePulsanteAccesso.rowconfigure(1, weight = 1)
        self.fFramePulsanteAccesso.rowconfigure(2, weight = 6)
        self.fFramePulsanteAccesso.rowconfigure(3, weight = 1)
        self.fFramePulsanteAccesso.rowconfigure(4, weight = 15)
        #Creo il pulsante di accesso e lo ancoro
        self.bPulsanteAccesso = ttk.Button(master = self.fFramePulsanteAccesso, command = PaginaRicercaProdotto.ImpostaPaginaAccesso)
        self.bPulsanteAccesso.grid(row = 1, column = 1, columnspan = 3, rowspan=3, sticky = "nsew")
        #Un immagine bottone per mostrarne il funzionamento
        self.fFrameImmagineBottoneAcesso = tk.Frame(master = self.fFramePulsanteAccesso, bg = "blue")
        self.fFrameImmagineBottoneAcesso.grid(row = 2, column = 2, sticky = "nsew")
        self.fFrameImmagineBottoneAcesso.columnconfigure(0, weight = 1)
        self.fFrameImmagineBottoneAcesso.rowconfigure(0, weight = 1)
        self.fFrameImmagineBottoneAcesso.grid_propagate(False)
        self.cCanvasImmagineBottoneAccesso = tk.Canvas(master = self.fFrameImmagineBottoneAcesso)
        self.cCanvasImmagineBottoneAccesso.grid(row = 0, column = 0, sticky = "nsew")
        self.myImgBottoneAccesso = MyImageButton(canvas = self.cCanvasImmagineBottoneAccesso, command = self.ImpostaPaginaAccesso, path = OMINO_ACCESSO_PATH)
        self.myImgBottoneAccesso.Resize(((1/47) * GestoreVariabiliGlobali.IGetDimensioniFinestra()[0]),
                                        ((1/47) * GestoreVariabiliGlobali.IGetDimensioniFinestra()[0]))   
        self.myImgBottoneAccesso.Show()


        # BOTTONE CARRELLO
        #Creo un frame per il pulsante carrello
        self.fFramePulsanteCarrello = ttk.Frame(master = self.fParteSuperioreSchermo)
        self.fFramePulsanteCarrello.grid(row = 0, column = 3, sticky = "nsew")
        self.fFramePulsanteCarrello.columnconfigure(0, weight = 1)
        self.fFramePulsanteCarrello.columnconfigure(1, weight = 1)
        self.fFramePulsanteCarrello.columnconfigure(2, weight = 4)
        self.fFramePulsanteCarrello.columnconfigure(3, weight = 16)
        self.fFramePulsanteCarrello.columnconfigure(4, weight = 1)
        self.fFramePulsanteCarrello.rowconfigure(0, weight = 4)
        self.fFramePulsanteCarrello.rowconfigure(1, weight = 1)
        self.fFramePulsanteCarrello.rowconfigure(2, weight = 8)
        self.fFramePulsanteCarrello.rowconfigure(3, weight = 1)
        self.fFramePulsanteCarrello.rowconfigure(4, weight = 4)
        #Creo il pulsante di accesso e lo ancoro
        self.bPulsanteCarrello = ttk.Button(master = self.fFramePulsanteCarrello, command = PaginaRicercaProdotto.ImpostaPaginaCarrello)
        self.bPulsanteCarrello.grid(row = 1, column = 1, columnspan=3, rowspan=3, sticky = "nsew")
        #Un immagine bottone per mostrarne il funzionamento
        self.fFrameImmagineBottoneCarrello = tk.Frame(master = self.fFramePulsanteCarrello)
        self.fFrameImmagineBottoneCarrello.grid(row = 2, column = 2, sticky = "nsew")
        self.fFrameImmagineBottoneCarrello.columnconfigure(0, weight = 1)
        self.fFrameImmagineBottoneCarrello.rowconfigure(0, weight = 1)
        self.fFrameImmagineBottoneCarrello.grid_propagate(False)
        self.cCanvasImmagineBottoneCarrello = tk.Canvas(master = self.fFrameImmagineBottoneCarrello)
        self.cCanvasImmagineBottoneCarrello.grid(row = 0, column = 0, sticky = "nsew")
        self.myImgBottoneCarrello = MyImageButton(canvas = self.cCanvasImmagineBottoneCarrello, command = self.ImpostaPaginaCarrello, path = CARRELLO_PATH)
        self.myImgBottoneCarrello.Resize(((1/27) * GestoreVariabiliGlobali.IGetDimensioniFinestra()[0]),
                                        ((1/27) * GestoreVariabiliGlobali.IGetDimensioniFinestra()[0]))   
        self.myImgBottoneCarrello.Show()


        #PARTE INFERIORE SCHERMO (7/8 schermo)
        #Creo il frame per contenerla, sarà diviso a griglia, 3 colonne principali
        self.fParteInferioreSchermo = ttk.Frame(master = self.fFramePrincipale)
        self.fParteInferioreSchermo.grid(row = 1, column = 0, sticky = "nsew")
        self.fParteInferioreSchermo.columnconfigure(0, weight = 1)
        self.fParteInferioreSchermo.rowconfigure(0, weight = 1)
        self.fParteInferioreSchermo.grid_propagate(False)


        # CANVAS SCORRIBILE
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


        # CLASSI AGGIUNTIVE       
        #Creo il gestore dei prodotti cercati
        self.gestoreRiquadriProdotti = GestoreRiquadriProdotti(master = self.fFrameScorrevoleCanvasInferiore, 
                                            numeroColonne = 4,
                                            numeroRighe = 6,
                                            centerx = (1/2) * GestoreVariabiliGlobali.IGetDimensioniFinestra()[0] + 50, 
                                            topy = (1/22) * GestoreVariabiliGlobali.IGetDimensioniFinestra()[1],
                                            width = (1/7.5) * GestoreVariabiliGlobali.IGetDimensioniFinestra()[0],
                                            height = (1/4.2) * GestoreVariabiliGlobali.IGetDimensioniFinestra()[1],
                                            padx = (1/25) * GestoreVariabiliGlobali.IGetDimensioniFinestra()[0],
                                            pady = (1/25) * GestoreVariabiliGlobali.IGetDimensioniFinestra()[1])
        
        #Creo il gestore filtri
        self.gestoreFiltri = GestoreFiltri(master = self.fFrameScorrevoleCanvasInferiore, 
                                            leftmostpoint = 0,
                                            topy = (1/22) * GestoreVariabiliGlobali.IGetDimensioniFinestra()[1],
                                            width = (1/6) * GestoreVariabiliGlobali.IGetDimensioniFinestra()[0],
                                            height = 40)


        # BIND VARI
        #Bindo gli eventi per scorrere
        self.cCanvasParteInferiore.bind("<MouseWheel>", lambda event : self.cCanvasParteInferiore.yview_scroll(int(-event.delta / 60), "units"))
        self.fFrameScorrevoleCanvasInferiore.bind("<MouseWheel>", lambda event : self.cCanvasParteInferiore.yview_scroll(int(-event.delta / 60), "units"))
        self.gestoreRiquadriProdotti.myBind("<MouseWheel>", lambda event : self.cCanvasParteInferiore.yview_scroll(int(-event.delta / 60), "units"))
        self.gestoreFiltri.myBind("<MouseWheel>", lambda event : self.cCanvasParteInferiore.yview_scroll(int(-event.delta / 60), "units"))
    


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
        self.gestoreRiquadriProdotti.UpdatePhysics(deltaTime)

        #Every 8 updates update the graphics
        if self.physicsUpdateSinceGraphicUpdate >= PaginaRicercaProdotto.UPDATE_FISICI_OGNI_UPDATE_GRAFICO:
            self.physicsUpdateSinceGraphicUpdate = 0

            #Update the graphics
            self.gestoreRiquadriProdotti.UpdateGraphics()
            self.gestoreFiltri.UpdateGraphics()
        self.physicsUpdateSinceGraphicUpdate += 1

    @staticmethod
    def MotionDetected(event):
        return
    
    #Cambio pagine
    @staticmethod
    def ImpostaPaginaHome(tkEvent = None): 
        GestorePagine.ICaricaPagina(PaginaGenerica.GetIdPagina("home"))
    @staticmethod
    def ImpostaPaginaAccesso(tkEvent = None): 
        GestorePagine.ICaricaPagina(PaginaGenerica.GetIdPagina("accesso"))
    @staticmethod
    def ImpostaPaginaCarrello(tkEvent = None): 
        GestorePagine.ICaricaPagina(PaginaGenerica.GetIdPagina("carrello"))  


    #Altre funzioni
    #Da implementare
    def ConfermaRicerca(self, tkEvent = None): 
        pass
    def AggiornaArticoliConsigliati(self): 
        self.gestoreRiquadriProdotti.AggiornaArticoliConsigliati()
    
#Inizializzo la pagina ricercaProdotto
PaginaRicercaProdotto.Init()

