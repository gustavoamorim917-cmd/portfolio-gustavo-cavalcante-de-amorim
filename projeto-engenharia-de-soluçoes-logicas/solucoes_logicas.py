# Projeto: Engenharia de Soluções Lógicas
# Autor: Gustavo Cavalcante de Amorim
# Disciplina: Programação de Computadores - UNICID
# Descrição: Soluções lógicas e algorítmicas aplicadas a problemas reais

def verificar_numero_primo(n):
    """Verifica se um número é primo."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def calcular_fatorial(n):
    """Calcula o fatorial de um número."""
    if n == 0 or n == 1:
        return 1
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def sequencia_fibonacci(n):
    """Gera os primeiros n termos da sequência de Fibonacci."""
    sequencia = []
    a, b = 0, 1
    for _ in range(n):
        sequencia.append(a)
        a, b = b, a + b
    return sequencia

def ordenar_lista(lista):
    """Ordena uma lista usando bubble sort."""
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def calcular_media(notas):
    """Calcula a média de uma lista de notas."""
    if not notas:
        return 0
    return sum(notas) / len(notas)

# Exemplos de uso
if __name__ == "__main__":
    print("=== Verificação de Primos ===")
    numeros = [2, 3, 4, 7, 10, 13, 17]
    for num in numeros:
        status = "primo" if verificar_numero_primo(num) else "não primo"
        print(f"{num} é {status}")

    print("\n=== Fatoriais ===")
    for i in range(1, 8):
        print(f"{i}! = {calcular_fatorial(i)}")

    print("\n=== Sequência de Fibonacci (10 termos) ===")
    print(sequencia_fibonacci(10))

    print("\n=== Ordenação de Lista ===")
    lista_desordenada = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original: {lista_desordenada}")
    print(f"Ordenada: {ordenar_lista(lista_desordenada.copy())}")

    print("\n=== Cálculo de Média ===")
    notas_aluno = [8.5, 7.0, 9.5, 6.0, 8.0]
    media = calcular_media(notas_aluno)
    situacao = "Aprovado" if media >= 6.0 else "Reprovado"
    print(f"Notas: {notas_aluno}")
    print(f"Média: {media:.2f} - {situacao}")
