from tkinter import *
from tkinter import messagebox

janela = Tk()
janela.title("Maluly")
janela.geometry('400x400')

def ola():

    messagebox.showinfo('O título da mensagem','conteúdo da mensagem')


btn = Button(janela,text='Clica aqui', command=ola)
btn.grid(column=0,row=0)

janela.mainloop()