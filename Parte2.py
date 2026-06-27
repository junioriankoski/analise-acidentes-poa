# PARTE 2 — TRATAMENTO E PREPARAÇÃO DOS DADOS
from dados import df, df_tratado, pd

df_tratado['data'] = pd.to_datetime(df_tratado['data'], errors='coerce')
df_tratado['data_extracao'] = pd.to_datetime(df_tratado['data_extracao'],errors='coerce')

# As colunas 'data' e 'data_extracao' estavam armazenadas como texto. A conversão para o tipo datetime
# permite realizar operações temporais, como filtrar por ano ou mês.

df_tratado['ano'] = df_tratado['data'].dt.year
df_tratado['mes'] = df_tratado['data'].dt.month

# Foram extraídas as informações de ano e mês a partir da coluna 'data',
# criando novas colunas que facilitarão análises temporais nas próximas etapas.

df_tratado['hora_int'] = df_tratado['hora'].str[:2].astype(float)

# A coluna 'hora' estava no formato de texto "19:00:00.0000000". Foram extraídos apenas
# os dois primeiros caracteres para obter a hora inteira como valor numérico.
# Os 629 registros sem hora registrada receberam NaN automaticamente.