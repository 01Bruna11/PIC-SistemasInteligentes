import pandas as pd
import numpy as np

# Gerar dados fictícios para simular um fluxo de valores na produção
np.random.seed(42)
dados = {
    "Fluxo_Valores": np.random.normal(loc=100000, scale=15000, size=100),  # Valores normais
    "Temperatura_Sensor": np.random.normal(loc=25, scale=5, size=100),  # Sensores de temperatura
    "Pressao_Sensor": np.random.normal(loc=5, scale=1, size=100),  # Pressão de sensores
}

# Criar DataFrame
df_teste = pd.DataFrame(dados)

# Adicionar alguns outliers para teste
df_teste.loc[5, "Fluxo_Valores"] = 200000  # Outlier alto
df_teste.loc[20, "Temperatura_Sensor"] = -10  # Outlier baixo
df_teste.loc[50, "Pressao_Sensor"] = 20  # Outlier alto

# Salvar como arquivo Excel
df_teste.to_excel("dados_teste.xlsx", index=False)

print("Planilha 'dados_teste.xlsx' criada com sucesso!")
