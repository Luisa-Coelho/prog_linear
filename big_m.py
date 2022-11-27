import simplex as sp

global auxiliares
auxiliares = int(input("Insira a quantidade de auxiliares."))

def simplex(matriz):

  resultado = False
  while resultado != True:
    matriz_t = transpose(matriz)
    n_linhas = len(matriz)
    n_colunas = len(matriz_t)
    colunaPivo = coluna_pivo(matriz, 0, n_colunas)
    linhaPivo = linha_pivo(matriz, 9999, colunaPivo, n_linhas, n_colunas)
    elementoPivo = matriz[linhaPivo][colunaPivo]
    matriz_t = transpose(matriz)
    vetor = matriz_t[colunaPivo]
    matriz = tabuleiros(matriz, colunaPivo, linhaPivo, elementoPivo, vetor, n_linhas, n_colunas)
    z = matriz[0]
    resultado = check_auxiliares(matriz, auxiliares, n_colunas, n_linhas) 

  #for col in matriz:
  #  for i in range(n_colunas-1-auxiliares, n_colunas):
  #      #del col[i]
  #      
  #for i in range(n_colunas-1-auxiliares, n_colunas):
  #      #del col[i]
  #      matriz= list(map(lambda x: x.pop(i), matriz))
  matriz = transpose(matriz)
  m1 = matriz_t[0:n_colunas-auxiliares]
  m2 = matriz_t[n_colunas-1]
  matriz = m1.append(m2)
  matriz = transpose(matriz)

  sp.simplex(matriz) 

  
def transpose(lista1):
    # iterate over list l1 to the length of an item
    lista2 = []
    for i in range(len(lista1[0])):
        # print(i)
        row =[]
        for item in lista1:
            # appending to new list with values and index positions
            # i contains index position and item contains values
            row.append(item[i])
        lista2.append(row)
    return lista2

def coluna_pivo(matriz, menorColuna, n_colunas):
  global colunaPivo
    ###achando coluna IN e linha OUT
  for i in range(1, n_colunas - 1): ##COLUNA IN >> RANGE(0+i, len(matrix)-1) -- range não contabiliza o último....
    if matriz[0][i] < menorColuna:
      menorColuna = matriz[0][i]
      colunaPivo = i
  
  return colunaPivo
      

def linha_pivo(matriz, menorLinha, colunaPivo, n_linhas, n_colunas):
  
  global linhaPivo
  for x in range(1, n_linhas):  
    try:
      if(matriz[x][n_colunas - 1]/matriz[x][colunaPivo] < menorLinha and matriz[x][n_colunas - 1]/matriz[x][colunaPivo] >= 0):
        menorLinha = matriz[x][n_colunas - 1]/matriz[x][colunaPivo]
        linhaPivo = x
    except ZeroDivisionError:
      continue

  return linhaPivo

def tabuleiros(matriz, colunaIn, linhaOut, elem_pivo, vetor, n_linhas, n_colunas):

  for line_p in range(0, n_linhas):
    if line_p == linhaOut:
      for col in range(0, n_colunas):
        matriz[line_p][col] = matriz[line_p][col]/elem_pivo ##mudou NLP - ok!

  for line in range(0, n_linhas):
    if line != linhaOut:
      for col in range(0, n_colunas):
        nova_linha = matriz[linhaOut][col] * (vetor[line]*-1) ##### 
        matriz[line][col] += nova_linha
  
  print("\n")
  #solution+=1
  print(f"Solução {solution}")
  print(matriz) 
  print("\n") 

  return matriz   

solution = 1
global resultado 

def check_auxiliares(matriz, auxiliares, n_colunas, n_linhas):
  zero = 0
  um = 0
  c = 0
  for i in range(0, n_colunas):
    if i >= n_colunas-auxiliares and i < n_colunas:
        for x in range(0, n_linhas):
            if matriz[x][i]> 1 or matriz[x][i] > 10000000000:
                c+=1
            if matriz[x][i] == 0:
                zero+=1
            if matriz[x][i] == 1:
                um+=1
  if um == 1*auxiliares and zero == n_linhas*auxiliares - auxiliares:
    return False
  if c > auxiliares:
    return True
