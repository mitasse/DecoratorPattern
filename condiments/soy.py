"""Soy concrete condiment decorator class"""
from size.size import Size

from condiments.condiment_decorator import CondimentDecorator


class Soy(CondimentDecorator):
    """Soy concrete condiment decorator class"""

    def get_description(self):
        """Get description"""
        return f"{self.beverage.get_description()}, Soy"

    def cost(self) -> float:
        """Compute beverage cost"""
        if self.beverage.get_size() == Size.TALL:
            return self.beverage.cost() + 0.10

        if self.beverage.get_size() == Size.GRANDE:
            return self.beverage.cost() + 0.15

        return self.beverage.cost() + 0.20
