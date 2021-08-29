from tkinter import ttk
from ttkthemes import ThemedTk
from tkinter.colorchooser import askcolor
from tkinter import *
class CardClass:
   
    def __init__(self,gui):
       self.textCard = ""
       self.cardFrame = ""
       self.frame = ttk.Frame(gui,width=250, height=450)
     
       self.frame.pack()
    
    def crateCard(self):
        self.cardFrame = ttk.Frame(self.frame)
        self.textCard = Text(self.cardFrame,bg="pink",wrap=WORD,relief=GROOVE,font=('Constantia', 12))
        self.textCard.pack()
        self.cardFrame.pack()
      
        
    def clearCard(self):
        self.textCard.delete(1.0,END)   
        
    def pickChangeColor(self):
        color = askcolor() 
        self.textCard.config(bg=color[1])
        
class MainWindow:
    def __init__(self,gui) :
        gui.configure()
        gui.title("Note")
        gui.geometry("250x500")
 
def application():
    gui = ThemedTk(theme="equilux") 
    root = MainWindow(gui)
    card = CardClass(gui)
    card.crateCard()
    buttonNewCard = ttk.Button(gui,text="New",command=application)
    buttonNewCard.pack(side=LEFT)
    buttonNewCard = ttk.Button(gui,text="clear",command=card.clearCard)
    buttonNewCard.pack(side=LEFT)
    buttonNewCard = ttk.Button(gui,text="Color",command=card.pickChangeColor)
    buttonNewCard.pack(side=RIGHT)
    gui.mainloop()    
if __name__ == "__main__" :
   application()       
        
    