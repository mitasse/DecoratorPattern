"""Dark roast concrete beverage class"""
from beverages.beverage import Beverage


class DarkRoast(Beverage):
    """DarkRoast concrete beverage class"""

    description: str = "Dark Roast Coffee"

    def cost(self) -> float:
        """Compute beverage cost"""
        return 0.99
