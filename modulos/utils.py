# Funcion auxiliar: rank (necesaria para spearman)
def rank(data):
    """Devuelve los rangos (posiciones relativas) de una lista, con corrección para empates."""
    sorted_data = sorted((val, idx) for idx, val in enumerate(data))
    ranks = [0] * len(data)

    i = 0
    while i < len(sorted_data):
        val = sorted_data[i][0]
        j = i
        while j < len(sorted_data) and sorted_data[j][0] == val:
            j += 1
        avg_rank = (i + j - 1) / 2 + 1  # Rango medio para empates
        for k in range(i, j):
            idx = sorted_data[k][1]
            ranks[idx] = avg_rank
        i = j
    return ranks
