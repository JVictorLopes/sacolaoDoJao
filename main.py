from tkinter import N
dicionario = {}
# função para adicionar frutas, listar frutas adicionadas e buscar pelo nome
def adicionar_fruta():
  qFrutas = int(input("Quantas frutas deseja adicionar? \n"))
  i = 0
  for i in range(0, qFrutas, 1):
    nomeFruta = (input("Insira o nome da fruta: \n"))
    valorFruta = float(input("Insira o preço da fruta: \n"))
    quantFruta = int(input("Insira a quantidade de frutas: \n"))

    dicionario[nomeFruta] = {"Valor:": valorFruta, "Quantidade:": quantFruta}

  Acao = int(input("Digite '1' para listar as frutas ou '2' para buscar uma fruta pelo nome."))
  if Acao == 1:
    print("Estoque de Frutas:")
    for nomeFruta, info in dicionario.items():
      print(f"{nomeFruta}: Valor = R${info[valorFruta]:.2f} | Quantidade = {info[quantFruta]}")
  if Acao == 2:
    fruta = input("Digite o nome da fruta que deseja buscar: ")
    if fruta in dicionario:
        print("{}: valor = R${:.2f} | quantidade = {}".format(nomeFruta, valorFruta['valor'], quantFruta['quantidade']))
    i+=1

#menu principal
while True:
    print("Sacolão do Jão")
    opcao = input("Digite 'a' para adicionar uma fruta. Digite 's' para sair: ")
    if opcao == 'a':
        adicionar_fruta()
    elif opcao == 's':
        break
    else:
        print("Opção inválida!")