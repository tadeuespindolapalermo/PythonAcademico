#Python3.6.1
#Pycharm
#GNU/Linux Ubuntu 16.10
#@utor: Tadeu Espíndola Palermo
#Data: 18/07/2017 às 13:00:00

print()
print("=" * 38)
print("Bem-vindo ao gerador de Tabuadas v 1.0")
print("Desenvolvedor: Tadeu Espíndola Palermo")
print("=" * 38 + "\n")

nome = input("Informe o seu nome: ")

def novaTabuada():
    print()
    outraTabuada = input("Deseja gerar outra Tabuada? [S]-SIM | [N]-NÃO: ")
    if outraTabuada.upper() == "S":
        contador = 1;
        print()
        try:
            numTabuadas = int(input("Quantas Tabuadas deseja gerar? "))
        except:
            print("O número digitado é inválido, tente novamente!")
            novaTabuada()
        while contador <= numTabuadas:
            tabuada()
            contador += 1
    elif outraTabuada.upper() == "N":
        print("Ok. Finalizando o programa...Obrigado por utilizar!!!")
        raise SystemExit
    else:
        print("{}, você digitou um valor inválido, tente novamente!".format(nome))
        novaTabuada()

def tabuada():
    try:
        print("Iniciando o programa, um momento por favor...\n")
        num = int(input("{}, informe um número inteiro para saber a tabuada: ".format(nome)))
        print()
        print("Gerando tabuada...Por favor, aguarde...\n")
        cont = 0
        aux = 0
        print("=" * 39)
        print("          TABUADA DO NÚMERO", num)
        print("=" * 39)
        while cont <= 10:
            aux = num * cont
            print('            {}  x {:2} = {}'.format(num, cont, aux))
            cont += 1
        print("=" * 39)
        print("Tabuada(s) gerada com sucesso! Obrigado!!!")
        print("=" * 39)
    except:
        print("{}, você digitou um número inválido!".format(nome))
        respostaUsuario = input("Deseja Sair ou Continuar? [S]-SAIR | [C]-CONTINUAR: ")
        if respostaUsuario.upper() == "C":
            tabuada()
        elif respostaUsuario.upper() == "S":
            print("Finalizando...")
            raise SystemExit
        else:
            print("{}, você digitou um valor inválido, não é possível continuar! Finalizando...".format(nome))
            raise SystemExit

tabuada()
novaTabuada()