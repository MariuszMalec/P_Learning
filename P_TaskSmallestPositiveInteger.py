def solution(listaInt):
    result = 0
    sortedList = sorted(listaInt)
    removeDuplicate = list(dict.fromkeys(sortedList))

    if all(x < 0 for x in removeDuplicate):
        return 1

    positiveList = [x for x in removeDuplicate if x >= 0]

    maxValue = max(positiveList)
    for i in range(1, maxValue + 1):
        if i in positiveList:
            result = result + 1
        if not i in positiveList:
            result = result + 1
            break
        if i == maxValue:
            result = result + 1

    return result


A = [1, 3, 6, 4, 1, 2]  # result 5
B = [-1, -3]  # result 1
C = [1, 2, 3]  # result 4
D = [-1, -3, 0, 1, 3, 4, 6]  # result 2

print(solution(C))
