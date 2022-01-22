"""House blend coffee concrete beverage class"""
from beverages.beverage import Beverage


class HouseBlend(Beverage):
    """House blend concrete beverage class"""

    description: str = "House Blend Coffee"

    def cost(self) -> float:
        """Compute beverage cost"""
        return 0.89
