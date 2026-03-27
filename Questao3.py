import pandas as pd

dados_extraidos = {
    'id_processo': [101, 102, None, 104, 105],
    'valor_causa': ['R$ 1.500,00', '2000', 'R$ 350,50', '5000.00', None],
    'status': ['Ativo', 'encerrado', 'ATIVO', 'Arquivado', 'Ativo'],
    'estado': ['SP', 'RJ', 'sp', 'MG', 'SP']
}

df = pd.DataFrame(dados_extraidos)

dadosTratados = df[df['id_processo'].notna()]

print(dadosTratados)

df['status'] = df['status'].str.title()


print(df)


df['valor_causa'] = df['valor_causa'].astype(str)


df['valor_causa'] = df['valor_causa'].str.replace('R$', '', regex=False).str.strip()


df['valor_causa'] = df['valor_causa'].str.replace('.', '', regex=False)

df['valor_causa'] = df['valor_causa'].str.replace(',', '.', regex=False)

df['valor_causa'] = pd.to_numeric(df['valor_causa'], errors='coerce')

print(df['valor_causa'])