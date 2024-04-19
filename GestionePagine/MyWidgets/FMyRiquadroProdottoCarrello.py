from GestionePagine.MyWidgets.FMyImageButton import *
from GestioneProdotti.FMagazzino import *

class RiquadroProdottoCarrello(tk.Frame):
    
    def __init__(self, master : tk.Frame, idProdotto : int):
        #Chiamo il costtruttore del padre
        super().__init__(master = master)

        #Salvo l'id del prodotto
        self.idProdotto = idProdotto

        #Configuro il frame principale
        self.columnconfigure(0,weight=2)
        self.columnconfigure(1,weight=3)
        self.rowconfigure(0,weight=1)
        self.grid_propagate(False)


        # IMMAGINE
        #Frame di supporrto
        self.__fFrameSupportoImmagine = tk.Frame(master = self)
        self.__fFrameSupportoImmagine.grid(row = 0, column=0, sticky="nsew")
        self.__fFrameSupportoImmagine.columnconfigure(0,weight=1)
        self.__fFrameSupportoImmagine.rowconfigure(0,weight=1)
        self.__fFrameSupportoImmagine.grid_propagate(False)
        #Canvas per contenere l'immagine
        self.__cCanvasImmagine = tk.Canvas(master = self)
        self.__cCanvasImmagine.grid(row = 0, column=0, sticky="nsew")
        #Immagine
        self.__myImgImmagineProdotto = MyImageTK(self.__cCanvasImmagine, IMMAGINE_DEFAULT_ANTEPRIMA)
        self.__myImgImmagineProdotto.Resize(((1/10) * GestoreVariabiliGlobali.IGetDimensioniFinestra()[0]),
                                            ((1/10) * GestoreVariabiliGlobali.IGetDimensioniFinestra()[0]))   
        self.__myImgImmagineProdotto.Show()


        #Creo il frame di SUPPORTO PARTE DESTRA
        self.__fFrameParteDestra = tk.Frame(master = self)
        self.__fFrameParteDestra.grid(row = 0, column=1,sticky="nsew")
        self.__fFrameParteDestra.columnconfigure(0,weight=2)
        self.__fFrameParteDestra.columnconfigure(1,weight=1)
        self.__fFrameParteDestra.columnconfigure(2,weight=1)
        self.__fFrameParteDestra.columnconfigure(3,weight=1)
        self.__fFrameParteDestra.columnconfigure(4,weight=1)
        self.__fFrameParteDestra.rowconfigure(0,weight=8)
        self.__fFrameParteDestra.rowconfigure(1,weight=4)
        self.__fFrameParteDestra.rowconfigure(2,weight=1)
        self.__fFrameParteDestra.rowconfigure(3,weight=3)
        self.__fFrameParteDestra.grid_propagate(False)


        #Frame supporto NOME PRODOTTO
        self.__fFrameNomeProdotto = tk.Frame(master = self.__fFrameParteDestra)
        self.__fFrameNomeProdotto.grid(row = 0, column=0, columnspan=4, sticky="nsew")
        self.__fFrameNomeProdotto.columnconfigure(0,weight=1)
        self.__fFrameNomeProdotto.rowconfigure(0,weight=1)
        self.__fFrameNomeProdotto.grid_propagate(False)
        #Label nome prodotto
        self.__lNomeProdotto_str = tk.StringVar()
        self.__lNomeProdotto_str.set("Ops, qualcosa è andato storto")
        self.__lNomeProdotto = tk.Label(master = self, textvariable=self.__lNomeProdotto_str)
        self.__lNomeProdotto.grid(row = 0, column=0,sticky="nsew")


        #Frame TIPO PRODOTTO
        self.__fFrameTipoProdotto = tk.Frame(master = self.__fFrameParteDestra)
        self.__fFrameTipoProdotto.grid(row = 1, column=0, columnspan=3, sticky="nsew")
        self.__fFrameTipoProdotto.columnconfigure(0,weight=1)
        self.__fFrameTipoProdotto.rowconfigure(0,weight=1)
        self.__fFrameTipoProdotto.grid_propagate(False)
        #Label tipo prodotto
        self.__lTipoProdotto_str = tk.StringVar()
        self.__lTipoProdotto_str.set("Ops, qualcosa è andato storto")
        self.__lTipoProdotto = tk.Label(master = self, textvariable=self.__lTipoProdotto_str)
        self.__lTipoProdotto.grid(row = 0, column=0,sticky="nsew")


        #Frame QUANTITA PRODOTTO
        self.__fFrameQuantitaProdotto = tk.Frame(master = self.__fFrameParteDestra)
        self.__fFrameQuantitaProdotto.grid(row = 3, column=0, columnspan=0, sticky="nsew")
        self.__fFrameQuantitaProdotto.columnconfigure(0,weight=1)
        self.__fFrameQuantitaProdotto.rowconfigure(0,weight=1)
        self.__fFrameQuantitaProdotto.grid_propagate(False)
        #Label quantita prodotto
        self.__fFrameQuantitaProdotto_str = tk.StringVar()
        self.__fFrameQuantitaProdotto_str.set("0")
        self.__lQuantitaProdotto = tk.Label(master = self, textvariable=self.__fFrameQuantitaProdotto_str)
        self.__lQuantitaProdotto.grid(row = 0, column=0,sticky="nsew")


        #Frame PREZZO PRODOTTO
        self.__fFramePrezzoProdotto = tk.Frame(master = self.__fFrameParteDestra)
        self.__fFramePrezzoProdotto.grid(row = 3, column=3, columnspan=2, sticky="nsew")
        self.__fFramePrezzoProdotto.columnconfigure(0,weight=1)
        self.__fFramePrezzoProdotto.rowconfigure(0,weight=1)
        self.__fFramePrezzoProdotto.grid_propagate(False)
        #Label prezzo prodotto
        self.__fFramePrezzoProdotto_str = tk.StringVar()
        self.__fFramePrezzoProdotto_str.set("0")
        self.__lPrezzoProdotto = tk.Label(master = self, textvariable=self.__fFramePrezzoProdotto_str)
        self.__lPrezzoProdotto.grid(row = 0, column=0,sticky="nsew")


    def AssociaProdotto(self, idProdotto : int, quantita : int):
        #Cerco il prodotto nel magazzino
        tempProdotto = Magazzino.GetProdotto(idProdotto)
        self.idProdotto = idProdotto

        #Se il prodotto è valido lo carico
        if idProdotto != -1:
            #Setto gli attributi
            self.__lNomeProdotto_str.set(tempProdotto.GetNome())
            self.__lTipoProdotto_str.set(tempProdotto.GetTipo())
            self.__lPrezzoProdotto_str.set(str(tempProdotto.GetPrezzo()) + "€")
            self.__lQuantitaProdotto.set(str(quantita))

            #Setto limmagine
            self.__myImgImmagineProdotto.ChangeImage(tempProdotto.GetPathImmagine())
            self.__myImgImmagineProdotto.Resize(((1/10) * GestoreVariabiliGlobali.IGetDimensioniFinestra()[0]),
                                            ((1/10) * GestoreVariabiliGlobali.IGetDimensioniFinestra()[0]))   
            self.__myImgImmagineProdotto.Show()
            return 
        
        #Altrimenti carico le informazioni default
        self.__lNomeProdotto_str.set("Ops, qualcosa è andato storto")
        self.__lTipoProdotto_str.set("Ops, qualcosa è andato storto")
        self.__lPrezzoProdotto_str.set("0€")
        self.__lQuantitaProdotto.set("0")
        self.__myImgImmagineProdotto.ChangeImage(IMMAGINE_DEFAULT_ANTEPRIMA)
        self.__myImgImmagineProdotto.Resize(((1/10) * GestoreVariabiliGlobali.IGetDimensioniFinestra()[0]),
                                            ((1/10) * GestoreVariabiliGlobali.IGetDimensioniFinestra()[0]))   
        self.__myImgImmagineProdotto.Show()
