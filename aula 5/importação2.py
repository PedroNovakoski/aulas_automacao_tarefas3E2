from funções import login 

while True:
    user = input('Digite o nome do usuario:')
    pwd = input ('Digite a senha do usuario:')
    if login(user, pwd):
        break
    else:
        print('Tente novamente!')