from GestionePagine.MyWidgets.FMyImage import *

class MyImageButton(MyImageTK):
    
    def __init__(self, canvas : tk.Canvas, command, path = ""):
        super().__init__(canvas, path)
        self.parentCanvas.bind("<ButtonRelease-1 >", command)

    

