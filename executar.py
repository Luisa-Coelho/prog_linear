import simplex
import grafico
import definir_modelo

prob_exemplo = [[1,-20,-30,-10,0,0,0,0], [0,1,1,1,1,0,0,400], [0,2,1,-1,0,1,0,200], [0,3,2,-1,0,0,1,300]]
resultado = simplex(prob_exemplo)
resultado
print(f"O resultado de lucro máximo é de: R${resultado[0][7]}")