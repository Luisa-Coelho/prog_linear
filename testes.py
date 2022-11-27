####import sympy
####from sympy.parsing.sympy_parser import (
####    parse_expr, standard_transformations,
####    implicit_multiplication_application
####)
####
####
####def my_parse(s, transfm=None):
####    lhs, rhs = eq.split('=')
####    if transfm is None:
####        transfm = (standard_transformations +
####            (implicit_multiplication_application,))
####    return sympy.Eq(
####        parse_expr(lhs, transformations=transfm),
####        parse_expr(rhs, transformations=transfm))
####    
####eq = input(f"insira a restricao {restricoes}")
####
####result = sympy.solve(eq)
####print(result)
####

import simplex as sp
import definir_modelo as df
import big_m
from math import inf 

#tabuleiro = [[1,-40,-25,-10,-20,0,0,0,0,0],[0,1,1,1,1,1,0,0,0,800],[0,2,3,1,-1,0,1,0,0,650],[0,1,2,2,1,0,0,1,0,480],[0,1,3,2,0,0,0,0,1,1000]]
#
#resultado = sp.simplex(tabuleiro)
#resultado[0]

#df.definirmodelo()
infinito = float("inf")
tab_bigm = [[1,-1,-1,-1,0,0,infinito, infinito,0],[0,2,1,-1,1,0,0,0,100],[0,1,1,2,0,-1,1,0,200],[0,2,1,3,0,0,0,1,600]]
######
resultado = big_m.simplex(tab_bigm)
resultado
     
#result = '1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18'
#n_rows = 3
#n_cols = 6
#lista_nova = []
#r = 0
#c = 0
#while r < n_rows:
#    r+=1
#    counter = c
#    #result = result.split(',')
#    result = result.replace(" ", "")
#    if counter == 0:
#        result_con = result[counter:n_cols*2-1]
#        convert = [int(s) for s in result_con.split(',')]
#        lista_nova.extend(convert)
#    for x in range(counter, n_cols+counter):
#        c+=1
#    if counter > 0:
#        result_con = result[counter*2:(n_cols*2)+counter*2]
#        convert = [int(s) for s in result_con.split(',')]
#        lista_nova.extend(convert)
#    for x in range(counter+1, (n_cols*2-1)+counter+2):
#        c+=1
##c=0
##for x in range(0, n_cols):
##       c+=1
##
##result = result.replace(" ", "")
##result_con = result[c*2:(n_cols*2)+c*2]
###convert = [int(s) for s in result_con.split(',')]
##print(result_con)
#
##result = result.replace(" ", "")
##result = result[0:(n_cols*2)-1]
##convert = [int(s) for s in result.split(',')]
##print(convert)
#lista_nova



