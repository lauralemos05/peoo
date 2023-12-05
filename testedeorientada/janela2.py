from tkinter import *

janela = Tk()
label = Label(janela, text='Menu Principal')
label.pack()


def criar_usuario():
    global janela
    janela.destroy()
    janela = Tk() 
    label = Label(janela, text='Criar Usuario')
    label.pack()
    janela.geometry("600x600+250+50")
    menu_bt = Button(janela, text='Voltar/Menur',command=menu)
    menu_bt.pack()


def editar_usuario():
    global janela
    janela.destroy()
    janela = Tk() 
    label = Label(janela, text='Editar Usuario')
    label.pack()
    janela.geometry("600x600+250+50")
    menu_bt = Button(janela, text='Voltar/Menur',command=menu)
    menu_bt.pack()


def menu():
    global janela
    janela.destroy()
    janela = Tk()

    label = Label(janela, text='Menu Principal')
    label.pack()

    menu_bt_criar = Button(janela, text='Criar Usuario',command=criar_usuario)
    menu_bt_edituser = Button(janela, text='Editar Usuario',command=editar_usuario)

    menu_bt_criar.place(x=30,y=100)
    menu_bt_edituser.place(x=30,y=130)

    janela.geometry("600x600+250+50")
    janela.title("Menu Principal")

    janela.mainloop()


menu_bt_criar = Button(janela, text='Criar Usuario',command=criar_usuario)
menu_bt_edituser = Button(janela, text='Editar Usuario',command=editar_usuario)

menu_bt_criar.place(x=30,y=100)
menu_bt_edituser.place(x=30,y=130)

janela.geometry("600x600+250+50")
janela.title("Menu Principal")

janela.mainloop()