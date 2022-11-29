import simplex as sp
import big_m as bm
#import grafico as gr
import definir_modelo as dm
import tkinter as tk
from PIL import Image, ImageTk
from tkinter.simpledialog import askinteger, askstring
import os
from math import inf 
infinito = float("inf")


#https://www.youtube.com/watch?v=itRLRfuL_PQ - moça
#https://www.youtube.com/watch?v=VMP1oQOxfM0 - indiano

master = tk.Tk()
master.title("Programação Linear - Passo a passo")
canvas = tk.Canvas(master, width=600,height=300)
canvas.grid(columnspan=3, rowspan=5)

#logo = Image.open('sign.png')
#logo = ImageTk.PhotoImage(logo)
#logo_label = tk.Label(image=logo)
#logo_label.image = logo
#logo_label.grid(column=1, row=1)

#instructions
instructions = tk.Label(master, text = 'Selecione o que você deseja fazer', font='Raleway')
instructions.grid(columnspan=3, column=0, row=0)

#browse_text = tk.StringVar()
#browse_text.set('É ISSO QUE VOÇÊ QUER???')

def exec_simplex():
    window_simplex = tk.Tk()

    def display_text():
        #global entry
        #insert= entry.get()
        #result = user_inp.configure(text=insert)
        lista_nova = []
        
        n_rows = askinteger(title = "Número de linhas", prompt ="Insira o n° de linhas do tabuleiro")
        n_cols = askinteger(title = "Número de colunas", prompt ="Insira o n° de colunas do tabuleiro")
        user_inp = askstring(title="Simplex padrão", prompt="Insira a matriz do 1° tabuleiro")

        convert = [float(s) for s in user_inp.split(',')]
        def insert_elements(begin, end, lista_from):
            lista = []
            for x in range(begin, end):
                lista.append(lista_from[x])

            return lista

        lista = []
        c = 0
        r = 1
        n = n_cols
        while r <= n_rows:
            lista_nova = insert_elements(c, n, convert)
            lista.append(lista_nova)
            r+=1
            c = n
            n+=n_cols

        output = sp.simplex(lista)
        tk.messagebox.showinfo("Resultado Simplex padrão", output).window_simplex = tk.Tk()     
    
    entry = tk.Entry(window_simplex, width = 40)
    entry.focus_set()
    entry.pack()
    tk.Button(window_simplex, text= "Okay",width= 20, command= display_text).pack(pady=20)
    
    #var = tk.DoubleVar(window_simplex, value=output)
    #tk.Radiobutton(window_simplex, variable=var, value=output, text="r1").pack()
    
    #tk.Button(window_simplex, text="print", command=sp.simplex()).pack()

    #tkinter_variable.get()
    window_simplex.mainloop()


browse_btn = tk.Button(master, text='Simplex padrão', command= lambda:exec_simplex(), font = 'Raleway', bg="#10bebe", fg='white', height=2, width=15)
browse_btn.grid(column=0, row=2)

canvas = tk.Canvas(master, width=600,height=250)
canvas.grid(columnspan=3)
  

def exec_grafico():
    pass


def exec_modelo():
    window_modelo = tk.Tk()

    dm.definirmodelo()

    window_modelo.mainloop()

browse_btn2 = tk.Button(master, text='Montar modelo', command= lambda:exec_modelo(), font = 'Raleway', bg="#15bebe", fg='white', height=2, width=15)
browse_btn2.grid(column=1, row=1)

#canvas = tk.Canvas(master, width=600,height=250)
#canvas.grid(columnspan=3)

def bigm():
    window_bigm = tk.Tk()

    def display_text():
        #global entry
        #insert= entry.get()
        #result = user_inp.configure(text=insert)
        lista_nova = []
        
        n_rows = askinteger(title = "Número de linhas", prompt ="Insira o n° de linhas do tabuleiro")
        n_cols = askinteger(title = "Número de colunas", prompt ="Insira o n° de colunas do tabuleiro")
        n_auxiliares = askinteger(title = "Número de auxiliares", prompt ="Insira o n° de auxiliares")
        user_inp = askstring(title="BIGM", prompt="Insira a matriz do 1° tabuleiro")

        convert = [float(s) for s in user_inp.split(',')]
        def insert_elements(begin, end, lista_from):
            lista = []
            for x in range(begin, end):
                lista.append(lista_from[x])

            return lista

        lista = []
        c = 0
        r = 1
        n = n_cols
        while r <= n_rows:
            lista_nova = insert_elements(c, n, convert)
            lista.append(lista_nova)
            r+=1
            c = n
            n+=n_cols

        output = bm.simplex(lista, n_auxiliares)
        tk.messagebox.showinfo("Resultado Simplex padrão", output).window_bigm = tk.Tk()     
    
    entry = tk.Entry(window_bigm, width = 40)
    entry.focus_set()
    entry.pack()
    tk.Button(window_bigm, text= "Okay",width= 20, command= display_text).pack(pady=20)

    window_bigm.mainloop()

browse_btn3 = tk.Button(master, text='Big M', command= lambda:bigm(), font = 'Raleway', bg="#15bebe", fg='white', height=2, width=15)
browse_btn3.grid(column=1, row=2)

def min():
    pass

browse_btn4 = tk.Button(master, text='Minimização', command= lambda:min(), font = 'Raleway', bg="#15bebe", fg='white', height=2, width=15)
browse_btn4.grid(column=2, row=2)

def openfile():
    #return doc.docx
    #os.system("./doc.docx")
    pass

button = tk.Button(master, text="Ajuda", command=openfile)  
button.grid(column=1, row=5)

def sair():
    master.destroy()

sair = tk.Button(master, text="Fechar", command=sair)
sair.grid(column=2, row=5)

master.mainloop()