import time  #Bibliotecas usadas - tempo / gerador de numero
from random import randint
print('============= MERCADO DIA A DIA =============')
lista = [] #Suposta lista vazia de compras, onde ficam armazenadas as "compras" (valores)
while True: #Primeira condição
    cliente = int(input('Cliente dia a dia: [0 = NÃO/ 1 = SIM]')) #Caso o cliente seja registrado ele tem desconto de 1.5 em todos os produtos
    if cliente == 0:
        cpf = int(input('CPF na nota: [0 = NÃO/ 1 = SIM]')) #Caso não seja registrado adicionar CPF na nota
        if cpf == 1:
            registrar_cpf = int(input('Digite o CPF:')) 
        while True: #Segunda condição
            produto = float(input('Registre o produto (ou 0 para sair): ')) #Registra os valores
            if produto == 0: #Se valor 0 adicinado enterronpe o loop
                break
            lista.append(produto) #Adiciona os valores na lista produto
            total1 = sum(lista) # Soma todos os valores da lista
            print(f'total: {total1:.2f}')
        break
    elif cliente == 1:
        while True: #Terceira condição
            produto = float(input('Registre o produto (ou 0 para sair): ')) #Registra os valores
            if produto == 0:
                break
            lista.append(produto)
            total1 = sum(lista)
            total1 = total1 - (total1 * (1.5 / 100))
            print(f'total: {total1:.2f}')
        break
    else:
        print('Numero invalido')
print('[0] = Dinheiro | [1] = Cartão Debito/credito | [2] = PIX')
forma_pagamento= int(input('Qual a forma de pagamento: '))
if forma_pagamento == 0:
    valor = int(input('Valor:'))
    troco = (valor - total1)
    print(f'Total de compras: {total1:.2f} | Valor recebido: {valor:.2f}| Troco: {troco:.2f}')
    print('OBRIGADO PELA PREFENCIA')
elif forma_pagamento == 1:
    formas = int(input('[0] Debito | [1] Credito: '))
    if formas == 1 and total1 >= 150:
        pagamento = int(input('Deseja dividir: [0] NÃO | [1] 2x: '))
        if pagamento == 1:
            dividir = total1 / 2
            print(f'Total de compras: {total1:.2f}, Parcelas: {dividir:.2f}')
    senha = int(input('Digite a senha: '))
    time.sleep(1)
    print('Pagamento aprovado')
    print('OBRIGADO PELA PREFENCIA')
elif forma_pagamento == 2:
    numero_aleatorio = randint(100000000, 999999999) #Gera uma sequencia de numeros aleatorios simulando um codigo PIX
    print(f'Codigo pix:', numero_aleatorio)
    time.sleep(3)
    print('Pagamento aprovado')
    print('OBRIGADO PELA PREFENCIA')
