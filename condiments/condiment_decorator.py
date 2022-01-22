"""Condiment decorator abstract class"""
from abc import abstractmethod

from beverages.beverage import Beverage
from size.size import Size


class CondimentDecorator(Beverage):
    """Condiment decorator abstract class"""

    def __init__(self, beverage) -> None:
        self.beverage: Beverage = beverage

    def get_size(self) -> Size:
        """Get size

        Returns:
            Size: beverage size
        """
        return self.beverage.get_size()

    @abstractmethod
    def get_description(self):
        """Get description"""
