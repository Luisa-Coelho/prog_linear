import simplex as sp
import grafico as gr
import definir_modelo as dm
import tkinter as tk
from PIL import Image, ImageTk

#https://www.youtube.com/watch?v=itRLRfuL_PQ - moça
#https://www.youtube.com/watch?v=VMP1oQOxfM0 - indiano

master = tk.Tk()
master.title("Programação Linear - Passo a passo")
canvas = tk.Canvas(master, width=600,height=300)
canvas.grid(columnspan=3, rowspan=3)

logo = Image.open('sign.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
#logo_label.grid(column=1, row=0)

#instructions
instructions = tk.Label(master, text = 'Selcione o que você deseja fazer', font='Raleway')
instructions.grid(columnspan=3, column=0, row=1)

#browse_text = tk.StringVar()
#browse_text.set('É ISSO QUE VOÇÊ QUER???')
def exec_simplex():
    name = input("Insira seu nome....")
    print(f"Bem-vindx, {name}")
    problema = input("Insira seu problema de programação linear")
    print(problema)
    solution = list(problema)
    print(solution[0])

browse_btn = tk.Button(master, text='browse_text', command= lambda:exec_simplex(), font = 'Raleway', bg="#15bebe", fg='white', height=2, width=15)
browse_btn.grid(column=1, row=2)

canvas = tk.Canvas(master, width=600,height=250)
canvas.grid(columnspan=3)



    

def exec_grafico():
    pass

def exec_modelo():
    pass

master.mainloop()