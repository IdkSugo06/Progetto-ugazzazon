from GestionePagine.MyWidgets.FMyRiquadroProdotto import * 


#Creo una classe per la gestione dei prodotti mostrati nelle pagine
class GestoreRiquadriProdotti:

    def __init__(self, 
                 master: tk.Frame,
                 numeroRighe : int,
                 numeroColonne : int,
                 height : int,
                 width : int,
                 centerx : int,
                 topy : int,
                 padx : int = 20,
                 pady : int = 20,
                ):
        
        #Salvo gli attributi utili
        self.__numeroRighe = numeroRighe
        self.__numeroColonne = numeroColonne
        self.__numeroProdotti = numeroRighe * numeroColonne
        self.__heightRiquadroProdotto = height
        self.__widthRiquadroProdotto = width
        
        self.__padx = padx
        self.__pady = pady
        
        self.__lunghezzaRiga = (numeroColonne - 1) * padx + numeroColonne * width
        self.__altezzaColonna = (numeroRighe - 1) * pady + numeroRighe * height
        self.__centro = [centerx, topy + self.__lunghezzaRiga//2]

        #Creo i prodotti e li contengo in una lista di liste organizzate come [[riga],[riga],...]
        self.prodotti = [[RiquadroProdotto(
            master = master, 
            width = width, 
            height = height,
            posx = int((centerx - (self.__lunghezzaRiga/2)) + (x * (width + padx)) + (width/2)),
            posy = int(topy + (y * (height + pady)) + (height/2)),
            ) for x in range(numeroColonne)] for y in range(numeroRighe)]

        
    # METODI
    def UpdatePhysics(self, deltaTime : float):
        for riga in self.prodotti:
            for riquadroProdotto in riga:
                riquadroProdotto.UpdatePhysics(deltaTime)
    
    def UpdateGraphics(self):
        for riga in self.prodotti:
            for riquadroProdotto in riga:
                riquadroProdotto.UpdateGraphics()

    def AggiornaArticoliConsigliati(self):
        return

    # BIND EVENTI
    def myBind(self, evento : str, function):
        for riga in self.prodotti:
            for riquadroProdotto in riga:
                riquadroProdotto.myBind(evento, function)


   
    
    

