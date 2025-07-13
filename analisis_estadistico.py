import os
import pandas as pd
import numpy as np

def evaluar_matriz(matriz):
    # Eliminar diagonal (autocorrelaciones)
    sin_diag = matriz.values.copy()
    np.fill_diagonal(sin_diag, np.nan)
    return np.nanmean(np.abs(sin_diag))  # media del valor absoluto fuera de la diagonal

def comparar_matrices(carpeta='resultados'):
    archivos = {
        'Pearson': 'correlacion_pearson.csv',
        'Spearman': 'correlacion_spearman.csv',
        'Kendall': 'correlacion_kendall.csv'
    }

    resultados = {}

    for nombre, archivo in archivos.items():
        ruta = os.path.join(carpeta, archivo)
        if not os.path.exists(ruta):
            print(f"❌ No se encuentra: {ruta}")
            continue
        df = pd.read_csv(ruta, index_col=0)
        score = evaluar_matriz(df)
        resultados[nombre] = score
        print(f"🔍 {nombre}: media abs(correlaciones fuera de diagonal) = {score:.4f}")

    if resultados:
        mejor = max(resultados, key=resultados.get)
        print(f"\n✅ La matriz con mayor estructura (según esta métrica) es: **{mejor}**")

# Ejecutar comparación
comparar_matrices(carpeta='resultados')  # ajusta si están en otra carpeta
