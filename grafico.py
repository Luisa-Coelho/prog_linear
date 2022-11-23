##############################################
########## GRÁFICO ###########################
##############################################
#import matplotlib.pyplot 
from matplotlib.pyplot import *
import numpy
from numpy import arange
from sympy import symbols, Eq, solve
from sympy.abc import x, a
from sympy.parsing.sympy_parser import (
    parse_expr, standard_transformations,
    implicit_multiplication_application
)

print sympy.solve(32*x-40,"x")
print sympy.solve(2*x+23-7*x,"x")





def my_parse(s, transfm=None):
    lhs, rhs = eq.split('=')
    if transfm is None:
        transfm = (standard_transformations +
            (implicit_multiplication_application,))
    return sympy.Eq(
        parse_expr(lhs, transformations=transfm),
        parse_expr(rhs, transformations=transfm))



#num_rest = [(2, 1), (10, 12)]
c = 0

n_var = int(input("insira n° variaveis"))
n_rest = int(input("insira n° restricoes"))


data_dict = {}
data_dict['x1'] = 0
data_dict['x2'] = 0
data_dict['x3'] = 0
data_dict['x4'] = 0
data_dict['x5'] = 0
data_dict['x6'] = 0
data_dict['x7'] = 0

for i in data_dict: 
    for j in range(n_rest):
        data_dict[i][j] = 0
        result = simpy.solve(expr)
        lista_nova.append(result)


lista_pontos = []
for restricoes in (n_rest):
  eq = input(f"insira a restricao {restricoes}")
  expr = my_parse(eq)
  c+=1 
  for i in range(0, n_var):
    expr.subs(x{i}, 0)
    if i == 0 and c == 1:
      ponto = 2*regioes[i] + 0 - 6
      lista_pontos.append(ponto)
    if i == 1 and c == 1:
      ponto2 = 0 + regioes[i] - 6
    if i == 0 and c == 2:
      ponto3 = 0 + 12*regioes[i] - 60
    if i == 1 and c == 2:
      ponto4 = 10*regioes[i] + 0 -60

n_rest = int(input("Insira a qtde de restricoes"))
for i in lista_pontos:

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
