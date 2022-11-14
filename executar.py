import simplex as sp
import grafico as gr
import definir_modelo as dm

prob1= [[1,-20,-30,-10,0,0,0,0], [0,1,1,1,1,0,0,400], [0,2,1,-1,0,1,0,200], [0,3,2,-1,0,0,1,300]]
prob2 = [[-4,-3,0,0,0,0],[1,3,1,0,0,7],[2,2,0,1,0,8],[1,1,0,0,1,3]]
sapateiro = [[1, -5, 2, 0, 0, 0], [0, 2, 1, 1, 0, 6], [0, 10, 12, 0, 1, 60]]
resultado = sp.simplex(prob2)
resultado
print(f"O resultado de lucro máximo é de: R${resultado[0][5]}")

#dm.definirmodelo()