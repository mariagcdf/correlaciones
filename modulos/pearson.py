# pearson_correlation(x, y)
def pearson_correlation(x, y):
    """Calcula la correlación de Pearson entre dos listas x e y."""
    n = len(x)
    if n != len(y) or n == 0:
        raise ValueError("Las listas deben tener la misma longitud y no estar vacías.")
    
    mean_x = sum(x) / n
    mean_y = sum(y) / n

    num = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
    den_x = sum((x[i] - mean_x) ** 2 for i in range(n)) ** 0.5
    den_y = sum((y[i] - mean_y) ** 2 for i in range(n)) ** 0.5

    return num / (den_x * den_y) if den_x and den_y else 0
