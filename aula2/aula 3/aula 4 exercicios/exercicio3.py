def calcular_operacao(num1, num2, operador):
    if operador == '+':
        return num1 + num2
    elif operador == '-':
        return num1 - num2
    elif operador == '*':
        return num1 * num2
    elif operador == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Erro: Divisão por zero!"
    else:
        return "Operador inválido!"

def main():
    continuar = True
    
    while continuar:
        
        num1 = float(input("Digite o primeiro número real: "))
        num2 = float(input("Digite o segundo número real: "))
        operador = input("Digite o operador matemático (+, -, *, /): ")
        
        
        resultado = calcular_operacao(num1, num2, operador)
        print("O resultado da operação é:", resultado)
        
        
        continuar_resposta = input("Deseja continuar calculando? (S/N): ")
        if continuar_resposta.upper() != 'S':
            continuar = False

if __name__ == "__main__":
    main()
