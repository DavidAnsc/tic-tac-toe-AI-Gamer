from dependencies import *

# This is the place that I will store all calculation-related functions. And no direct expression in this file. Only functions

def oneOneBoardList():
    index = -1
    for x in BoardData.allPlacements:
        index = index + 1
        oItem = PositionData(position=x.position)

        boardList[index].oList.append(oItem)

        for y in BoardData.allPlacements:
            if (not y == x) and (len(boardList[index].oList) == len(boardList[index].xList) + 1):
                xItem = y
                boardList[index].xList.append(xItem)
            elif not len(boardList[index].xList) + 1 == len(boardList[index].oList) and not y == x:
                index += 1
                boardList[index].oList.append(x)

                xItem = y
                boardList[index].xList.append(xItem)
            else:
                # If there's an empty PositionData value, that's the one that didn't meet the requirements of the rules, you should delete them.
                xItem = PositionData([0, 0])
                boardList[index].oList.clear()
                boardList[index].xList.clear()
            if xItem.position == [0, 0]:
                print("No data found")
            else:
                print(oItem.position, xItem.position)


def oneTwoBoardList():
