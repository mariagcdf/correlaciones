```markdown
# Correlation Analysis – Wastewater Data

## About

Correlation analysis of wastewater treatment data using Pearson, Spearman, and Kendall methods. Includes heatmaps and metric-based comparison. Data is exported from BSM2 MATLAB simulations.

## Project Structure

```plaintext
correlaciones/
├── data/                  # CSV files from MATLAB (influent and effluent)
├── resultados/            # CSV correlation matrices
├── graficos/
│   └── YYYY-MM-DD/        # Heatmap images by date
├── modulos/               # Python modules (Pearson, Spearman, Kendall, utils)
│   ├── pearson.py
│   ├── spearman.py
│   ├── kendall.py
│   └── utils.py
├── main.py                # Computes correlation matrices
├── graficar_heatmaps.py   # Shows/saves heatmaps
├── comparar_metricas.py   # Compares matrices based on correlation structure
└── README.md              # Project description
```

## Requirements

Install dependencies (use virtual environment if desired):

```bash
pip install pandas seaborn matplotlib numpy
```

## How to Run

1. Export the MATLAB data as `Dyn_Influentav_p.csv` and `Dyn_Effluentav_p.csv`, and place them in the `data/` folder.

2. Compute correlation matrices:

```bash
python main.py
```

3. Generate and save heatmaps:

```bash
python graficar_heatmaps.py
```

4. Compare which correlation method captures the strongest structure:

```bash
python comparar_metricas.py
```

## Output

- Correlation CSVs → `resultados/`
- Heatmaps (Pearson, Spearman, Kendall) → `graficos/YYYY-MM-DD/`
- Printed comparison summary in terminal

---

📁 Developed for the statistical exploration of BSM2 influent/effluent data in environmental engineering workflows.
```
