import simplex as sp
#import grafico as gr
import definir_modelo as dm
import tkinter as tk
from PIL import Image, ImageTk
from tkinter.simpledialog import askinteger, askstring


#https://www.youtube.com/watch?v=itRLRfuL_PQ - moça
#https://www.youtube.com/watch?v=VMP1oQOxfM0 - indiano

master = tk.Tk()
master.title("Programação Linear - Passo a passo")
canvas = tk.Canvas(master, width=600,height=300)
canvas.grid(columnspan=3, rowspan=3)

#logo = Image.open('sign.png')
#logo = ImageTk.PhotoImage(logo)
#logo_label = tk.Label(image=logo)
#logo_label.image = logo
#logo_label.grid(column=1, row=0)

#instructions
instructions = tk.Label(master, text = 'Selcione o que você deseja fazer', font='Raleway')
instructions.grid(columnspan=3, column=0, row=1)

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


browse_btn = tk.Button(master, text='Simplex padrão', command= lambda:exec_simplex(), font = 'Raleway', bg="#15bebe", fg='white', height=2, width=15)
browse_btn.grid(column=1, row=2)

canvas = tk.Canvas(master, width=600,height=250)
canvas.grid(columnspan=3)
  

def exec_grafico():
    pass

def exec_modelo():
    pass

master.mainloop()