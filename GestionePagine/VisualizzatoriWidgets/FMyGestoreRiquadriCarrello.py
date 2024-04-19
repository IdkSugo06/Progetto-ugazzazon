from GestionePagine.MyWidgets.FMyRiquadroProdottoCarrello import *

class GestoreRiquadriCarrello:

    def __init__(self, master : tk.Frame):
        
        #Creo la lista riquadri carrello, verrà popolata quando si aggiornerà il carrello
        self.master = master
        self.__listaRiquadriCarrello = []
        self.__fFrameRiquadriCarrello = []


        #Creo il FRAME PRINCIPALE
        self.__fFramePrinciple = tk.Frame(master=master)
        self.__fFrameParteCentrale.grid(row=0, column=0, sticky="nsew")
        self.__fFramePrinciple.columnconfigure(0,weight=1)
        self.__fFramePrinciple.columnconfigure(1,weight=15)
        self.__fFramePrinciple.rowconfigure(0,weight=1)
        self.__fFramePrinciple.rowconfigure(1,weight=3)
        self.__fFramePrinciple.rowconfigure(2,weight=1)
        self.__fFramePrinciple.grid_propagate(False)


        #Creo il FRAME CENTRALE
        self.__fFrameParteCentrale = tk.Frame(master=self.__fFramePrinciple)
        self.__fFrameParteCentrale.grid(row=1, column=1, sticky="nsew")
        self.__fFrameParteCentrale.columnconfigure(0,weight=1)
        self.__fFrameParteCentrale.rowconfigure(0,weight=1)
        self.__fFrameParteCentrale.grid_propagate(False)
        self.__fFrameParteCentrale.pack_propagate(False)


        #Creo la scritta AVVISO NESSUN PRODOTTO
        self.__lAvvisoNessunProdotto = tk.Label(master=self.__fFrameParteCentrale, text="Nessun prodotto nel carrello")
        self.__lAvvisoNessunProdotto.pack(side ="top", expand="x",fill ="nsew")

        

    def AggiornaCarrello(self, listaIdProdotti : list[int]):
        #Controllo che la lista non sia vuota
        self.__lAvvisoNessunProdotto.forget()
        if len(listaIdProdotti) == 0:
            self.__lAvvisoNessunProdotto.forget()


        #Popolo la lista di frame
        self.__listaRiquadriCarrello = []
        i = 0
        for idProdotto in listaIdProdotti:
            self.__listaRiquadriCarrello.append(RiquadroProdottoCarrello(self.master, idProdotto))
            self.__listaRiquadriCarrello[i].pack(side ="top", expand="x",fill ="nsew")
            i += 1
