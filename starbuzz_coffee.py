"""Main function"""
from beverages.beverage import Beverage
from beverages.dark_roast import DarkRoast
from beverages.espresso import Espresso
from beverages.house_blend import HouseBlend
from condiments.mocha import Mocha
from condiments.soy import Soy
from condiments.whip import Whip
from size.size import Size


def main() -> None:
    """Main function"""
    beverage = Espresso()
    print(f"{beverage.get_description()} ${beverage.cost()}")

    beverage2: Beverage = DarkRoast()
    beverage2 = Mocha(beverage2)
    beverage2 = Mocha(beverage2)
    beverage2 = Whip(beverage2)
    print(f"{beverage2.get_description()} ${beverage2.cost()}")

    beverage3: Beverage = HouseBlend()
    beverage3.set_size(size=Size.GRANDE)
    beverage3 = Soy(beverage3)
    beverage3 = Mocha(beverage3)
    beverage3 = Whip(beverage3)
    print(f"{beverage3.get_description()} ${beverage3.cost()}")


if __name__ == "__main__":
    main()
