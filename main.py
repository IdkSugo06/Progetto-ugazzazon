from GestionePagine.Pagine.FPagine import *
from threading import *

running = True
def Update():
    lastTime = time.time()
    while GestoreVariabiliGlobali.IGetRunning():

        if MyEventHandler.CheckFatalErrorOccurred():
            Quit()
            return 
        
        currentTime = time.time()
        GestorePagine.IUpdatePaginaCorrente(currentTime - lastTime)
        lastTime = currentTime
        
def Start():
    t = Thread(target=Update)
    t.start()
    GestorePagine.ICaricaPagina(PaginaGenerica.GetIdPagina("accesso"))
    GestorePagine.IMainLoop()
    t.join()

def Quit(tkInterEvent = None):
    GestorePagine.IGetWindow().destroy()
    GestoreVariabiliGlobali.ISetRunning(False)
    
GestorePagine.IGetWindow().bind("<Escape>", Quit)
Start() 