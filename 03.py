import json
import pandas as pd

with open('dados.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

# Filtrar os valores que são maiores que zero
valores_validos = [registro['valor'] for registro in dados if registro['valor'] > 0]

# 1. Encontrar o menor valor de faturamento
menor_valor = min(valores_validos)

# 2. Encontrar o maior valor de faturamento
maior_valor = max(valores_validos)

# 3. Calcular a média mensal (excluindo dias com faturamento zero)
media = sum(valores_validos) / len(dados)

# 4. Contar o número de dias com faturamento acima da média
dias_acima_media = 0
for valor in valores_validos:
    if valor > media:
        dias_acima_media += 1


# Exibir os resultados
print(f"Menor valor de faturamento no mês: R${menor_valor:.2f}")
print(f"Maior valor de faturamento no mês: R${maior_valor:.2f}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_media}")
