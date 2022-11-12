##############################################
########## GRÁFICO ###########################
##############################################
import matplotlib.pyplot 
from matplotlib.pyplot import *
import numpy
from numpy import arange


num_rest = [(2, 1), (10, 12)]
c = 0
for regioes in (num_rest):
  c+=1 
  for i in range(0, 2):
    if i == 0 and c == 1:
      ponto1 = 2*regioes[i] + 0 - 6
    if i == 1 and c == 1:
      ponto2 = 0 + regioes[i] - 6
    if i == 0 and c == 2:
      ponto3 = 0 + 12*regioes[i] - 60
    if i == 1 and c == 2:
      ponto4 = 10*regioes[i] + 0 -60

for i in range(1, len(num_rest)+1):
  pass


figure()
hlines(0, -20, 80, color = 'k')
vlines(0, -20, 80, color = 'k')
grid(True)
plot([ponto1, 0], [0, ponto2], "b")
plot([ponto3, 0], [0, ponto4], "y")

A = [ponto1, 0, 0.00, 0.00]
B = [0.00, ponto2, 0.00, 0.0]
fill(A,B,'g+')

C = [0, ponto3, 0, 0]  ###ponto1 e ponto3 são negativos??
D = [ponto4, 0, 0, 0]
fill(C,D,'r+')
