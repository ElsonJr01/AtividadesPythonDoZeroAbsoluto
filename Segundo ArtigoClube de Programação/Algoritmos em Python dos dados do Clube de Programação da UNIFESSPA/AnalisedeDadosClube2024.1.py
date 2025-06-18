import pandas as pd
import matplotlib.pyplot as plt
from itertools import combinations
from collections import Counter

# Leitura do CSV
url = "https://raw.githubusercontent.com/ElsonJr01/AtividadesPythonDoZeroAbsoluto/refs/heads/main/Segundo%20ArtigoClube%20de%20Programa%C3%A7%C3%A3o/200000nscri%C3%A7%C3%A3o%20nas%20oficinas%20do%20clube%20de%20programa%C3%A7%C3%A3o%20(respostas).xlsx%20-%20Respostas%20ao%20formul%C3%A1rio%201.csv"
df_raw = pd.read_csv(url, sep='\t')

# Adiciona identificador de aluno
df_raw["AlunoID"] = df_raw.index

# Isola colunas de oficinas (ignorando "Nome completo")
colunas_oficinas = [col for col in df_raw.columns if col != "AlunoID" and "Nome completo" not in col]

# Formato long
df_melted = df_raw.melt(id_vars=["AlunoID"], value_vars=colunas_oficinas,
                        var_name="ColunaOriginal", value_name="Oficina")

# Limpeza
df_melted["Oficina"] = df_melted["Oficina"].astype(str).str.strip()
df_melted = df_melted[df_melted["Oficina"].str.lower().isin(["", "nan", "none"]) == False]

# Agrupar oficinas por aluno
df_grouped = df_melted.groupby("AlunoID")["Oficina"].apply(list)

# Contar pares de oficinas em comum
coocorrencias = Counter()
for oficinas in df_grouped:
    for par in combinations(sorted(set(oficinas)), 2):  # combinações únicas
        coocorrencias[par] += 1

# Converter em DataFrame e ordenar por frequência
df_coocorrencias = pd.DataFrame(coocorrencias.items(), columns=["Par", "Quantidade"])
df_coocorrencias["ParFormatado"] = df_coocorrencias["Par"].apply(lambda x: f"{x[0]} + {x[1]}")
df_top = df_coocorrencias.sort_values(by="Quantidade", ascending=False).head(10)

# Gráfico de barras
plt.figure(figsize=(10, 6))
plt.barh(df_top["ParFormatado"], df_top["Quantidade"], color="skyblue")
plt.xlabel("Número de alunos")
plt.title("Top 10 combinações de oficinas escolhidas em comum")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()
