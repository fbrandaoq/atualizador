# lista de 6 nomes
nomes = ['Alex','Fernanda','Carlos','Carla','Joana','José']

# usuário informa o indice que deseja alterar
indice = int(input('Informa o indice que deseja alterar: '))
indice  -= 1

#usuário informa o novo nome
nomes[indice] = input('Informe o novo nome: ')

#exibe a lista
for nome in nomes:
    print(nome)