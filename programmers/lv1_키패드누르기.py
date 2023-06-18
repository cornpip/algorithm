left_col = [1, 4, 7]
right_col = [3, 6, 9]

number_map = {
    0: [3, 1],
    1: [0, 0],
    2: [0, 1],
    3: [0, 2],
    4: [1, 0],
    5: [1, 1],
    6: [1, 2],
    7: [2, 0],
    8: [2, 1],
    9: [2, 2],
}

def distance(list1, list2):
    return abs(list1[0] - list2[0]) + abs(list1[1] - list2[1])

def solution(numbers, hand):
    answer = ""
    left_xy = [3, 0]
    right_xy = [3, 2]

    for num in numbers:
        target = number_map.get(num, False)
        if (num in left_col):
            left_xy = target
            answer += "L"
        elif (num in right_col):
            right_xy = target
            answer += "R"
        else:
            left_dist = distance(left_xy, target)
            right_dist = distance(right_xy, target)

            # print(answer, target, left_xy, right_xy, left_dist, right_dist)
            if left_dist == right_dist:
                if hand == "right":
                    right_xy = target
                    answer += "R"
                else:
                    left_xy = target
                    answer += "L"
            else:
                if right_dist < left_dist:
                    right_xy = target
                    answer += "R"
                else:
                    left_xy = target
                    answer += "L"

    return answer
