#Tadeu Espíndola Palermo

print()
print("=====================================================")
print("==========PROGRAMA PARA ORDENAÇÃO DE LISTA===========")
print("=====================================================")

def tratamentoExcept():
    print()
    print("Você não inseriu um número inteiro!\n")
    sair = input("Deseja encerrar o progama? [S]sim - [N]não: ")
    print()
    if sair == "S" or sair == "s":
        print("Saindo do Programa... Obrigado por utilizar!")
        print("Volte sempre!")
        raise SystemExit
    elif sair == "N" or sair == "n":
        print("Reiniciando o programa...")
        main()
    else:
        print("Você digitou uma opção inválida!\n")
        print("Reiniciando o programa, por favor aguarde...")
        main()

def buubleSort(lista):
    # Algoritmo de Ordenação Bubble Sort com Python
    tamanho_lista = len(lista)
    for i in range(tamanho_lista):
        troca = False
        for j in range(1, tamanho_lista - i):
            if lista[j] < lista[j - 1]:
                lista[j], lista[j - 1] = lista[j - 1], lista[j]
                troca = True
        if not troca:
            break

def main():
    try:
        print()
        num = int(input("Quantos números deseja inserir na lista?: "))

        print()
        contador = 0
        lista = []

        while num > contador:
            contadortxt = str(contador)
            insere = int(input("Insira o número " + contadortxt + " na lista: "))
            lista.append(insere)
            contador += 1

        print()
        print("Processando... Espere, por favor...")
        print()
        print("Lista NÃO ORDENADA:", lista, "\n")

        buubleSort(lista)

        print("Lista ORDENADA:    ", lista, "\n")
        print("A ordenação ocorreu com sucesso!\n")

    except:
        tratamentoExcept()
main()

#FIM


