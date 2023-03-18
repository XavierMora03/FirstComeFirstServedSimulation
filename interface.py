
from tkinter import *
from tkinter import ttk


class Aplicacion():

    def __init__(self):
     raiz = Tk()
     raiz.geometry('600x400')
     raiz.title('FCFS Algorithm')

     ttk.Button(raiz,text='Salir',command=quit).pack(side=BOTTOM)

     raiz.mainloop();
