from .pearson import pearson_correlation
from .utils import rank

def spearman_correlation(x, y):
    """
    Calcula la correlación de Spearman entre dos listas de datos.
    Es equivalente a aplicar la correlación de Pearson sobre los rangos de los datos.
    
    Args:
        x (list or array-like): Primer conjunto de datos.
        y (list or array-like): Segundo conjunto de datos.
        
    Returns:
        float: Coeficiente de correlación de Spearman.
    """
    if len(x) != len(y):
        raise ValueError("Las listas deben tener la misma longitud.")
    
    rx = rank(x)
    ry = rank(y)
    
    return pearson_correlation(rx, ry)