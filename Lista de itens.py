import os

lista = []

def adicionar_item():
    addItem = 0
    while addItem < 1:
        item = input("Digite um novo item: ")
        lista.append(item)
        addItem+=1
        print(f"Item '{item}' adicionado!")
    print('\n')


def info_lista():
    print(f"Quantidade de items: {len(lista)}")
    print("Itens armazenados na lista:")
    for l in lista:
        print("- " + l)
    print('\n')


def excluir_item():
    for l in lista:
        print("- " + l)
    excl_item = input("\nDigite o nome do item que deseja excluir\nDigite aqui: ")
    if (excl_item in lista):
        lista.remove(excl_item)
        print(f"\nO item '{excl_item}' foi excluido!\n\nItens restates:\n" + str(lista) + "\n")
    else:
        print("Item nao existe na lista!")

def menu_item():
    menu = 0
    while menu != 4:
        selMenu = input("\nSelecione a opcao desejada:" +
                "\n1 - Adicionar Item" +
                "\n2 - Informações da lista" + 
                "\n3 - Deletar Item" +
                "\n4 - Sair do programa" + 
                "\nDigite aqui: ")
        os.system('cls')

        if (selMenu == '1'):
            print("ADICIONAR ITEM")
            adicionar_item()
            os.system('pause'), os.system('cls')
        elif (selMenu == '2'):
            print("INFO. DA LISTA")
            info_lista()
            os.system('pause'), os.system('cls')
        elif (selMenu == '3'):
            print("EXCLUIR ITEM")
            excluir_item()
            os.system('pause'), os.system('cls')
        elif (selMenu == '4'):
            print("Saindo do programa...")
            os.system('pause'), os.system('cls')
            quit()
        else: ("Programa finalizado!")
menu_item()