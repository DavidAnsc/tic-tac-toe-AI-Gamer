
# This is the class that can store the data types. And also no direct expression in the file, only declaration and functions.
class PositionData:
    position: list[int]

    def __init__(self, position: list[int]):
        self.position = position

    def __str__(self):
        return f"{self.position}"

    def __lt__(self, other):
        position1 = self.position
        position2 = other.position

        if position1[0] < position2[0]:
            return True
        elif position1[0] == position2[0]:
            if position1[1] < position2[1]:
                return True
            elif position1[1] == position2[1]:
                return False
            elif position1[1] > position2[1]:
                return False
            else:
                return False
        elif position1[0] > position2[0]:
            return False
        else:
            return False

    def __eq__(self, other):
        value1 = self.position
        value2 = other.position

        return value1 == value2


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

    def __hash__(self):
        o_tuple = tuple(sorted(tuple(p.position) for p in self.oList))
        x_tuple = tuple(sorted(tuple(p.position) for p in self.xList))
        return hash((o_tuple, x_tuple))



# This is the list that stores all the board data instances.
boardList: list[BoardData] = []
boardList2: list[BoardData] = []
boardList3: list[BoardData] = []
boardList4: list[BoardData] = []
boardList5: list[BoardData] = []

totalList = [boardList, boardList2, boardList3, boardList4, boardList5]

for m in totalList:
    if m == boardList3:
        for r in range(0, 3500):
            n = BoardData([], [], False, False, False, False)
            m.append(n)
    else:
        for r in range(0, 1000):
            n = BoardData([], [], False, False, False, False)
            m.append(n)



boardListTemp = [BoardData(xList=[PositionData(position=[2, 1]), PositionData(position=[1, 3])], oList=[], followedRules=False, win=False, draw=False, playedFull=False)]

def printInfo(mode: int, list: list[BoardData]):
    # This function prints the count of oList & xList in a specific boardList, also gives a board count after all.
    count = 0
    xCount = 0
    oCount = 0
    if mode == 1:
        for x in list:
            count += 1
            print(count, end=": ")
            for i1, t in enumerate(x.oList):
                if i1 == 0:
                    print(f"oList: {t}", end="")
                else:
                    print(t, end=", ")
                oCount += 1
            for i2, p in enumerate(x.xList):
                if i2 == 0:
                    print(f"xList: {p}", end=", ")
                else:
                    print(f"{p}", end=", ")
                xCount += 1
            print("")
    elif mode == 2:
        count = 0
        xCount = 0
        oCount = 0
        # for x in boardList3:
        #     x.oList.sort()
        #     x.xList.sort()
        for x in list:
            for i1, t in enumerate(x.oList):
                if i1 == 0:
                    count += 1
                    oCount += 1
                #     print(f"{count}: ", end="")
                #     print("oList: ", end="")
                # print(t)
                oCount += 1
            for i2, r in enumerate(x.xList):
                if i2 == 0:
                    xCount += 1
                #     print("xList: ", end="")
                # print(r)
                xCount += 1

    print(f"o:{oCount}, x:{xCount} \nThe board count is: {count}")
