class Race:
    """
    A dictionary with keys of names corresponding to approximate time.
    if a runner expects to run in 20, 30, or 40 or less, their time equals the 
    respective number. If they expect to run in greater than 40, their time equals 50.

    Attributes
    runners: list of tuples of name and time.

    """
    runners: dict

    def __init__(self, runners: list[tuple]) -> None:
        """Initializes a new class Race, with attribute runners being a dictionary with
        keys equal to a runner's name.
        """
        runner = {}
        for person in runners:
            runner[person[0]] = person[1]
        self.runners = runner

    def speed_cat(self, time: int) -> list:
        """ returns a list of runners in a given category.
        """
        people = []
        for person in self.runners:
            if self.runners[person] == time:
                people.append(person)
        return people
    
    def time(self, runner: str) -> int:
        """If runner is registered, returns their speed category. Otherwise,
        returns negative 1."""
        if runner in self.runners:
            return self.runners[runner]
        return -1
    
    def register(self, runner: tuple) -> None:
        """Registers a new runner to the race."""
        self.runners[runner[0]] = runner[1]
    
    def newspeed(self, runner: tuple) -> None:
        """Updates the speed of a runner"""
        self.register(runner)


race = Race([('tom', 50), ('wen', 20), ('dave', 20)])
print(race.speed_cat(20))
race.register(('brad', 30))
print(race.time('brad'))
