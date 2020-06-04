class World:
    """Class to contain the properties of the World.
    
    :param yearly_population: World's population by year
    :type arg: dict

    :ivar yearly_population: Internal attribute to hold the world population.
    :vartype yearly_population: dict
    """

    def __init__(self, yearly_population):
        self.yearly_population = yearly_population

    def population(self, year):
        """Obtain the population in the world for a given year.

        :param year: Year of which the population wants to be known.
        :type year: int

        :returns: Population for that year. 0 if the year was not found.
        :rtype: int 
        """
        return self.yearly_population.get(year, 0)
