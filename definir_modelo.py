from collections import Counter

##############################################
########## CONSTRUINDO O MODELO ##############
##############################################
def definirmodelo():
  fo = input('Insira a função objetivo ')

  fo_tipo = input("Qual o tipo da sua função objetivo? É de custo, receita, lucro...?")

  lista_min = ['custo']
  lista_max = ['receita', 'lucro']


  ###3x1 + 4x2 + 3x3 + 4x4 
  sign_count = 0
  for signs in fo:
    if(signs in ['+', '-']):
        sign_count += 1

  n_var = sign_count + 1
  n_fixo = 2 ### b e fo


  continuar = 0
  rest = []
  i = 0
  n_rest = 0
  try:
    while(continuar != 2):
      rest.append(input(f"Insira a restrição {i+1}"))
      i+=1
      n_rest+=1
      continuar = int(input('Deseja inserir mais restrições? 1 - Sim    2 - Não'))
  except ValueError:
    pass

  print("\n\n\n")
  print("Resposta do modelo de PL")
  print("Função objetivo")
  if fo_tipo in lista_min:
    print("Mínimo de FO")
  else:
    print("Máximo de FO")
  print(fo)

  print("Variáveis")
  i = 0
  for i in range(n_var):
    i+=1
    print(f"x{n_var-(n_var - i)}")


  print("Restrições")
  for i in rest:
    print(i)

  print("Não negatividade")
  i = 0
  for i in range(0, n_var):
    i+=1
    print(f"x{n_var-(n_var - i)} >= 0")

