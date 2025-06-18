import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests
from io import StringIO


def carregar_dados(url):
    print(f"🔹 Fazendo o download dos dados...")
    response = requests.get(url)
    raw_text = response.text
    print("2. Dados brutos baixados.")
    return raw_text


def processar_dados(raw_text, coluna_oficinas, sep=','):
    df = pd.read_csv(StringIO(raw_text), sep=sep, on_bad_lines='skip')
    print(f"3. Colunas carregadas: {df.columns.tolist()}")

    if coluna_oficinas not in df.columns:
        raise ValueError(f"❌ Coluna '{coluna_oficinas}' não encontrada no CSV.")

    df[coluna_oficinas] = df[coluna_oficinas].astype(str)

    df_oficinas = df.dropna(subset=[coluna_oficinas]).copy()
    # Corrigindo warning do escape \s na regex
    df_oficinas[coluna_oficinas] = df_oficinas[coluna_oficinas].str.split(r',\s*', regex=True)
    df_oficinas = df_oficinas.explode(coluna_oficinas)
    df_oficinas[coluna_oficinas] = df_oficinas[coluna_oficinas].str.strip()

    print("5. Oficinas separadas e limpadas.")

    contagem = df_oficinas[coluna_oficinas].value_counts()
    print("6. Contagem de participantes por oficina feita:")
    print(contagem)
    return contagem


def plotar_graficos(contagem, ano):
    sns.set(style="whitegrid")

    df_contagem = contagem.reset_index()
    df_contagem.columns = ['Oficina', 'Quantidade']
    df_contagem = df_contagem.sort_values('Quantidade', ascending=False)

    plt.figure(figsize=(12, 7))
    sns.barplot(data=df_contagem, y='Oficina', x='Quantidade', palette='viridis')
    plt.title(f'Quantidade de Participantes por Oficina - {ano}', fontsize=16, fontweight='bold')
    plt.xlabel('Número de Participantes', fontsize=14)
    plt.ylabel('Oficina', fontsize=14)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 6))
    proporcoes = df_contagem['Quantidade'] / df_contagem['Quantidade'].sum()
    sns.barplot(x=proporcoes, y=df_contagem['Oficina'], palette='magma')
    plt.title(f'Proporção de Participantes por Oficina - {ano}', fontsize=16, fontweight='bold')
    plt.xlabel('Proporção')
    plt.ylabel('Oficina')
    plt.tight_layout()
    plt.show()


# URLs
url_2024 = "https://raw.githubusercontent.com/ElsonJr01/AtividadesPythonDoZeroAbsoluto/refs/heads/main/Segundo%20ArtigoClube%20de%20Programa%C3%A7%C3%A3o/2024nscri%C3%A7%C3%A3o%20clube%20de%20programa%C3%A7%C3%A3o%202024%20(respostas).csv"
url_2025 = "https://raw.githubusercontent.com/ElsonJr01/AtividadesPythonDoZeroAbsoluto/refs/heads/main/Segundo%20ArtigoClube%20de%20Programa%C3%A7%C3%A3o/Inscri%C3%A7%C3%A3o%20Clube%20de%20Programa%C3%A7%C3%A3o%202025%20Dados%20Tratados.csv"

try:
    print("🔹 Processando dados de 2024...")
    raw_2024 = carregar_dados(url_2024)
    # Note que o CSV de 2024 usa ; como separador e talvez a coluna correta seja diferente
    # Vou ajustar a coluna para o nome que aparece na tabela, ex: 'Oficinas' não existe, precisa conferir
    # Caso não tenha, você precisa me informar o nome exato da coluna das oficinas
    # Aqui vou tentar com "Oficinas" e se der erro você me avisa para ajustar.
    contagem_2024 = processar_dados(raw_2024, coluna_oficinas='Oficinas', sep=';')
    plotar_graficos(contagem_2024, "2024")
except Exception as e:
    print(f"❌ Erro ao carregar 2024: {e}")

try:
    print("🔹 Processando dados de 2025...")
    raw_2025 = carregar_dados(url_2025)
    contagem_2025 = processar_dados(raw_2025, coluna_oficinas='Oficinas', sep=',')
    plotar_graficos(contagem_2025, "2025")
except Exception as e:
    print(f"❌ Erro ao carregar 2025: {e}")

print("✅ Processamento concluído.")
