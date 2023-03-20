
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from time import sleep
from random import randint

MAX_UFO_RECORRIDO = 32

class Aplicacion():
    def __init__(self):
     self.i = [0,0,0,0,0]
     width = 600
     canvasVertticalSeparation = 70
     self.raiz = Tk()
     self.raiz.geometry('600x400')
     self.raiz.title('FCFS Algorithm')     

     self.canvas = []
     self.canvas.append( Canvas(self.raiz, width=width , height=60, bg="green"))
     self.canvas[0].place(x=0,y=0)
     self.canvas.append(Canvas(self.raiz, width=width , height=60, bg="cornsilk"))
     self.canvas[1].place(x=0,y=1*canvasVertticalSeparation)
     self.canvas.append(Canvas(self.raiz, width=width , height=60, bg="bisque"))
     self.canvas[2].place(x=0,y=2*canvasVertticalSeparation)
     self.canvas.append(Canvas(self.raiz, width=width , height=60, bg="CadetBlue1"))
     self.canvas[3].place(x=0,y=3*canvasVertticalSeparation)
     self.canvas.append(Canvas(self.raiz, width=width , height=60, bg="Coral"))
     self.canvas[4].place(x=0,y=4*canvasVertticalSeparation)

     self.ufoImgOBJ = PhotoImage(file='./ufor.png')
     # self.ufoImg = self.canvas1.create_image(0,0,anchor=NW,image=self.ufoImgOBJ)
     self.ufoImg = []

     self.ufoImg.append(self.canvas[0].create_image(0,0,anchor=NW,image=self.ufoImgOBJ))
     self.ufoImg.append(self.canvas[1].create_image(0,0,anchor=NW,image=self.ufoImgOBJ))
     self.ufoImg.append(self.canvas[2].create_image(0,0,anchor=NW,image=self.ufoImgOBJ))
     self.ufoImg.append(self.canvas[3].create_image(0,0,anchor=NW,image=self.ufoImgOBJ))
     self.ufoImg.append(self.canvas[4].create_image(0,0,anchor=NW,image=self.ufoImgOBJ))

     self.btnReiniciar = Button(self.raiz, text='Reiniciar', command=self.reiniciar)
     self.btnReiniciar.place(x=150,y=380)

     ttk.Button(self.raiz, text='Salir', command=self.raiz.destroy).pack(side=BOTTOM)

     processQueue = [[self.canvas[0],0,110],[self.canvas[1],1,200],[self.canvas[2],2,90],[self.canvas[3],3,20],[self.canvas[4],4,100]]


     self.btnCorrer = Button(self.raiz,text='Correr',command= lambda:self.firstComeFirstServed(processQueue,0))
     self.btnCorrer.place(x=20, y=380)


     self.raiz.mainloop();

    def avanza(self,canvas,index,delay):
            if(self.i[index] < MAX_UFO_RECORRIDO):
                self.i[index]+=1
                self.canvas[index].move(self.ufoImg[index],self.i[index],0)
                canvas.after(delay,lambda: self.avanza(canvas,index,delay))
                return 0
            print(self.i[index])


    def firstComeFirstServed(self,queue,delayAnterior):
        self.avanza(queue[0][0],queue[0][1],queue[0][2])
        delayRecorrido  = MAX_UFO_RECORRIDO*queue[0][2] 
        if(len(queue)>1):
            queue.pop(0)
            self.raiz.after(delayRecorrido,lambda:self.firstComeFirstServed(queue,delayRecorrido))


    def reiniciar(self):
        for i in range(5):
            self.i[i] = 0
            self.canvas[i].move(self.ufoImg[i],0,0)

Aplicacion()
