#bfo = 1
#rest_x1 = 1
#rest_x2 = 2
#rest_xf1 = 1
#b_rest = 1

### tabuleiro ficticio com 4 colunas e 2 linhas i.e. 2 variáveis e 1 restrição
#matriz1 = [[fo_x1, fo_x2, fo_xf1, bfo], [rest_x1, rest_x2, rest_xf1, b_rest]]

#global fo_x1
#global fo_x2
#global fo_x3
#global bfo
#global solution
solution = 1
global resultado 

def check_max(linha, n_col):
  #if n_col == 6:
  #  fo_x1 = matriz[0][1]
  #  fo_x2 = matriz[0][2]
  #  bfo = matriz[0][3]
  #if n_col == 8:
  #  fo_x1 = matriz[0][1]
  #  fo_x2 = matriz[0][2]
  #  fo_x3 = matriz[0][3]
  #  bfo = matriz[0][7]
  #return fo_x1, fo_x2, fo_x3, bfo
  c = 0
  for i in linha:
    c+=1
    if i < 0:
      break
    if c == n_col and i >= 0:
      return True

  

def simplex(matriz):
  #fo_x1, fo_x2, fo_x3, bfo = (-1, -1, -1, -1) 
  # while fo_x1 < 0 or fo_x2 < 0 or fo_x3 < 0 or bfo < 0:
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
    resultado = check_max(z, n_colunas) 

  return matriz

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