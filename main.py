from GestionePagine.Pagine.FPagine import *
from threading import *

running = True
def Update():
    lastTime = time.time()
    while GestoreVariabiliGlobali.IGetRunning():
        currentTime = time.time()
        GestorePagine.IUpdatePaginaCorrente(currentTime - lastTime)
        lastTime = currentTime
        time.sleep(0.001)
        
def Start():
    t = Thread(target=Update)
    t.start()
    GestorePagine.ICaricaPagina(PaginaGenerica.GetIdPagina("accesso"))
    GestorePagine.IMainLoop()
    t.join()

def Quit(event):
    GestorePagine.IGetWindow().destroy()
    GestoreVariabiliGlobali.ISetRunning(False)
    
GestorePagine.IGetWindow().bind("<Escape>", Quit)
Start() 