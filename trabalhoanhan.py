import matplotlib.pyplot as plt

# Criação do dicionário de vendas
vendas = {
    'João': 1500,
    'Maria': 2300,
    'Ana': 1800,
    'Pedro': 1200
}

# Separação de chaves e valores
nomes = list(vendas.keys())
valores = list(vendas.values())

# Criação do gráfico
plt.bar(nomes, valores, color='skyblue')
plt.title('Vendas por Vendedor')
plt.xlabel('Vendedor')
plt.ylabel('Valor de Vendas (R$)')
plt.grid(True)
plt.show()
