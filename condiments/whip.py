"""Whip concrete condiment decorator class"""
from condiments.condiment_decorator import CondimentDecorator


class Whip(CondimentDecorator):
    """Whip concrete condiment decorator class"""

    def get_description(self):
        """Get description"""
        return f"{self.beverage.get_description()}, Whip"

    def cost(self) -> float:
        """Compute beverage cost"""
        return self.beverage.cost() + 0.10
