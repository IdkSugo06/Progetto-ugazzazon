from GestionePagine.MyWidgets.FMyImage import * 
from GestionePagine.VisualizzatoriWidgets.FMyGestoreRiquadriProdotti import * 

#Frame animato
#Classe derivata da una classe di tkInter
class ProdottoNovita(RiquadroProdotto):
    posMousePremuto = [0,0]
    posMouse = [0,0]

    def __init__(self, 
                master : tk.Canvas,
                posx : float, 
                posy : float, 
                height : int, 
                width : int,
                _id : int = 0 ):
        
        super().__init__(
            master = master,
            posx = posx,
            posy = posy,
            height = height,
            width = width,
            _id = _id
        )

    #Aggiorna posizione, zoom e mostra il widget
    def UpdatePhysics(self, deltaTime : float):
        #Calcolo la posizione considerando la velocità
        self.posx += self.velx * deltaTime
        self.posy += self.vely * deltaTime

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
        self.iAnteprimaProdotto.SetZoomIstantaneo((self.zoomAttualeMouse**4))
        self.iAnteprimaProdotto.Show()
        self.forget()
        self.place(x = self.posx, 
                   y = self.posy, 
                   height= self.height * self.zoomAttualeMouse * self.zoomIstantaneo, 
                   width= self.width * self.zoomAttualeMouse * self.zoomIstantaneo, 
                   anchor="center")

    # GET E SET
    #Ritorna la posizione in screenUnits
    def GetPos(self): 
        return [self.posx, self.posy]
    #Setta la posizione in screenUnits
    def SetPos(self, x : int, y : int): 
        self.posx = x
        self.posy = y
    #Aggiunge un valore alla posizione in screenUnits
    def AddPos(self, deltax : int, deltay : int): 
        self.posx += deltax
        self.posy += deltay
    #Setta la velocità istantaneo
    def SetVelocita(self, velx : float, vely : float):
        self.velx = velx
        self.vely = vely
    #Setta la velocità istantaneo
    def MultVelocita(self, f : float):
        self.velx *= f
        self.vely *= f
    #Setta la dimensione in screenUnit
    def SetDim(self, height : float, width : float): 
        self.height = height
        self.width = width
    #Setta lo zoom istantaneo
    def SetZoomIstantaneo(self, zoomIstantaneo : float):
        self.zoomIstantaneo = zoomIstantaneo