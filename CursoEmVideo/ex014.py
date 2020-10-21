from tkinter import *


def button_avancar():
    print("Tela 2")


def button_sair():
    exit()


janela = Tk()

janela.title("Menu Inciar")


bt1 = Button(janela, width=15, text="Avançar para tela 2", command=button_avancar)
bt1.place(x=700, y=450)
bt2 = Button(janela, width=15, text="Sair", command=button_sair)
bt2.place(x=760, y=450)

janela.geometry("1000x500+200+200")
janela.mainloop()
