from typing import List, Optional

class CocktailMaker:
    MIN_SIZE = 30
    MAX_SIZE = 500
    VALID_ICES = ('crushed', 'cubes')
    def __init__(self) -> None:
        self._counter = 0

    @property
    def cocktails_made(self) -> int:
        """Get number of cocktails made by this maker."""
        return self._counter

    def make_a_cocktail(self,
                        size: int,
                        /,
                        *,
                        basic_ing: str ='apple',
                        addons: Optional[List[str]] = None,
                        ices: Optional[str]=None,
                        sipper: bool = False
    ) -> str:
        """
        Args:
            Make a cocktail with given parameters.
            size (int) - must be as first
            basic_ing (str) - must be with name
            addons (list) - must be a list with names
            ices (str) - must be with name ('crushed', or 'cubes')
            sipper (bool) - must be True or False
        Returns:
            str: Describe prepared cocktail

        Raises:
            ValueError: If size is not between 30 and 500ml.
            ValueError: If ices type is valid
        """
        size, ices = self.check_size_and_ices(size, ices)
        return self.format_cocktail_desc(basic_ing, size, ices, sipper, addons)

    @staticmethod
    def check_size_and_ices(size: int,
                            ices: Optional[str] = None
                            )-> tuple[int, Optional[str]]:
        if not CocktailMaker.MIN_SIZE <= size <= CocktailMaker.MAX_SIZE:
            raise ValueError(f"Size must be between {CocktailMaker.MIN_SIZE} and {CocktailMaker.MAX_SIZE} ml")
        if ices and ices not in CocktailMaker.VALID_ICES:
            raise ValueError(f"Ices must be one of {CocktailMaker.VALID_ICES}")
        return size, ices


    def format_cocktail_desc(self,
                             basic_ing: str,
                             size: int,
                             ices: Optional[str] = None,
                             sipper: bool = True,
                             addons: Optional[list[str]] = None
                             ) -> str:
        self._counter += 1
        cocktail = f"Cocktail #{self._counter}: {basic_ing} of {size}ml"

        if sipper:
            cocktail += " in sipper"
        if ices:
            cocktail += f" with ices: {ices}"
        if addons:
            cocktail += f"\nAddons: {', '.join(addons)}"

        return cocktail + "\nGood appetite!\n"


def main():
    maker = CocktailMaker()
    print(maker.make_a_cocktail(100, basic_ing='apple', addons=['lemon', 'lime']))
    print(maker.make_a_cocktail(200, basic_ing='lemon'))
    print(maker.make_a_cocktail(300, basic_ing='lemon', addons=['lime', 'grape'], ices='crushed', sipper=True))
    print(f"\n{maker.cocktails_made} cocktails made")

if __name__ == "__main__":
    main()
