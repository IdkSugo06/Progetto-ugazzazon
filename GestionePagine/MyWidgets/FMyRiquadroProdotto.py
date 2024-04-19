from GestionePagine.MyWidgets.FMyImage import *
from GestioneProdotti.FMagazzino import *

#Frame minimamente animato
#Classe derivata da una classe di tkInter
#Conterra un prodotto statico, con solo l'animazione di zoom quando ci passa il mouse sopra
class RiquadroProdotto(tk.Frame):
    FONT_NOME_PRODOTTO = "Montserrat 18 italic"
    FONT_TIPO_PRODOTTO = "Montserrat 12 italic"
    VELOCITA_ZOOM = 0.001
    ZOOM_MOUSE_PUNTATO = 0.2 #Zoom imposto dal mouse quando ci passa sopra (graduale)

    def __init__(self,
                 master : tk.Frame,
                 width : int, 
                 height : int,
                 posx : int,
                 posy : int,
                 _id : int = 0
                 ):
        
        super().__init__(master = master, highlightthickness = 1, highlightbackground="#333333")

        # ATTRIBUTI MOVIMENTO
        #Imposto le coordinate iniziali
        self.posx = posx
        self.posy = posy
        #Creo attributi per la velocita
        self.velx = 0
        self.vely = 0
        #Imposto le dimensioni iniziali
        self.height = height
        self.width = width
        self.zoomIstantaneo = 1
        #Altro
        self.id = _id

        #Setto gli attributi del frame principale
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=3)
        self.rowconfigure(1, weight=2)
        self.grid_propagate(False)
        
        #Creo un frame per la parte superiore
        self.fFrameParteSuperiore = tk.Frame(master=self)
        self.fFrameParteSuperiore.grid(row = 0, column=0, sticky="nsew")
        self.fFrameParteSuperiore.columnconfigure(0, weight=1)
        self.fFrameParteSuperiore.rowconfigure(0, weight=1)
        self.fFrameParteSuperiore.grid_propagate(False)

        #Creo un canvas per sostenere l'immagine e l'immagine
        self.cCanvasAnteprimaProdotto = tk.Canvas(master = self.fFrameParteSuperiore)
        self.cCanvasAnteprimaProdotto.grid(row = 0, column=0, sticky="nsew")
        self.iAnteprimaProdotto = MyImageTK(canvas = self.cCanvasAnteprimaProdotto, path = (IMMAGINE_DEFAULT_ANTEPRIMA))
        self.iAnteprimaProdotto.Show()

        #Creo un frame per la parte inferiore
        self.fFrameParteInferiore = tk.Frame(master=self)
        self.fFrameParteInferiore.grid(row = 1, column=0,sticky="nsew")
        self.fFrameParteInferiore.columnconfigure(0, weight=2)
        self.fFrameParteInferiore.columnconfigure(1, weight=1)
        self.fFrameParteInferiore.columnconfigure(2, weight=2)
        self.fFrameParteInferiore.rowconfigure(0, weight=3)
        self.fFrameParteInferiore.rowconfigure(1, weight=2)
        self.fFrameParteInferiore.rowconfigure(2, weight=3)
        self.fFrameParteInferiore.grid_propagate(False)

        #NOME PRODOTTO
        #Creo un frame a supporto del nome prodotto
        self.fFrameNomeProdotto = tk.Frame(master = self.fFrameParteInferiore)
        self.fFrameNomeProdotto.grid(row = 0, column= 0, columnspan=3, sticky="nsew")
        self.fFrameNomeProdotto.columnconfigure(0, weight=1)
        self.fFrameNomeProdotto.rowconfigure(0, weight=1)
        self.fFrameNomeProdotto.grid_propagate(False)
        self.fFrameNomeProdotto.pack_propagate(False)

        #Creo una variabile associata al testo scritto, questo permetterà di cambiarla in qualsiasi momento
        self.tvNomeProdotto_str = tk.StringVar()
        self.tvNomeProdotto_str.set("Ops, qualosa è andato storto")
        self.tNomeProdotto = tk.Label(master = self.fFrameNomeProdotto,
                                        textvariable = self.tvNomeProdotto_str,
                                        font = RiquadroProdotto.FONT_NOME_PRODOTTO)
        self.tNomeProdotto.grid(row = 0, column= 0,sticky="nsew")

        #TIPO PRODOTTO
        #Creo un frame a supporto
        self.fFrameTipoProdotto = tk.Frame(master = self.fFrameParteInferiore)
        self.fFrameTipoProdotto.grid(row = 1, column= 0, columnspan=2, sticky="nsew")
        self.fFrameTipoProdotto.columnconfigure(0, weight=1)
        self.fFrameTipoProdotto.rowconfigure(0, weight=1)
        self.fFrameTipoProdotto.grid_propagate(False)
        self.fFrameTipoProdotto.pack_propagate(False)

        #Creo una variabile associata al testo scritto, questo permetterà di cambiarla in qualsiasi momento
        self.tvTipoProdotto_str = tk.StringVar()
        self.tvTipoProdotto_str.set("Ops, qualosa è andato storto")
        self.tTipoProdotto = tk.Label(master = self.fFrameTipoProdotto, 
                                        textvariable = self.tvNomeProdotto_str, 
                                        font = RiquadroProdotto.FONT_TIPO_PRODOTTO)
        self.tTipoProdotto.pack(side="left")


        #Creo un supporto per l'ingrandimento quando il mouse punta a questo widget
        self.bind("<Enter>", self.MousePuntato)
        self.bind("<Leave>", self.MouseNonPiuPuntato)
        self.mousePuntato = False
        self.zoomAttualeMouse = 0.98
        self.zoomRichiestoMouse = 1

    # METODI UPDATE
    def UpdatePhysics(self, deltaTime : float):
        #Calcolo lo zoom
        dZoom = (self.zoomRichiestoMouse - self.zoomAttualeMouse) #differenza di zoom
        abs_dZoom = abs(dZoom)
        if abs_dZoom < 0.03: return
        segno = dZoom / abs_dZoom
        coeff = abs_dZoom**4
        d = 0.2
        v = -19.65 
        self.zoomAttualeMouse += segno * self.zoomRichiestoMouse*(coeff / (coeff + exp(v*(deltaTime + d))))


    def UpdateGraphics(self):
        if self.zoomAttualeMouse <= self.zoomRichiestoMouse - 0.01 or self.zoomAttualeMouse >= self.zoomRichiestoMouse + 0.01:
            self.iAnteprimaProdotto.SetZoomIstantaneo(self.zoomAttualeMouse**2)
            self.iAnteprimaProdotto.Show()
            self.forget()
            self.place(x = self.posx, 
                       y = self.posy, 
                       height = self.height * self.zoomAttualeMouse, 
                       width = self.width * self.zoomAttualeMouse, 
                       anchor ="center")
    # METODI
    def AssociaProdotto(self, prodotto : Prodotto):
        self


    # METODI EVENTI
    #Aumenta lo zoom
    def MousePuntato(self, event):
        self.mousePuntato = True
        self.zoomRichiestoMouse = 1 + RiquadroProdotto.ZOOM_MOUSE_PUNTATO
    #Ripristina lo zoom
    def MouseNonPiuPuntato(self, event):
        self.mousePuntato = False
        self.zoomRichiestoMouse = 1

    # BINDING EVENTI
    #Per bindare un evento al frame, dobbiamo bindarlo a tutti i suoi figli
    #altrimenti non sarà catchato (se si preme il mouse sul label il frame non lo saprà)
    def myBind(self, event : str, _function):
        self.bind(event, _function)
        self.fFrameParteInferiore.bind(event, _function)
        self.cCanvasAnteprimaProdotto.bind(event, _function)
        self.tNomeProdotto.bind(event, _function)
        self.tTipoProdotto.bind(event, _function)