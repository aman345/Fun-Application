from tkinter import *
from datetime import date
from tkinter import simpledialog

class singleplate:
    
    def __init__(self,gui,):
        self.frame = Frame(gui,width=400, height=200, background="bisque")
        self.frame.pack()

    def deleteframe(self,s,text):
        s.destroy()
        
    def createFrame(self,text): 
        s = Frame(self.frame,width=200, height=100, background="bisque")  
        banner = Label(s,text=text)
        banner.pack(side=LEFT,fill="both")
        button = Button(s, text ="Delete", command = lambda:self.deleteframe(s,text))
        button.pack(side=RIGHT)
        s.pack(padx=5,pady=5)
        
class WindowFrame:
   
    def __init__(self,gui):
        gui.configure(background = "light green")
        gui.title("To do Application")
        gui.geometry("250x300")
        label = Label(gui,text="To Do's of {}".format(date.today()),anchor='w')
        label.pack(side=TOP)
       
if __name__ == "__main__" :
 
    gui = Tk() 
    root = WindowFrame(gui)
    f =   singleplate(gui)
    def addfunction():
        answer = simpledialog.askstring("Task", "Add task",parent=gui)
        print(answer)
        if answer!="" and answer != None:
            f.createFrame(answer) 

    button = Button(gui, text ="Add", command =addfunction)
    button.pack(side=BOTTOM)
      
    gui.mainloop()
   
