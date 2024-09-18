def is_fibonacci(n):
    # Função para gerar a sequência de Fibonacci até o número n
    fib_sequence = [0, 1]
    
    # Continuar a gerar até o número ser maior ou igual a n
    while fib_sequence[-1] < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    
    # Verificar se o número está na sequência
    if n in fib_sequence:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} NÃO pertence à sequência de Fibonacci."

# Solicitar o número ao usuário
numero = int(input("Informe um número: "))

# Chamar a função e exibir o resultado
print(is_fibonacci(numero))
