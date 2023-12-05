import tkinter as tk

def abrir_janela():
	janela2 = tk.Toplevel()
	janela2.title('janela nova')
	label_nome = tk.Label(janela2, text = "Nome")
	label_nome.grid(row = 0, column = 0 )
	botao_voltar = tk.Button(janela2, text = 'Fechar a janela2', command = janela2.destroy)
	botao_voltar.grid(row = 1, column = 0)

janela = tk.Tk()

botao = tk.Button(janela, text = 'Ir para nova janela', command = abrir_janela)
botao.grid(row = 0, column = 0)

janela.mainloop()
