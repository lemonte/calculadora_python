def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Erro: divisão por zero"


def main():
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")
    option = input("Escolha uma opção (1/2/3/4/5): ")

    if(float(option) < 1 or float(option) > 5):
         raise Exception("Opção inválida. Tente novamente.")

    if option == '5':
        print("Saindo da calculadora...")
        return '5'

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if option == '1':
        print("Resultado:", add(num1, num2))

    elif option == '2':
        print("Resultado:", subtract(num1, num2))

    elif option == '3':
        print("Resultado:", multiply(num1, num2))

    elif option == '4':
        print("Resultado:", divide(num1, num2))
    else:
        print("Opção inválida. Tente novamente.")
    return option


while True:
    try:
        opcao = main()
        if(opcao == '5'):
            break
        print("\n###############################################\n\n")

    except Exception as e:
        print("\n\n###############################################\n")
        print("Valor digitado inválido. Tente novamente.\n" + str(e))
        print("###############################################\n\n")