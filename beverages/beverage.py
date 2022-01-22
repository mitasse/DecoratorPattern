"""Beverage abstract class"""
from abc import ABC, abstractmethod

from size.size import Size


class Beverage(ABC):
    """Beverage abstract class"""

    size: Size = Size.TALL
    description: str = "Unknown Beverage"

    def get_description(self):
        """Get description"""
        return f"{self.get_size().name.capitalize()} {self.description}"

    def get_size(self) -> Size:
        """Get size

        Returns:
            Size: beverage size
        """
        return self.size

    def set_size(self, size: Size) -> None:
        """Set size"""
        self.size = size

    @abstractmethod
    def cost(self) -> float:
        """Compute beverage cost"""
