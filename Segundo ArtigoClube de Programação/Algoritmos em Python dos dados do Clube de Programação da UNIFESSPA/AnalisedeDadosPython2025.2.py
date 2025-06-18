import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Estilo dos gráficos
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_context("notebook", font_scale=1.1)

# URLs dos dados
url_2025 = "https://raw.githubusercontent.com/ElsonJr01/AtividadesPythonDoZeroAbsoluto/refs/heads/main/Segundo%20ArtigoClube%20de%20Programa%C3%A7%C3%A3o/Inscri%C3%A7%C3%A3o%20Clube%20de%20Programa%C3%A7%C3%A3o%202025%20Dados%20Tratados.csv"
url_2024 = "https://raw.githubusercontent.com/ElsonJr01/AtividadesPythonDoZeroAbsoluto/refs/heads/main/Segundo%20ArtigoClube%20de%20Programa%C3%A7%C3%A3o/2024nscri%C3%A7%C3%A3o%20clube%20de%20programa%C3%A7%C3%A3o%202024%20(respostas).csv"

# Leitura dos arquivos
df_2025 = pd.read_csv(url_2025, sep=";", encoding="utf-8")
df_2024 = pd.read_csv(url_2024, sep=";", encoding="utf-8")

# Normalização do nome dos cursos
def normalizar_cursos(df):
    df["Curso"] = (
        df["Curso"]
        .astype(str)
        .str.lower()
        .str.strip()
        .str.replace(r"\s+", " ", regex=True)
        .str.title()
    )
    return df

df_2024 = normalizar_cursos(df_2024)
df_2025 = normalizar_cursos(df_2025)

# Adicionar coluna de ano
df_2024["Ano"] = "2024.1"
df_2025["Ano"] = "2025.2"

# Juntar os dois DataFrames
df_comparativo = pd.concat([df_2024[["Curso", "Ano"]], df_2025[["Curso", "Ano"]]], ignore_index=True)

# Gráfico comparativo por curso
plt.figure(figsize=(12, 6))
sns.countplot(data=df_comparativo, y="Curso", hue="Ano", palette="Set2", edgecolor="black")
plt.title("Inscrições por Curso em 2024.1 e 2025.2", fontsize=14, weight="bold")
plt.xlabel("Número de Inscritos")
plt.ylabel("Curso")
plt.legend(title="Período", loc='upper right')
plt.tight_layout()
plt.show()
