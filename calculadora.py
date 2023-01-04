from tkinter import *
from tkinter import ttk


# Cores
cor1 = "#3b3b3b" # Preta
cor2 = "#ffffff" # Branca
cor3 = "#38576b"  # Azul
cor4 = "#ECEFF1" # Cinza
cor5 = "#FFAB40" # Laranja


# Criando a janela da calculadora
janela = Tk()
janela.title('Calculadora')
janela.geometry("236x310")
janela.config(bg=cor1)


# Criando frames
frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1, column=0)


#variael e todos os valores
todos_valores = ''

valor_texto = StringVar()


# Criando a Função
def entrar_valores(event):
    global todos_valores

    todos_valores = todos_valores + str(event)

    # Passando o valor para a tela
    valor_texto.set(todos_valores)

# Função para calcular
def calcular():
    global todos_valores

    resultado = eval(todos_valores)

    valor_texto.set(str(resultado))


# Função Limpar tela
def limpar_tela():
    global todos_valores

    todos_valores = ""

    valor_texto.set("")






# Criando a label
app_label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg=cor3, fg=cor2)
app_label.place(x=0, y=0)


#Criando os botões
clear = Button(frame_corpo, text="C", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=limpar_tela)
clear.place(x=0, y=0)

modulo = Button(frame_corpo, text="%", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: entrar_valores('%'))
modulo.place(x=118, y=0)

divisao = Button(frame_corpo, text="/", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: entrar_valores('/'))
divisao.place(x=177, y=0)

##
num_7 = Button(frame_corpo, text="7", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: entrar_valores('7'))
num_7.place(x=0, y=52)

num_8 = Button(frame_corpo, text="8", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: entrar_valores('8'))
num_8.place(x=59, y=52)

num_9 = Button(frame_corpo, text="9", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: entrar_valores('9'))
num_9.place(x=118, y=52)

mult = Button(frame_corpo, text="*", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: entrar_valores('*'))
mult.place(x=177, y=52)

##
num_4 = Button(frame_corpo, text="4", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: entrar_valores('4'))
num_4.place(x=0, y=104)

num_5 = Button(frame_corpo, text="5", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: entrar_valores('5'))
num_5.place(x=59, y=104)

num_6 = Button(frame_corpo, text="6", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: entrar_valores('6'))
num_6.place(x=118, y=104)

menos = Button(frame_corpo, text="-", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: entrar_valores('-'))
menos.place(x=177, y=104)

##
num_1 = Button(frame_corpo, text="1", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: entrar_valores('1'))
num_1.place(x=0, y=156)

num_2 = Button(frame_corpo, text="2", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: entrar_valores('2'))
num_2.place(x=59, y=156)

num_3 = Button(frame_corpo, text="3", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: entrar_valores('3'))
num_3.place(x=118, y=156)

mais = Button(frame_corpo, text="+", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: entrar_valores('+'))
mais.place(x=177, y=156)

##
num_0 = Button(frame_corpo, text="0", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: entrar_valores('0'))
num_0.place(x=0, y=208)

ponto = Button(frame_corpo, text=".", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=lambda: entrar_valores('.'))
ponto.place(x=118, y=208)

igual = Button(frame_corpo, text="=", width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE, command=calcular)
igual.place(x=177, y=208)



janela.mainloop()

