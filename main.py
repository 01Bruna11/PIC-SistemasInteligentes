import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

# Carregar dados da planilha gerada para testes
file_path = "dados_teste.xlsx"  # Planilha de teste

df = pd.read_excel(file_path)

# Supondo que a coluna 'Fluxo_Valores' representa medições de produção
df = df[['Fluxo_Valores']].dropna()

# Aplicar Z-score para detecção de outliers
z_score = (df['Fluxo_Valores'] - df['Fluxo_Valores'].mean()) / df['Fluxo_Valores'].std()
df['Z_Score_Outlier'] = np.abs(z_score) > 3  # Outliers são valores acima de 3 desvios-padrão

# Aplicar Isolation Forest para detecção de anomalias
iso_forest = IsolationForest(contamination=0.02, random_state=42)
df['Isolation_Forest_Outlier'] = iso_forest.fit_predict(df[['Fluxo_Valores']]) == -1

# Criar gráficos antes e depois da correção
def plot_histogram(data, title, color):
    plt.figure(figsize=(10, 5))
    plt.hist(data, bins=50, alpha=0.7, color=color, edgecolor='black')
    plt.axvline(data.mean(), color='red', linestyle='dashed', linewidth=2, label='Média')
    plt.title(title)
    plt.xlabel('Valor Simulado')
    plt.ylabel('Frequência')
    plt.legend()
    plt.grid()
    plt.show()

# Gráfico antes da correção
plot_histogram(df['Fluxo_Valores'], 'Distribuição dos Dados - Antes da Correção', 'blue')

# Remover outliers detectados por ambos os métodos
df_corrigido = df[~df['Z_Score_Outlier'] & ~df['Isolation_Forest_Outlier']]

# Gráfico depois da correção
plot_histogram(df_corrigido['Fluxo_Valores'], 'Distribuição dos Dados - Depois da Correção', 'green')

# Estatísticas finais
num_outliers_zscore = df['Z_Score_Outlier'].sum()
num_outliers_if = df['Isolation_Forest_Outlier'].sum()
print(f'Número de outliers detectados pelo Z-score: {num_outliers_zscore}')
print(f'Número de outliers detectados pelo Isolation Forest: {num_outliers_if}')
print(f'Tamanho original dos dados: {len(df)}, Após correção: {len(df_corrigido)}')
