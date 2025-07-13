import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime

def mostrar_heatmaps_juntos(carpeta='resultados', guardar=False):
    # Archivos y títulos
    graficos = [
        ('correlacion_pearson.csv',  'Pearson'),
        ('correlacion_spearman.csv', 'Spearman'),
        ('correlacion_kendall.csv',  'Kendall'),
    ]

    # Crear figura grande para que los números quepan bien
    fig, axes = plt.subplots(1, 3, figsize=(30, 10))

    for i, (archivo, titulo) in enumerate(graficos):
        ruta_csv = os.path.join(carpeta, archivo)
        if not os.path.exists(ruta_csv):
            raise FileNotFoundError(f"❌ No se encuentra: {ruta_csv}")
        matriz = pd.read_csv(ruta_csv, index_col=0)

        sns.heatmap(
            matriz,
            annot=True,
            fmt=".2f",
            cmap='coolwarm',
            vmin=-1,
            vmax=1,
            linewidths=0.5,
            linecolor='grey',
            cbar_kws={"shrink": 0.8},
            annot_kws={"size": 9},  # Tamaño del texto dentro de cada celda
            ax=axes[i]
        )

        axes[i].set_title(f'Correlación de {titulo}', fontsize=14)
        axes[i].tick_params(axis='x', rotation=45)
        axes[i].tick_params(axis='y', rotation=0)

    plt.tight_layout(pad=4.0)  # Espacio entre subplots

    if guardar:
        fecha = datetime.now().strftime('%Y-%m-%d')
        carpeta_salida = os.path.join("graficos", fecha)
        os.makedirs(carpeta_salida, exist_ok=True)
        nombre_archivo = os.path.join(carpeta_salida, "correlaciones_heatmaps.png")
        plt.savefig(nombre_archivo, dpi=300)
        print(f"✅ Figura guardada en: {nombre_archivo}")
    else:
        plt.show()

# Ejecutar (ajusta 'guardar=True' si quieres guardar la figura)
mostrar_heatmaps_juntos(guardar=True)
