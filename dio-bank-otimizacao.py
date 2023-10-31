import sys
import time

nomeBanco = ("DioBank".center(63,"-"))
linhaBranca = ("".center(63,"-"))
menu = f"""
{nomeBanco}

Selecione a opção abaxio conforme sua operação.

[1] - Saque
[2] - Depósito
[3] - Extrato
[4] - Sair
[5] - Cadastrar Usuário
[6] - Banco de cadastros
[7] - Criar conta corrente

{linhaBranca}
"""
menuProximo = f"""
Deseja realizar outra operação?

[1] - Saque
[2] - Depósito
[3] - Extrato
[4] - Sair
[5] - Cadastrar Usuário
[6] - Banco de cadastros
[7] - Criar conta corrente


{linhaBranca}
"""
menuErro = f"""

A opção selecionada não existe, tente novamente.

[1] - Saque
[2] - Depósito
[3] - Extrato
[4] - Sair
[5] - Cadastrar Usuário
[6] - Banco de cadastros

{linhaBranca}
"""

saldo = 0
limite = 0
numero_depositos = 0
valorDepositado = 0
numero_saques = 0
valorSaque = 0
LIMITE_SAQUES = 3
contador = 0
numeroContas = 0

def menuSelecionar(palavra):
    print(palavra)
    opcao = int(input())
    operacao = switch.get(opcao, erro)
    operacao()
#Criar usuário

usuarios = [
]
def cadastrarUsuario():
    usuario = {}
    usuario["nome"] = str(input("Me informe seu nome completo\n"))
    usuario["data-Nascimento"] = str(input("Qual sua data de nascimento? Coloque um . para separar (xx.xx.xxxx)\n"))
    cpfVerificar = int(input("Digite o seu CPF (apenas números)\n"))
    for u in usuarios:
        if u["cpf"] == cpfVerificar:
            print("Desculpe, o CPF já está cadastrado, tente novamente..\n")
            cadastrarUsuario()
    usuario["cpf"] = cpfVerificar
    print("Agora vamos cadastrar seu endereço")
    rua = str(input("Qual nome da sua rua?\n"))
    bairro = str(input("Qual o bairro?\n"))
    cidade = str(input("Qual cidade você mora?\n"))
    estado = str(input("Qual estado você mora?\n"))
    endereco = f"Rua: {rua}, Bairro: {bairro} em {cidade}/{estado}"
    usuario["endereco"] = endereco
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!..\n")
    menuSelecionar(menuProximo)
def criarConta():
    global numeroContas
    print("Vamos abrir sua conta conosco, mas antes disto preciso saber se você tem cadastro em nosso banco\n")
    cpfTitular = int(input("Informa qual o número do seu CPF"))
    
    for u in usuarios:
        if u["cpf"] == cpfTitular:
            numeroContas = numeroContas + 1
            print(u["nome"],f"seu cadastro foi encontrado, sua conta foi criada! o número da sua conta é {numeroContas}, agência 0001")
            u["contaAgencia"] = "0001"
            u["contaNumero"] = numeroContas
            menuSelecionar(menuProximo)
        else:
            print("usuario não encontrado, tente novamente")
            menuSelecionar(menuProximo)
def listarUsuarios():
    global contador
    for usuario in usuarios:
        contador = contador + 1 
        print("Usuário ",contador,"Nome: ",usuario["nome"],"| Data nascimento: ",usuario["data-Nascimento"],"| CPF: ",usuario["cpf"], "Endereço: ",usuario["endereco"],"\n")
    contador = 0;
    menuSelecionar(menuProximo)
def deposito():
    global saldo, numero_depositos, valorDepositado
    deposito = float(input("Ok, informe o valor que você deseja depósitar\n"))
    if deposito > 0:
        saldo += deposito
        print(f"Depósito concluido com sucesso! Seu saldo atual é de R${saldo:.2f}\n")
        numero_depositos += 1
        valorDepositado += deposito
        menuSelecionar(menuProximo)
    else:
        print("Não foi possível realizar a operação.. tente novamente")
        menuSelecionar(menu)
def saque():
    global saldo, valorSaque, numero_saques
    if numero_saques < LIMITE_SAQUES:
        saque = float(input("Digite o valor do saque\n"))
        if saque > 500:
            print("Seu limite de saque é de R$ 500,00.")
            menuSelecionar(menuProximo)
        elif saque <= saldo:
            saldo -= saque
            numero_saques += 1
            valorSaque += saque
            print(f"Saque no valor de R${saque:.2f} foi efetuado com sucesso.\nSeu novo saldo é de R${saldo:.2f}\n") 
            menuSelecionar(menuProximo)
        else:
            print("Saldo insufiente, tente novamente")
            menuSelecionar(menu)
    else:
        print("Seu limite de saque diário expirou.")
        menuSelecionar(menuProximo)
def extrato():
    print(f"""
{nomeBanco}
Seu extrato detalhado.

Total de operações {numero_depositos+numero_saques} 

Número  total de saques: {numero_saques}
Valor total sacado: {valorSaque}
Número total de depósitos: {numero_depositos}
Valor total depósitado: {valorDepositado}

Saldo atual: {saldo}
Limite de saque diário: {LIMITE_SAQUES} / {numero_saques}
""")
    menuSelecionar(menuProximo)
def sair():
    print("Finalizando, aguarde!")
    time.sleep(2)
    sys.exit()
def erro():
    menuSelecionar(menuErro)

switch = {
    1: saque,
    2: deposito,
    3: extrato,
    4: sair,
    5: cadastrarUsuario,
    6: listarUsuarios,
    7: criarConta
}

menuSelecionar(menu)
