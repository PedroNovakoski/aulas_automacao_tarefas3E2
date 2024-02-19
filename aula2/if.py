print ('digite sua idade: ')
idade = input()
idade = int(idade) + 1

print("no ano que vem sua idade será", idade)

if idade <= 12:
     print('voce é uma criança')           
elif idade < 18:
     print('voce é um adolescente')
elif idade <= 64:
     print('voce e um adulto')
elif idade >= 65:
    print('voce e um idoso')