'''para utilizarmos as funções  criadas em outros arquivos de código fonte devemos importa-las.para isso utilizamos o comando import ou from import

exemplo1:importar todas as funções do arquivo funções'''

import funções 

base = float(input('digite a base do triangulo:'))
altura = float(input('digite a altura do triangulo:'))

area = funções.calcularAreaTriangulo(base, altura)
print(area)
