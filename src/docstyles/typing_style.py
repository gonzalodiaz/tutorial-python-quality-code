class World:
    """Class to contain the properties of the World.
    
    :param yearly_population: World's population by year

    :ivar yearly_population: Internal attribute to hold the world population.
    """

    def __init__(self, yearly_population: dict):
        self.yearly_population: dict = yearly_population

    def population(self, year: int) -> int:
        """Obtain the population in the world for a given year.

        :param year: Year of which the population wants to be known.

        :returns: Population for that year. 0 if the year was not found.
        """
        return self.yearly_population.get(year, 0)

    def population_on_2020(self) -> int:
        """Obtain the population for 2020.

        :returns: population for the year 2020.
        """
        return self.population(2020)
