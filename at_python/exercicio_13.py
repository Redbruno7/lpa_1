# TECNÓLOGO DE ANÁLISE E DESENVOLVIMENTO DE SISTEMAS
# LÓGICA DE PROGRAMAÇÃO E ALGORITMOS 1
# ALUNO: BRUNO C. RODGERS
# DATA: 2024, 2º SEMESTRE

import os


os.system('cls')

# Título
print('=' * 70)
print('EXERCÍCIO 13 - ANÁLISE DE IDADE E PESO')
print('=' * 70)

# Entrada contadores
contador_peso = 0
soma_idade = 0
total_pessoas = 7

# Iteração 7 pessoas
for i in range(1, total_pessoas + 1):
    print()
    print('=' * 70)
    print(f'Dados pessoa {i}:')
    print('=' * 70)
    
    # Validação de idade
    while True:
        idade = int(input('Digite a idade: '))
        print('-' * 70)
        if idade > 0:
            break
        else:
            print('Idade inválida! Insira um valor positivo.')
            print('-' * 70)

    # Validação de peso
    while True:
        peso = float(input('Digite o peso em quilos: '))
        print('=' * 70)
        if peso > 0:
            break
        else:
            print('Peso inválido! Insira um valor positivo.')
            print('-' * 70)
    
    # Contagem para peso > 90 kg
    if peso > 90:
        contador_peso += 1

    # Soma das idades
    soma_idade += idade

# Média das idades
media_idade = soma_idade / total_pessoas

# Saída
print()
print('=' * 70)
print('Resultados: ')
print('=' * 70)
print(f'Quantidade de pessoas com mais de 90 quilos: {contador_peso}')
print('-' * 70)
print(f'Média das idades: {media_idade:.0f} anos.')
print('=' * 70)
