import matplotlib.pyplot as plt

# Dados fictícios simulando os resultados da análise

# 1. Frequência por tipo de acidente
tipos_acidente = ['Colisão Traseira', 'Colisão Lateral', 'Atropelamento', 'Capotamento', 'Queda de Motocicleta']
frequencias = [3200, 2400, 800, 500, 1500]

plt.figure(figsize=(10, 6))
plt.bar(tipos_acidente, frequencias, color='skyblue')
plt.title('Frequência por Tipo de Acidente')
plt.xlabel('Tipo de Acidente')
plt.ylabel('Número de Acidentes')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. Proporção de acidentes por gravidade
gravidade = ['Sem vítimas', 'Feridos', 'Fatais']
valores = [6000, 2500, 300]

plt.figure(figsize=(6, 6))
plt.pie(valores, labels=gravidade, autopct='%1.1f%%', colors=['lightgreen', 'orange', 'red'], startangle=140)
plt.title('Proporção de Acidentes por Gravidade')
plt.show()

# 3. Acidentes por condição climática
clima = ['Céu claro', 'Chuva', 'Nublado', 'Nevoeiro']
quantidade = [5000, 2200, 1000, 300]

plt.figure(figsize=(8, 5))
plt.bar(clima, quantidade, color='lightblue')
plt.title('Acidentes por Condição Climática')
plt.xlabel('Condição Climática')
plt.ylabel('Número de Acidentes')
plt.tight_layout()
plt.show()

# 4. Acidentes por horário
horarios = ['Manhã', 'Tarde', 'Noite', 'Madrugada']
acidentes_por_turno = [2000, 3500, 2800, 700]

plt.figure(figsize=(8, 5))
plt.plot(horarios, acidentes_por_turno, marker='o', linestyle='-', color='purple')
plt.title('Distribuição de Acidentes por Horário')
plt.xlabel('Horário do Dia')
plt.ylabel('Número de Acidentes')
plt.grid(True)
plt.tight_layout()
plt.show()

# 5. Tipo de pista e gravidade
tipos_pista = ['Simples', 'Dupla']
fatais = [220, 80]
feridos = [1200, 600]

plt.figure(figsize=(8, 5))
bar1 = plt.bar(tipos_pista, fatais, label='Fatais', color='red')
bar2 = plt.bar(tipos_pista, feridos, bottom=fatais, label='Feridos', color='orange')

plt.title('Gravidade dos Acidentes por Tipo de Pista')
plt.xlabel('Tipo de Pista')
plt.ylabel('Número de Vítimas')
plt.legend()
plt.tight_layout()
plt.show()
