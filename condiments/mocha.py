"""Mocha concrete condiment decorator class"""
from condiments.condiment_decorator import CondimentDecorator


class Mocha(CondimentDecorator):
    """Mocha concrete condiment decorator class"""

    def get_description(self):
        """Get description"""
        return f"{self.beverage.get_description()}, Mocha"

    def cost(self) -> float:
        """Compute beverage cost"""
        return self.beverage.cost() + 0.20
