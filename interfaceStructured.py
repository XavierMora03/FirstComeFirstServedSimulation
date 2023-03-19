
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


i = 100


def suma():
    global i
    i+=2
    canvas1.move(ufoImg,i,0)
    print('jajas',i)
width = 600
heigth = 400
canvasVertticalSeparation = 70
raiz = Tk()
raiz.geometry('600x400')
raiz.title('FCFS Algorithm')
btnCorrer = Button(raiz,text='Correr',command=lambda: suma())
btnCorrer.place(x=20, y=380)

btnReiniciar = Button(raiz, text='Reiniciar', command=lambda: suma())
btnReiniciar.place(x=150,y=380)
canvas1 = Canvas(raiz, width=width , height=60, bg="green")
canvas1.place(x=0,y=0)
canvas2 = Canvas(raiz, width=width , height=60, bg="cornsilk")
canvas2.place(x=0,y=1*canvasVertticalSeparation)
canvas3 = Canvas(raiz, width=width , height=60, bg="bisque")
canvas3.place(x=0,y=2*canvasVertticalSeparation)
canvas4 = Canvas(raiz, width=width , height=60, bg="CadetBlue1")
canvas4.place(x=0,y=3*canvasVertticalSeparation)
canvas5 = Canvas(raiz, width=width , height=60, bg="Coral")
canvas5.place(x=0,y=4*canvasVertticalSeparation)

ufoImgN = ImageTk.PhotoImage(Image.open("./ufor.png"))
ufoImg = canvas1.create_image(0,0,anchor=NW,image=ufoImgN)

ttk.Button(raiz, text='Salir', command=raiz.destroy).pack(side=BOTTOM)

raiz.mainloop();



