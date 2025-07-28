# This is the class that can store the data of positions
class PositionData:
    position: list[int]

    def __init__(self, position: list[int]):
        self.position = position



# This is the board data of a moment in game
class BoardData:
    xList: list[PositionData]
    oList: list[PositionData]

    followedRules: bool

    win: bool
    draw: bool
    playedFull: bool
    allPlacements: list[PositionData] = []
    for _ in range(0, 1):
        for x in range(1, 4):
            for y in range(1, 4):
                s = PositionData(position=[])
                s.position = [x, y]
                allPlacements.append(s)


    def __init__(self,
                 xList: list[PositionData],
                 oList: list[PositionData],
                 followedRules: bool, win: bool, draw: bool,
                 playedFull: bool):
        self.xList = xList
        self.oList = oList
        self.followedRules = followedRules
        self.win = win
        self.draw = draw
        self.playedFull = playedFull


# This is the list that stores all the board data instances.
boardList: list[BoardData] = []