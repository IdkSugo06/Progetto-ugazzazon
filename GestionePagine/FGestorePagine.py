from GestionePagine.Pagine.FPaginaGenerica import *

#Gestirà il caricamento pagina, conterra tutte le pagine, 
#la pagina corrente e l'istanza del widget finestra principale
class GestorePagine(): #Singleton

# ATTRIBUTI STATICI -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- ATTRIBUTI STATICI
    #Creo un istanza statica accessibile da tutti col metodo GetGestorePagine()
    __gestorePagine = None


# INTERFACCE -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- INTERFACCE
    @staticmethod
    def Init(): #Inizializzo l'istanza statica
        #Se l'istanza non è ancora stata creata, la creo
        if GestorePagine.__gestorePagine == None:
            GestorePagine.__gestorePagine = GestorePagine()

    @staticmethod
    def GetGestorePagine(): #Metodo per accedere all'istanza statica
        #Se l'istanza non è ancora stata creata, la creo
        if GestorePagine.__gestorePagine == None:
            GestorePagine.__gestorePagine = GestorePagine()
        #Ritorno l'istanza statica
        return GestorePagine.__gestorePagine
    
    @staticmethod 
    def IGetWindow(): #Chiamerà l'ononima funzione dell'istanza statica 
        return GestorePagine.GetGestorePagine().__GetWindow() 
    
    @staticmethod 
    def IGetFramePrincipale(): #Chiamerà l'ononima funzione dell'istanza statica 
        return GestorePagine.GetGestorePagine().__GetFramePrincipale() 
    
    @staticmethod
    def ICaricaPagina(idPagina : int): #Chiamerà l'ononima funzione dell'istanza statica 
        GestorePagine.GetGestorePagine().__CaricaPagina(idPagina)

    @staticmethod
    def IChiusuraFinestra(): #Chiamerà l'ononima funzione dell'istanza statica 
        GestorePagine.GetGestorePagine().__ChiusuraFinestra()
    
    @staticmethod
    def IUpdatePaginaCorrente(deltaTime : float): #Chiamerà l'ononima funzione dell'istanza statica 
        GestorePagine.GetGestorePagine().__UpdatePaginaCorrente(deltaTime)

    @staticmethod 
    def IAddPagina(paginaDaAggiungere : PaginaGenerica): #Chiamerà l'ononima funzione dell'istanza statica 
        GestorePagine.GetGestorePagine().__AddPagina(paginaDaAggiungere) 

    @staticmethod 
    def IMainLoop(): #Inizierà il loop di tkInter
        GestorePagine.GetGestorePagine().__window.mainloop()

    
# METODI -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- METODI
    # COSTRUTTORI
    def __init__(self): #Costruttore dovrebbe essere privato

        #Creo un istanza della finestra principale e setto qualche attributo
        self.__window = tk.Tk()
        self.__window.title('Ugazzazon')
        self.__window.geometry(str(LARGHEZZA_SCHERMO_INIZIALE) + "x" + str(ALTEZZA_SCHERMO_INIZIALE) + "+" + str(OFFSET_ORIZZONTALE_SCHERMO) + "+" + str(OFFSET_VERTICALE_SCHERMO))
        self.__window.minsize(MIN_LARGHEZZA_SCHERMO, MIN_ALTEZZA_SCHERMO)
        self.__window.maxsize(MAX_LARGHEZZA_SCHERMO, MAX_ALTEZZA_SCHERMO)
        #rimuovo la barra del titolo, ma anche il grip per ridimensionare la finestra, quindi lo aggiungo
        self.__window.overrideredirect(True) 
        self.__grip = ttk.Sizegrip(master = self.__window)
        self.__grip.place(relx = 0.9, rely = 0.9, anchor="se")
        #Creo due frame per dividere la finestra in frame principale e titlebar
        #Configuro righe e colonne della finestra per poter contenere i due frame
        self.__window.rowconfigure(0, weight=1)
        self.__window.rowconfigure(1, weight=39)
        self.__window.columnconfigure(0, weight=1)
        #Creo il titleBar
        self.__fTitleBar = tk.Frame(master = self.__window, bg = "#553096")
        self.__fTitleBar.grid(row = 0, column= 0, sticky = "nsew")
        self.__fTitleBar.columnconfigure(0,weight=1)
        self.__fTitleBar.columnconfigure(1,weight=32)
        self.__fTitleBar.columnconfigure(2,weight=1)
        self.__fTitleBar.columnconfigure(3,weight=1)
        self.__fTitleBar.columnconfigure(4,weight=1)
        self.__fTitleBar.rowconfigure(0,weight=1)
        self.__fTitleBar.grid_propagate(False)
        #Creo i widget per chiudere la finestra
        self.__bPulsanteChiusuraFinestra = tk.Button(master = self.__fTitleBar, text = "x", command=self.__ChiusuraFinestra)
        self.__bPulsanteChiusuraFinestra.grid(row = 0, column= 4, sticky="nsew")
        #Creo il frame principale
        self.__fFramePrincipale = ttk.Frame(master = self.__window)
        self.__fFramePrincipale.grid(row = 1, column= 0, sticky = "nsew")
        self.__fFramePrincipale.columnconfigure(0,weight=1)
        self.__fFramePrincipale.rowconfigure(0,weight=1)
        self.__fFramePrincipale.grid_propagate(False)

        #Salvo una referenza alle istanze delle pagine (singleton) così da poterle utilizzare quando necessario
        self.__idPaginaCaricataAttualmente = 0 #id posizionale della pagina caricata attualmente
        self.__pagine = [] #La lista sarà popolata durante la definizione delle classi Pagina (per problemi di accesso ai file)
    
    # GETTER    
    def __GetWindow(self):
        #Ritorno l'istanza della finestra (Tk)
        return self.__window
    
    def __GetFramePrincipale(self):
        #Ritorno l'istanza della frame principale (Tk)
        return self.__fFramePrincipale
    
    # ADDER
    def __AddPagina(self, paginaDaAggiungere : PaginaGenerica):
        #Aggiungo la pagina alla lista di pagine
        self.__pagine.append(paginaDaAggiungere) 
        
    # METODI GENERALI
    def __CaricaPagina(self, idPagina : int):
        #Chiudo la pagina precedente e carico la nuova
        self.__pagine[self.__idPaginaCaricataAttualmente].NascondiPagina() 
        self.__pagine[idPagina].CaricaPagina() 
        self.__idPaginaCaricataAttualmente = idPagina

    def __UpdatePaginaCorrente(self, deltaTime : float): #Chiamerà l'ononima funzione dell'istanza statica 
        self.__pagine[self.__idPaginaCaricataAttualmente].UpdatePagina(deltaTime)
        GestoreVariabiliGlobali.IUpdateMousePos(self.__window.winfo_pointerx(), self.__window.winfo_pointery())

    def __ChiusuraFinestra(self):
        GestoreVariabiliGlobali.ISetRunning(False)
        self.__window.destroy()

#Inizializzo il gestore pagina
GestorePagine.Init()

    

        
    