print("exemplo 1: ================")
i = 0
while i < 5:
    print(i,"vezes")
    i = i + 1

print("exemplo2: ========")
nomes= []
while True:
    nome = input("digite um nome")
    nomes.append(nome)
    if (nome == 'fim'):
        print(nomes)
        break