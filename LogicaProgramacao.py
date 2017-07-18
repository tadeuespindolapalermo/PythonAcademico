#Tadeu Espíndola Palermo

#Ex.: 1
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
s = n1 + n2
print()
print("A soma entre {} e {} é igual a {} ".format(n1,n2,s))
print("A soma entre %i e %i é igual a %i " % (n1,n2,s))
print()

#Ex.:2
n = input("Digite algo: " )
print()
print("O tipo primitivo de {} é: {}".format(n, type(n)) + "\n")
print("É {} que {} é alfanumérico!".format(n.isalnum(),n))
print("É {} que {} é alfabético!".format(n.isalpha(),n))
print("É {} que {} é um dígito!".format(n.isdigit(),n))
print("É {} que {} é um identificador!".format(n.isidentifier(),n))
print("É {} que {} está em minúsculas!".format(n.islower(),n))
print("É {} que {} é um número!".format(n.isnumeric(),n))
print("É {} que {} é imprimível!".format(n.isprintable(),n))
print("É {} que {} só tem espaços!".format(n.isspace(),n))
print("É {} que {} está capitalizada!".format(n.istitle(),n))
print("É {} que {} está em maiúsculas!".format(n.isupper(),n))

#Ex.:3
print()
num = int(input("Digite um número inteiro: "))
suc = num + 1
ant = num - 1
print("O SUCESSOR do número informado é: {} e seu ANTECESSOR é: {}.".format(suc,ant))

#Ex.:4
print()
num = int(input("Informe um número: "))
dobro = num * 2
triplo = num * 3
raiz = num**(1/2)
print("O dobro do número informado é: {}".format(dobro))
print("O tripo do número informado é: {}".format(triplo))
print("A raiz quadrada do número informado é: {:.2f}".format(raiz))

#Ex.:5
print()
nota1 = float(input("Entre com a primeira nota do aluno: "))
nota2 = float(input("Entre com a segunda nota aluno: "))
media = (nota1 + nota2) / 2
print("A média entre {:.1f} e {:.1f} é igual a {:.1f}".format(nota1,nota2,media))

#Ex.:6
print()
metros = float(input("Entre com o valor em metros: "))
centimetros = metros * 100
milimetros = metros * 1000
print("O valor de {} metros corresponde à: {:.0f} centímetros e "
      "{:.0f} milímetros.".format(metros,centimetros,milimetros))

#Ex.:7
print()
num = int(input("Entre com um número inteiro para ver sua tabuada: "))
print()
cont = 0
aux = 0
print("="*18)
print("  TABUADA DO",num )
print("="*18)
while cont <= 10:
    aux = num * cont
    print('{} x {:2} = {}'.format(num,cont,aux))
    cont += 1
print("="*18)

#Ex.:8
print()
carteira = float(input("Entre com o valor de dinheiro que tem na carteira: R$ "))
dolares = carteira / 3.27
print("Com {:.2f} R$ é possível comprar {:.2f} US$.".format(carteira,dolares))

#Ex.:9
print()
largura = float(input("Entre com a largura: "))
altura = float(input("Entre com a altura: "))
area = largura * altura
tinta = area / 2
print("Sua parede tem a dimensão de {} x {} e sua área é de {} M.".format(largura,altura,area))
print("Para pintar essa parede você precisará de {} L de tinta.".format(tinta))

#Ex.:10
print()
preco = float(input("Entre com o preço do produto: R$ "))
novoPreco = preco - (preco * 5 / 100)
print("O produto que antes custava R$ {:.2f}, com 5 % de desconto passará a custar R$ {:.2f}. ".format(preco,novoPreco))

#Ex.:11
print()
salario = float(input("Entre com o atual salário do funcionário: R$ "))
novoSalario = salario + (salario * 15) / 100
print("O salário do funcionário que antes era R$ {:.2f}, com 15% de desconto passará a ser R$ {:.2f}".format(salario,novoSalario))


#Ex.:12
print()
c = float(input("Informe a temperatura em graus °C: "))
f = 9 * c / 5 + 32
print("A temperatura de {:.0f} °C corresponde à {:.0f} °F!".format(c,f))

#Ex.:13
dias = (int(input("Quantos dias alugados: "))) * 60
km = (float(input("Quantos Km rodados: "))) * 0.15
total = dias + km
print("O total a pagar é de R$: {:.2f}".format(total))