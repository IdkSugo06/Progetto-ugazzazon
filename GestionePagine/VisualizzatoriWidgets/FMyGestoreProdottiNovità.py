from GestionePagine.MyWidgets.FMyProdottoNovità import * 

#Si occuperà della gestione degli update, velocità, attriti... lo zoom sarà gestito dal prodottoNovita
class GestoreProdottiNovita:
    ZOOM_ESTREMO_FINESTRA = -0.4 #Zoom imposto dalla posizione della finestra (istantaneo)
    ATTRITO_SCORRIMENTO = 3.7 #Zoom imposto l'attrito durante lo scorrimento

    def __init__(self,
                 master : tk.Frame, 
                 numeroProdotti : int, 
                 centerx : int,
                 centery : int,
                 height : int, 
                 width : int,
                 padx : int = 30,
                 limitiBordo = True
                 ):
        
        if numeroProdotti == 0:
            LOG.IPrint("Gestore prodottiNovita inizializzato con 0 elementi", LOG_ERROR)
            return
        
        if numeroProdotti < 6:
            limitiBordo = False

        #Salvo i parametri passati
        self.__heightProdottoNovita = height
        self.__widthProdottoNovita = width
        self.__padxProdottoNovita = padx
        self.__centroIniziale = [centerx, centery]
        self.__numeroProdotti = numeroProdotti
        self.__limitiBordo = limitiBordo

        # SUPPORTO POSIZIONE PRODOTTI
        #Calcolo la lunghezza di tutti i prodotti affiancati 
        self.__lunghezzaTotaleProdottiNovita = numeroProdotti * width + (numeroProdotti + 1) * padx #+1 perche considero dello spazio agli estremi dei widget
        
        # ISTANZIO I PRODOTTI
        #Creo i prodottiNovita
        self.__prodottiNovita = [ProdottoNovita(master, int(centerx - (self.__lunghezzaTotaleProdottiNovita/2) + padx * (i+1) + width * (i+0.5)),
                                                centery, height, width, i) for i in range(numeroProdotti)] 
        
        # SUPPORTO VELOCITA
        self.__cronometro = Chrono() #Istanzio un oggetto cronometro in modo da calcolare la velocità impressa quando si muovono i widget
        self.__posizioneMouseB1Premuto = [0,0]
        self.__mousePremuto = False
        #Creo una variabile per controllare se si è scorso troppo, in modo da evitare che tutti i widget escano dallo schermo e rimanga bianco
        self.centroRelativo = 0 #In pixel
        self.velocitaCentroRelativo = 0 #In pixel/s

        #Lego gli eventi per rilevare i trascinamenti
        #Per evitare di rilevare gli stessi eventi piu volte, ne lego alcuni solo al primo prodottoNovita (id = 0)
        for i in range(numeroProdotti):
            self.__prodottiNovita[i].myBind("<Button-1>", self.MousePremutoB1)
            self.__prodottiNovita[i].myBind("<ButtonRelease-1>", self.MouseRilasciatoB1)

    # METODI 
    def UpdatePhysics(self, deltaTime : float):

        # UPDATE OGNI PRODOTTO
        #Eseguo l'update per ogni prodotto
        larghezzaFinestra = GestoreVariabiliGlobali.IGetDimensioniFinestra()[0]
        for i in range(self.__numeroProdotti):
            #Calcolo la distanza dall'estremo del widget e imposto lo zoom per dare l'effetto dell'arco desiderato
            distanzaEstremoFinestra = (self.__prodottiNovita[i].GetPos()[0] - larghezzaFinestra/2)
            sigma = larghezzaFinestra/2
            coeff = exp(-(distanzaEstremoFinestra/sigma)**2) #Uso una distribuzione normale in quanto il limite all'infinito tende a 0
            self.__prodottiNovita[i].SetZoomIstantaneo(1 + GestoreProdottiNovita.ZOOM_ESTREMO_FINESTRA * (1-coeff))

            #Eseguo l'update di ogni prodotto
            self.__prodottiNovita[i].UpdatePhysics(deltaTime)
            self.__prodottiNovita[i].MultVelocita(1 - GestoreProdottiNovita.ATTRITO_SCORRIMENTO * deltaTime)

        # SEGUI CURSORE SE MOUSE PREMUTO
        #Se il mouse è premuto, ogni update sposto i widget della distanza percorsa dal mouse
        if self.__mousePremuto == True:
            distanzaMousePercorsa = GestoreVariabiliGlobali.IGetDeltaMousePos()
            #Aggiungo il deltaMousePos e setto velocita a 0
            self.centroRelativo += distanzaMousePercorsa[0]
            self.velocitaCentroRelativo = 0
            for i in range(self.__numeroProdotti):
                self.__prodottiNovita[i].AddPos(distanzaMousePercorsa[0], 0)
                self.__prodottiNovita[i].SetVelocita(0,0)

        # CONTROLLO MARGINI
        #Controllo che i widget siano ancora nello schermo
        self.centroRelativo += self.velocitaCentroRelativo * deltaTime
        self.velocitaCentroRelativo *=  1 - (GestoreProdottiNovita.ATTRITO_SCORRIMENTO * deltaTime)
        distanzaOltreLimite = abs(self.centroRelativo - self.__widthProdottoNovita/2 - self.__padxProdottoNovita) + GestoreVariabiliGlobali.IGetDimensioniFinestra()[0]/2 - self.__lunghezzaTotaleProdottiNovita/2
        #Se la il rapporto tra abs(centroRelativo) e lunghezzaTotaleProdotti è maggiore di uno significa
        #che l'utente ha scorso troppo, quindi riaggiusto imprimento un cambio di posizione relativa alla distanza
        #dal punto massimo
        
        if distanzaOltreLimite > 0 and self.__limitiBordo:
            #Calcolo la distanza moltiplicando la direzione ad un coefficente dipendente dalla distanzaOltreLimite
            direzione = 0
            if self.centroRelativo > 0: direzione = -1
            elif self.centroRelativo < 0: direzione = 1
            coeff = direzione * ((distanzaOltreLimite/10)**2) * deltaTime + direzione * distanzaOltreLimite*2 * deltaTime

            #Aggiorno le posizioni
            self.centroRelativo += coeff
            for i in range(self.__numeroProdotti):
                self.__prodottiNovita[i].AddPos(coeff, 0)

    def UpdateGraphics(self):
        for i in range(self.__numeroProdotti):
            self.__prodottiNovita[i].UpdateGraphics()

    def AggiornaArticoliConsigliati(self):
        return
    
    #Salva le coordinate del mouse l'ultima volta premuto
    def MousePremutoB1(self, event): #Tutti prodotti chiameranno questo metodo in quanto l'evento viene chiamato solo quando si preme sul widget
        #Setto il flag a true
        self.__mousePremuto = True
        self.__posizioneMouseB1Premuto = GestoreVariabiliGlobali.IGetMousePosFrameCorrente()
        self.__cronometro.SetCheckpoint()
    #Calcola la velocità impressa dal trascinamento
    def MouseRilasciatoB1(self, event):  #Solo il prodotto novita con id 0 chiamerà questo metodo
        #Setto il flag a falso
        self.__mousePremuto = False
        #Calcola la velocita
        deltaTime = self.__cronometro.GetTimeFromCheckpoint()
        posMouseRilasciato = GestoreVariabiliGlobali.IGetMousePosFrameCorrente()
        velocita = [(posMouseRilasciato[0] - self.__posizioneMouseB1Premuto[0]) / deltaTime,
                    (posMouseRilasciato[1] - self.__posizioneMouseB1Premuto[1]) / deltaTime]
        #Setta la velocita per ogni prodotto
        self.velocitaCentroRelativo = velocita[0]
        for i in range(self.__numeroProdotti):
            self.__prodottiNovita[i].SetVelocita(velocita[0], 0)

    # BIND EVENTI
    def myBind(self, evento : str, function):
        for i in range(self.__numeroProdotti):
            self.__prodottiNovita[i].myBind(evento, function)