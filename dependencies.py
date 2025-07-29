# This is the class that can store the data types. And also no direct expression in the file, only declaration and functions.
class PositionData:
    position: list[int]

    def __init__(self, position: list[int]):
        self.position = position

    def __str__(self):
        return self.position

    def __lt__(self, other):
        index1 = self.position[0]
        index2 = other.position[0]

        return index1 < index2
    def __gt__(self, other):
        index1 = self.position[0]
        index2 = other.position[0]

        return index1 > index2


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

    def __str__(self):
        oListTemp = []
        xListTemp = []
        for o in self.oList:
            oListTemp.append(o.position)
        for x in self.xList:
            xListTemp.append(x.position)
        return f"oList: {oListTemp}, xList: {xListTemp}"


# This is the list that stores all the board data instances.
boardList: list[BoardData] = []
boardList2: list[BoardData] = []
boardList3: list[BoardData] = []
boardList4: list[BoardData] = []
boardList5: list[BoardData] = []

totalList = [boardList, boardList2, boardList3, boardList4, boardList5]

for m in totalList:
    for r in range(0, 1000):
        n = BoardData([], [], False, False, False, False)
        m.append(n)



