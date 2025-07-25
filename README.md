# Análisis de Correlaciones – Datos de Aguas Residuales

## Acerca del proyecto

Este repositorio realiza un análisis de correlaciones de datos del tratamiento de aguas residuales utilizando los métodos de Pearson, Spearman y Kendall. Incluye la generación de mapas de calor y una comparación métrica entre los métodos. Los datos se exportan desde MATLAB (BSM2) en formato CSV y se guardan en la carpeta `data/`, desde donde son leídos por los módulos.

## Estructura del proyecto

```plaintext
correlaciones/
├── data/                  # Archivos CSV desde MATLAB (influyente y efluente)
├── resultados/            # Matrices de correlación en formato CSV
├── graficos/
│   └── YYYY-MM-DD/        # Imágenes de mapas de calor por fecha
├── modulos/               # Módulos en Python (Pearson, Spearman, Kendall, utils)
│   ├── pearson.py
│   ├── spearman.py
│   ├── kendall.py
│   └── utils.py
├── main.py                # Calcula las matrices de correlación
├── graficar_heatmaps.py   # Muestra/guarda mapas de calor
├── comparar_metricas.py   # Compara las matrices según estructura
└── README.md              # Descripción del proyecto
```

## Requisitos

Instala las dependencias (recomendado usar entorno virtual):

```bash
pip install pandas seaborn matplotlib numpy
```

## Cómo ejecutar

1. Exporta los datos desde MATLAB como `Dyn_Influentav_p.csv` y `Dyn_Effluentav_p.csv`, y colócalos en la carpeta `data/`.

2. Calcula las matrices de correlación:

```bash
python main.py
```

3. Genera y guarda los mapas de calor:

```bash
python graficar_heatmaps.py
```

4. Compara qué método de correlación captura mejor la estructura del sistema:

```bash
python comparar_metricas.py
```

## Salidas generadas

- CSVs de correlación → `resultados/`
- Mapas de calor (Pearson, Spearman, Kendall) → `graficos/YYYY-MM-DD/` (fecha del dia en el que se hicieron, puesta automaticamente por graficar_heatmaps.py)
- Comparativa impresa en terminal

---

📁 Desarrollado para el análisis estadístico de datos de influente/efluente del BSM2 en ingeniería ambiental.
```
