import matplotlib.pyplot 
from matplotlib.pyplot import *
import numpy as np
from numpy import arange

def montar_grafico():
    figure()

    n_rest = int(input("Quantas restrições existem nesse sistema? \t"))

    if n_rest == 1:
        maior = 0
    
        sinal = input("Sua 1° restrição tem esse []x1 + []x2 = [] ou []x1 - []x2 = [] ou []xn = [] formatos? Responda + ou - ou = \t")
        x1 = int(input(f"Insira o x1 da sua 1° restrição: \t"))
        if x1 > maior:
            maior = x1
        
        x2 = int(input(f"Insira o x2 da sua 1° restrição: \t"))
        if x2 > maior:
            maior = x1
        
        output = int(input("Insira o resultado da sua 1° restrição: \t"))
        if output > maior:
            maior = output
        
        if sinal == '+':
            ponto1a = output/x1
            ponto2a = output/x2
        
        if sinal == '-':
            ponto1a = output/x1
            ponto2a = output/x2
    
        d = np.linspace(0,maior*10,maior*10)
    
        hlines(0, -10, maior*1.5, color = 'k')
        vlines(0, -10, maior*1.5, color = 'k')
        grid(True)
        
        xlabel('X-axis')
        ylabel('Y-axis')
        
        
        #Plotting graph
        coord1 = [ponto1a, 0]
        coord2 = [0, ponto2a]
        plot(coord1, coord2, color = 'b')
     
        # get the co-ordinates of intersection points by mere visualisation
        A = [ponto1a, 0, 0.00, 0.00]
        B = [0.00, ponto2a, 0.00, 0.0]
        fill(A,B,'g+')
    
        show()
        
    if n_rest == 2:
        maior = 0
    
        sinal = input("Sua 1° restrição tem esse []x1 + []x2 = [] ou []x1 - []x2 = [] ou []xn = [] formatos? Responda + ou - ou = \t")
        x1a = int(input(f"Insira o x1 da sua 1° restrição: \t"))
        if x1a > maior:
            maior = x1a
        
        x2a = int(input(f"Insira o x2 da sua 1° restrição: \t"))
        if x2a > maior:
            maior = x2a
        
        outputa = int(input("Insira o resultado da sua 1° restrição: \t"))
        if outputa > maior:
            maior = outputa
        
        if sinal == '+':
            ponto1a = outputa/x1a
            ponto2a = outputa/x2a
        
        if sinal == '-':
            ponto1a = outputa/x1a
            ponto2a = outputa/x2a
    
        sinal = input("Sua 2° restrição tem esse []x1 + []x2 = [] ou []x1 - []x2 = [] ou []xn = [] formatos? Responda + ou - ou = \t")
        x1b = int(input(f"Insira o x1 da sua 2° restrição: \t"))
        if x1b > maior:
            maior = x1b
        
        x2b = int(input(f"Insira o x2 da sua 2° restrição: \t"))
        if x2b > maior:
            maior = x2b
        
        outputb = int(input("Insira o resultado da sua 2° restrição: \t"))
        if outputb > maior:
            maior = outputb
        
        if sinal == '+':
            ponto1b = outputb/x1b
            ponto2b = outputb/x2b
        
        if sinal == '-':
            ponto1b = outputb/x1b
            ponto2b = outputb/x2b
    
    
        d = np.linspace(0,maior*10,maior*10)
    
        hlines(0, -10, maior*1.5, color = 'k')
        vlines(0, -10, maior*1.5, color = 'k')
        grid(True)
        
        xlabel('X-axis')
        ylabel('Y-axis')
        
        
        #Plotting graph
        coord1 = [ponto1a, 0]
        coord2 = [0, ponto2a]
        
        coord3 = [ponto1b, 0]
        coord4 = [0, ponto2b]
        plot(coord1, coord2, color = 'b')
        plot(coord3, coord4, color = 'r')    
      
        # get the co-ordinates of intersection points by mere visualisation
        A = [ponto1a, 0, 0.00, 0.00]
        B = [0.00, ponto2a, 0.00, 0.0]
        fill(A,B,'g+')
        
        #c = [0, 10, 10, 7.5]
        #d = [10, 0, 6.67, 10]
        #fill(c,d,'b+')
        
        e = [0, ponto1b, ponto1a, 0]
        f = [ponto2b, 0, 0, ponto2a]
        fill(e,f,'r+')
        
        show()
        
    
    
    x, y = np.meshgrid(d,d)
    matplotlib.pyplot.imshow( ((3*y <= 200 - 2*x) & (3*y <= 300 - x)).astype(int), extent=(x.min(),x.max(),y.min(),y.max()), origin="lower", cmap="Greys", alpha = 0.3)
    