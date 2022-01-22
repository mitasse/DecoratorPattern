"""Espresso concrete beverage class"""
from beverages.beverage import Beverage


class Espresso(Beverage):
    """Espresso concrete beverage class"""

    description: str = "Espresso"

    def cost(self) -> float:
        """Compute beverage cost"""
        return 1.99
