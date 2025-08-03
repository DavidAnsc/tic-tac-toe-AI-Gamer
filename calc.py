from dependencies import *

# This is the place that I will store all calculation-related functions. And no direct expression in this file. Only functions

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

        boardList2[index].oList.append(v)

        for y in BoardData.allPlacements:
            if not y == v and len(boardList2[index].oList) == 1:
                oItem = y
                boardList2[index].oList.append(oItem)
                for u in BoardData.allPlacements:
                    if not u == v and not u == oItem and len(boardList2[index].xList) == 0:
                        boardList2[index].xList.append(u)
                    elif len(boardList2[index].xList) > 0 and not u == v and not u == oItem:
                        index += 1
                        boardList2[index].oList.append(v)

                        boardList2[index].oList.append(y)

                        boardList2[index].xList.append(u)
            elif not y == v and len(boardList2[index].oList) > 1:
                index += 1

                boardList2[index].oList.append(v)

                boardList2[index].oList.append(y)

                for u in BoardData.allPlacements:
                    if not u == v and not u == y and len(boardList2[index].xList) == 0:
                        boardList2[index].xList.append(u)
                    elif len(boardList2[index].xList) > 0 and not u == v and not u == y:
                        index += 1
                        boardList2[index].oList.append(v)

                        boardList2[index].oList.append(y)

                        boardList2[index].xList.append(u)
            else:
                xItem = PositionData(position=[-1, -1])
                # ☝️ is the "2" part.


def twoTwoBoardList():
    index = -1
    for v in BoardData.allPlacements:
        index = index + 1

        boardList3[index].oList.append(v)

        for p in BoardData.allPlacements:
            if not p == v and len(boardList3[index].oList) == 1:
                boardList3[index].oList.append(p)
                for c in BoardData.allPlacements:
                    if len(boardList3[index].xList) == 0 and c != p and c != v:
                        boardList3[index].xList.append(c)

                        for d in BoardData.allPlacements:
                            if len(boardList3[index].xList) == 1 and not d == p and not d == v and not d == c:
                                boardList3[index].xList.append(d)
                            elif len(boardList3[index].xList) > 1 and not d == p and not d == v and not d == c:
                                index += 1
                                boardList3[index].oList.append(v)
                                boardList3[index].oList.append(p)

                                boardList3[index].xList.append(c)
                                boardList3[index].xList.append(d)
                    elif len(boardList3[index].xList) > 0 and not c == p and not c == v:
                        index += 1
                        boardList3[index].oList.append(v)
                        boardList3[index].oList.append(p)

                        boardList3[index].xList.append(c)

                        for d in BoardData.allPlacements:
                            if len(boardList3[index].xList) == 1 and not d == p and not d == v and not d == c:
                                boardList3[index].xList.append(d)
                            elif len(boardList3[index].xList) > 1 and not d == p and not d == v and not d == c:
                                index += 1
                                boardList3[index].oList.append(v)
                                boardList3[index].oList.append(p)

                                boardList3[index].xList.append(c)
                                boardList3[index].xList.append(d)

            elif not p == v and len(boardList3[index].oList) > 1:
                index += 1

                oItem = v
                boardList3[index].oList.append(oItem)

                oItem = p
                boardList3[index].oList.append(oItem)

                for c in BoardData.allPlacements:
                    if len(boardList3[index].xList) == 0 and not c == p and not c == v:
                        boardList3[index].xList.append(c)

                        for d in BoardData.allPlacements:
                            if len(boardList3[index].xList) == 1 and not d == p and not d == v and not d == c:
                                boardList3[index].xList.append(d)
                            elif len(boardList3[index].xList) > 1 and not d == p and not d == v and not d == c:
                                index += 1
                                boardList3[index].oList.append(v)
                                boardList3[index].oList.append(p)

                                boardList3[index].xList.append(c)
                                boardList3[index].xList.append(d)
                    elif len(boardList3[index].xList) > 0 and not c == p and not c == v:
                        index += 1
                        boardList3[index].oList.append(v)
                        boardList3[index].oList.append(p)

                        boardList3[index].xList.append(c)

                        for d in BoardData.allPlacements:
                            if len(boardList3[index].xList) == 1 and not d == p and not d == v and not d == c:
                                boardList3[index].xList.append(d)
                            elif len(boardList3[index].xList) > 1 and not d == p and not d == v and not d == c:
                                index += 1
                                boardList3[index].oList.append(v)
                                boardList3[index].oList.append(p)

                                boardList3[index].xList.append(c)
                                boardList3[index].xList.append(d)


def sortList(list6: list[BoardData]):
    # Tested:
    for x in list6:
        x.oList.sort()
        x.xList.sort()
    # Until here


def removeDupl(list5: list[BoardData]):
    deletionList = {}
    duplicate = 0
    for i, u in enumerate(list5):
        duplicate = 0
        for index, l in enumerate(list5):
            if index != i and u.oList == l.oList and u.xList == l.xList and not l in deletionList.keys():
                duplicate += 1
                deletionList.update({u:duplicate})


    for o in deletionList:
        for _ in range(0, list5.count(o)):
            list5.remove(o)