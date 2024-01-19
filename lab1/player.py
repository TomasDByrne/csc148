class Player:
    """
    A player is a class with two attirbutes, a name and a list corresponding to
    their previous scores.

    Attribute
    name: str
    scores: list[int]

    >>>guy = Player('tom', [1, 2, 3, 3, 3])
    >>>guy.average(3)
    3
    >>>guy.best()
    3
    """
    name: str
    games: list[int]

    def __init__(self, name: str, games: list[int]) -> None:
        """Initialize a new player, including both their name and game history
        """
        
        self.name = name
        self.games = games
    

    def newscores(self, newgames: list[int]) -> None:
        """ Adds the scores in newgames to the end of self.games.
        """
        self.games.extend(newgames)

    def average(self, n: int) -> float:
        """Returns the average score of the last n games in self.games,
        or -1 if this would produce an error. 
        """
        if 0 < n < len(self.games):
            av = 0
            for i in range(len(self.games) - n, len(self.games)):
                av += self.games[i]
            return av / n
        else:
            return -1

    def best(self) -> int:
        """returns the highest score in self.games.
        """
        best = -1
        for score in self.games:
            if score > best:
                best = score
        return best

