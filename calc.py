from dependencies import *

# This is the place that I will store all calculation-related functions. And no direct expression in this file. Only functions

def printInfo(list: list[BoardData]):
    # This function prints the count of oList & xList in a specific boardList, also gives a board count after all.
    count = 0
    xCount = 0
    oCount = 0
    for x in list:
        for i1, t in enumerate(x.oList):
            if i1 == 0:
                count += 1
            #     print(f"{count}: ", end="")
            #     print("oList: ", end="")
            # print(t)
            oCount += 1
        for i2, r in enumerate(x.xList):
            #     print("xList: ", end="")
            # print(r)
            xCount += 1

    print(f"The count before removing duplicates: o:{oCount}, x:{xCount} \nThe board count is: {count}")

def removeDupl():
    # This is the sorting code 👇🏿
    for x in boardList:
        x.oList.sort()
        x.xList.sort()
    for x in boardList2:
        x.oList.sort()
        x.xList.sort()

    # This is the removing code 👇🏿
    for i, x in enumerate(boardList):
        for i2, y in enumerate(boardList):
            if (not i == i2) and x == y:
                boardList.remove(x)
    for i, x in enumerate(boardList2):
        for i2, y in enumerate(boardList2):
            if i == i2 and x == y:
                boardList2.remove(x)


def oneOneBoardList():
    index = -1
    for v in BoardData.allPlacements:
        index = index + 1
        oItem = PositionData(position=v.position)

        boardList[index].oList.append(oItem)

        for y in BoardData.allPlacements:
            if (not y == v) and (len(boardList[index].oList) == len(boardList[index].xList) + 1):
                xItem = y
                boardList[index].xList.append(xItem)
            elif not len(boardList[index].xList) + 1 == len(boardList[index].oList) and not y == v:
                index += 1
                boardList[index].oList.append(v)

                xItem = y
                boardList[index].xList.append(xItem)
            else:
                # If there's an empty PositionData value, that's the one that didn't meet the requirements of the rules, you should delete them.
                xItem = PositionData([0, 0])
                boardList[index].oList.clear()
                boardList[index].xList.clear()
            # if xItem == [0, 0]:
            #     print("No data found")
            # else:
            #     print(oItem, xItem)


def twoOneBoardList():
    index = -1
    for v in BoardData.allPlacements:
        index = index + 1
        oItem = PositionData(position=v.position)

        boardList2[index].oList.append(oItem)

        for y in BoardData.allPlacements:
            if not y == v and len(boardList2[index].oList) == 1:
                oItem = y
                boardList2[index].oList.append(oItem)
                for u in BoardData.allPlacements:
                    if not u == v and not u == oItem and len(boardList2[index].xList) == 0:
                        xItem = u
                        boardList2[index].xList.append(xItem)
                    elif len(boardList2[index].xList) > 0 and not u == v and not u == oItem:
                        index += 1
                        oItem = v
                        boardList2[index].oList.append(oItem)

                        oItem = y
                        boardList2[index].oList.append(oItem)

                        xItem = u
                        boardList2[index].xList.append(xItem)
            elif not y == v and len(boardList2[index].oList) > 1:
                index += 1

                oItem = v
                boardList2[index].oList.append(oItem)

                oItem = y
                boardList2[index].oList.append(oItem)

                for u in BoardData.allPlacements:
                    if not u == v and not u == oItem and len(boardList2[index].xList) == 0:
                        boardList2[index].xList.append(u)
                    elif len(boardList2[index].xList) > 0 and not u == v and not u == oItem:
                        index += 1
                        oItem = v
                        boardList2[index].oList.append(oItem)

                        oItem = y
                        boardList2[index].oList.append(oItem)

                        xItem = u
                        boardList2[index].xList.append(xItem)
            else:
                xItem = PositionData(position=[-1, -1])
                # ☝️ is the "2" part.



twoOneBoardList()
print("Before removing duplicates:")
printInfo(list=boardList2)

removeDupl()

print("After removing duplicates:")
printInfo(list=boardList2)