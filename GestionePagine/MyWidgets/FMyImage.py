from GestionePagine.MyWidgets.FTKmodules import * 


#Creo una classe per gestire le immagini, cambio immagini, ridimensionamento ecc...
class MyImageTK:

    def __init__(self, canvas : tk.Canvas, path = ""):
        
        #Creo le variabili per il supporto di cambio immagine e ridimensionamento
        self.parentCanvas = canvas
        self.originalImage = None
        self.resizedImage = None
        #Per evitare il flickering, salvo due immagini, una dello scorso ridimensionamento e una dell'attuale
        #Se non salvassi il ridimensionamento precedente, il create_image non trovando l'immagine non si caricherebbe
        self.immagineTKridimensionamentoPrecedente = None
        self.immagineTKridimensionamentoAttuale = None
        self.aspectRatio = None
        self.canvasWidth = canvas.winfo_reqwidth()
        self.canvasHeight = canvas.winfo_reqheight()
        self.canvasAspectRatio = self.canvasWidth / self.canvasHeight

        #Per animazione
        self.zoomIstantaneo = 1

        #Per evitare il flickering quando elimino l'immagine e la rimpiazzo con quella corretta, salvo un istanza di due immagini
        #l'immagine piazzata nello scorso frame e l'immagine piazzata nel frame attuale
        self.imgLastFrameIstance = None
        self.imgThisFrameIstance = None

        #Verifico che la path sia stata inserita o sia valida
        if path == "":
            LOG.log("Non è satata inserita una path nel costruttore delle immagini", 1)
        try: 
            #Importo l'immagine e ne calcolo l'aspect ratio
            self.originalImage = Image.open(path)
            self.aspectRatio = self.originalImage.size[0] / self.originalImage.size[1]

            #Riscalo l'immagine per non avere problemi di prestazioni 
            self.originalImage.resize((200,200)) 

            #Creo una variabile per contenere una copia dell'immagine riscalata e poter attingere 
            #ogni volta dall'immagine originale, così da non perdere qualità
            self.resizedImage = Image.open(path)
            self.imageTk = ImageTk.PhotoImage(self.originalImage)
            self.parentCanvas.bind("<Configure>", self.ResizeEvent)

            #Creo l'istanza così da poterla cancellare nel prossimo update
            self.imgThisFrameIstance = self.parentCanvas.create_image(self.canvasWidth/2, self.canvasHeight/2, image = self.immagineTKridimensionamentoAttuale, anchor = "center")
        except: 
            LOG.log("È stata rilevata una path non valida: " + str(path), 2)
        
    def Show(self, _anchor = "center"):
        #Cancello l'immagine precedente e carico la nuova, lasciandone sempre in vista due in modo da evitare il "flickering"
        self.parentCanvas.delete(self.imgLastFrameIstance)
        self.imgLastFrameIstance = self.imgThisFrameIstance
        self.imgThisFrameIstance = self.parentCanvas.create_image(self.canvasWidth/2, self.canvasHeight/2, image = self.immagineTKridimensionamentoAttuale, anchor = _anchor)
    

    def Resize(self, width : int, height : int):
        #Cambio gli attributi e salvo i nuovi
        self.canvasWidth = width
        self.canvasHeight = height
        self.canvasAspectRatio = width / height

        #Controllo l'aspect ratio e ridimensiono l'immagine in base a quello
        if self.canvasAspectRatio < self.aspectRatio:
            dim = [(int) (width * self.zoomIstantaneo),
                   (int) (height * self.zoomIstantaneo / self.aspectRatio)]
        else:
            dim = [(int) (width * self.zoomIstantaneo * self.aspectRatio),
                   (int) (height * self.zoomIstantaneo)]
            
        #Ricalcolo l'immagine e l'immagine tk
        self.resizedImage = self.originalImage.resize(dim)
        self.immagineTKridimensionamentoPrecedente = self.immagineTKridimensionamentoAttuale
        self.immagineTKridimensionamentoAttuale = ImageTk.PhotoImage(self.resizedImage)

    def ChangeImage(self, newPath : str): #Necessita di resize e show per essere cambiata
        try: 
            #Importo l'immagine e ne calcolo l'aspect ratio
            self.originalImage = Image.open(newPath)
            self.aspectRatio = self.originalImage.size[0] / self.originalImage.size[1]

            #Riscalo l'immagine per non avere problemi di prestazioni 
            self.originalImage.resize((200,200)) 

            #Creo una variabile per contenere una copia dell'immagine riscalata e poter attingere 
            #ogni volta dall'immagine originale, così da non perdere qualità
            self.resizedImage = Image.open(newPath)
            self.imageTk = ImageTk.PhotoImage(self.originalImage)

            #Creo l'istanza così da poterla cancellare nel prossimo update
            self.imgThisFrameIstance = self.parentCanvas.create_image(self.canvasWidth/2, self.canvasHeight/2, image = self.immagineTKridimensionamentoAttuale, anchor = "center")
        except: 
            LOG.log("È stata rilevata una path non valida: " + str(newPath), 2)

    def ResizeEvent(self, event):
        self.Resize(event.width, event.height)

    def SetZoomIstantaneo(self, zoomIstantaneo : float):
        self.zoomIstantaneo = zoomIstantaneo
