import os
import pandas as pd
import numpy as np

from modulos.pearson import pearson_correlation
from modulos.spearman import spearman_correlation
from modulos.kendall import kendall_correlation

# Leer archivos CSV exportados desde MATLAB
print("Leyendo archivos CSV...")
df_influent = pd.read_csv('data/Dyn_Influentav_p.csv')
df_effluent = pd.read_csv('data/Dyn_Effluentav_p.csv')

# Eliminar columna de tiempo (Time)
df_influent = df_influent.drop(columns=['Time'])
df_effluent = df_effluent.drop(columns=['Time'])

# Unir ambas matrices
df_all = pd.concat([df_influent, df_effluent], axis=1)
variables = df_all.columns.tolist()
n = len(variables)

# Inicializar matrices vacías
pearson_matrix = np.full((n, n), np.nan)
spearman_matrix = np.full((n, n), np.nan)
kendall_matrix = np.full((n, n), np.nan)

# Calcular correlaciones
print("Calculando matrices de correlación...")
for i in range(n):
    for j in range(i + 1):  # Triangular inferior
        xi = df_all.iloc[:, i].tolist()
        xj = df_all.iloc[:, j].tolist()

        pearson_matrix[i, j] = pearson_correlation(xi, xj)
        spearman_matrix[i, j] = spearman_correlation(xi, xj)
        kendall_matrix[i, j] = kendall_correlation(xi, xj)

print("¡Correlaciones calculadas!")

# Convertir a DataFrames para exportar
pearson_df = pd.DataFrame(pearson_matrix, index=variables, columns=variables)
spearman_df = pd.DataFrame(spearman_matrix, index=variables, columns=variables)
kendall_df = pd.DataFrame(kendall_matrix, index=variables, columns=variables)

#GUARDAR

# Crear carpeta si no existe
output_dir = "resultados"
os.makedirs(output_dir, exist_ok=True)

# Convertir a DataFrames
pearson_df = pd.DataFrame(pearson_matrix, index=variables, columns=variables)
spearman_df = pd.DataFrame(spearman_matrix, index=variables, columns=variables)
kendall_df = pd.DataFrame(kendall_matrix, index=variables, columns=variables)

# Guardar como CSV dentro de la carpeta 'resultados'
pearson_df.to_csv(os.path.join(output_dir, 'correlacion_pearson.csv'))
spearman_df.to_csv(os.path.join(output_dir, 'correlacion_spearman.csv'))
kendall_df.to_csv(os.path.join(output_dir, 'correlacion_kendall.csv'))

print("✅ Matrices exportadas a la carpeta 'resultados':")
print(f"- {os.path.join(output_dir, 'correlacion_pearson.csv')}")
print(f"- {os.path.join(output_dir, 'correlacion_spearman.csv')}")
print(f"- {os.path.join(output_dir, 'correlacion_kendall.csv')}")
