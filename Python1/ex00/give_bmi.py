import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    """
    Calcule l'IMC (Indice de Masse Corporelle) pour une liste de tailles et de poids donnés.

    Args:
        height (list[int | float]): Liste des tailles en mètres.
        weight (list[int | float]): Liste des poids en kilogrammes.

    Returns:
        list[int | float]: Liste des valeurs d'IMC correspondantes.
    """
    bmi = np.array(weight) / np.array(height) ** 2
    return bmi.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Applique une limite supérieure aux valeurs d'IMC pour déterminer si elles dépassent cette limite.

    Args:
        bmi (list[int | float]): Liste des valeurs d'IMC.
        limit (int): Valeur limite d'IMC.

    Returns:
        list[bool]: Liste indiquant pour chaque valeur d'IMC si elle dépasse la limite (True) ou non (False).
    """
    return (np.array(bmi) > limit).tolist()
