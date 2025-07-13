# kendall_correlation(x, y)
def kendall_correlation(x, y):
    """Calcula la correlación de Kendall Tau entre dos listas x e y."""
    n = len(x)
    if n != len(y):
        raise ValueError("Las listas deben tener la misma longitud.")

    concordant = discordant = 0

    for i in range(n):
        for j in range(i + 1, n):
            a = x[i] - x[j]
            b = y[i] - y[j]
            prod = a * b
            if prod > 0:
                concordant += 1
            elif prod < 0:
                discordant += 1
            # Si hay empate (prod == 0), no se cuenta

    total_pairs = n * (n - 1) / 2
    return (concordant - discordant) / total_pairs if total_pairs != 0 else 0
