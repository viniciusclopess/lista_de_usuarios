import os
import random
os.system('cls')
lista_usuarios = []
emails = ["@gmail.com", "@outlook.com", "@hotmail.com","@yahoo.com"]
ddd_brasil = [
    "68", "82", "96", "92", "71",
    "85", "61", "27", "62", "98",
    "65", "67", "31", "91", "83",
    "41", "81", "86", "21", "84",
    "51", "69", "95", "47", "11",
    "79", "63"
]
#Loop do programa
while True:
    print('*' * 60)
    print('LISTA DE CONTATOS')
    escolha = input('''[i]nserir
[r]emover
[l]istar
[s]air
sua opção->''')
    #Escolheu a opção inserir
    if escolha == 'i':

        nome = input('Insira seu nome: ')
        while len(nome) <= 2:
            nome = input('Insira um nome válido: ')
        nome = nome.capitalize()        


        email = input('Insira seu email: ')
        while len(email) < 4 or len(email) > 20:
            email = input('Insira um e-mail válido: ')    
        if '@' not in email:
            email += random.choice(emails)

        
        telefone = input('Insira seu telefone: ')
        while len(telefone) != 16:
            if len(telefone) == 9:
                telefone = f"+55({random.choice(ddd_brasil)}){telefone}"
            elif len(telefone) == 11:
                ddd = telefone[0] + telefone[1]
                telefone = f"+55({ddd}){telefone[2:]}"
            else:
                telefone = input('Insira um número válido:')
            
            
        info_usuario = {
            'nome': nome,
            'email': email,
            'telefone': telefone
        }
        lista_usuarios.append(info_usuario)
        print('listado com sucesso')

    #Escolheu a opção remover
    elif escolha == 'r':
        remover = int(input("índice para remover: "))
        if remover >= len(lista_usuarios):
            print('Índice inválido.')
        else:
            print(f'índice {remover} removido')
            del lista_usuarios[remover]

    #Escolheu a opção listar
    elif escolha == 'l':
        os.system('cls')
        if len(lista_usuarios) == 0:
            print('Nada para listar')
        else:
            for indice, usuario in enumerate(lista_usuarios):
                print(f'Índice: {indice} -- Nome: {usuario["nome"]} -- E-mail: {usuario["email"]} -- Telefone: {usuario["telefone"]}')
    
    #Escolheu a opção sair
    elif escolha == 's':
        print('encerrando...')
        break
