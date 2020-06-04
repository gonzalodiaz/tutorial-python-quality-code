class World:
    """Class to contain the properties of the World.
    
    Parameters
    ----------
    yearly_population : dict
        World's population by year

    Attributes
    ----------
    yearly_population :dict
        Internal attribute to hold the world population.
    """

    def __init__(self, yearly_population):
        self.yearly_population = yearly_population

    def population(self, year):
        """Obtain the population in the world for a given year.

        Parameters
        ----------
        year : int
            Year of which the population wants to be known.

        Returns
        -------
        Population for that year. 0 if the year was not found.
        """
        return self.yearly_population.get(year, 0)
