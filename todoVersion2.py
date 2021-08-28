from tkinter import ttk 
from datetime import date
from tkinter import simpledialog
from tkinter.constants import BOTTOM, LEFT, RIGHT, TOP
from ttkthemes import ThemedTk


class singleplate:
    
    def __init__(self,gui):
        self.frame = ttk.Frame(gui,width=250, height=450)
        self.frame.pack_propagate(0)
        self.frame.pack()

    def deleteframe(self,s,text):
        s.destroy()
        
    def createFrame(self,text): 
        s = ttk.Frame(self.frame)  
        banner = ttk.Label(s,text=text)
        banner.pack(side=LEFT,fill="both")
        button = ttk.Button(s, text ="Delete", command = lambda:self.deleteframe(s,text))
        button.pack(side=RIGHT)
        s.pack(padx=5,pady=5)
        
class WindowFrame:
   
    def __init__(self,gui):
        gui.configure()
        gui.title("To do Application")
        gui.geometry("250x500")
        label = ttk.Label(gui,text="To Do's of {}".format(date.today()),anchor='w')
        label.pack(side=TOP)
       
if __name__ == "__main__" :
 
    gui = ThemedTk(theme="equilux") 
    root = WindowFrame(gui)
    gui.pack_propagate(0)
    f =   singleplate(gui)
    def addfunction():
        answer = simpledialog.askstring("Task", "Add task",parent=gui)
        print(answer)
        if answer!="" and answer != None:
            f.createFrame(answer) 

    button = ttk.Button(gui, text ="Add", command =addfunction)
    button.pack(side=BOTTOM)
      
    gui.mainloop()
   
