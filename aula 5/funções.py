'''as funções são utilizadas para modularizar o código, ou seja, dividi-lo em partes menores, que podem ser reutilizadas.

estruturas:

def nome_funcao(param1, param2):
    faz algo 
    return Valor   

exemplos:'''

def calcularAreaTriangulo(base, altura):
    area = (base * altura) / 2 
    return area

def login(usuario, senha):
    if usuario == 'admin' and senha == '123':
        return True 
    else:
        return False
    
#print(login("ivan", '123'))
#area = calcularAreaTriangulo(100,50)
#print('A area do triangulo é', area)