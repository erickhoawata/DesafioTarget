def fibonacci(numero):
    a, b = 0, 1
    while b < numero:
        a, b = b, a + b
    return b == numero

def main():
    numero_verificar = int(input("Digite o número que deseja verificar na sequência de Fibonacci: "))
    if fibonacci(numero_verificar):
        print(f"O número {numero_verificar} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero_verificar} NÃO pertence à sequência de Fibonacci.")

if __name__ == "__main__":
    main()
