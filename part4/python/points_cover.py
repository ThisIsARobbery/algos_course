
def pointsCover(list_of_segments):
    num_of_points = 0
    result_points = []
    sorted_list = list_of_segments.copy()
    sorted_list.sort(key=lambda seg: seg[1])
    flag = False
    i = 0
    while i < len(sorted_list):
        if flag:
            break
        point = sorted_list[i][1]
        num_of_points += 1
        result_points.append(point)
        i += 1
        while i < len(sorted_list):
            if sorted_list[i][0] <= point <= sorted_list[i][1]:
                i += 1
            else: break

    print(num_of_points)
    for point in result_points:
        print(point, end=" ")

n_seg = int(input())
list_of_segments = []
for i in range(n_seg):
    input_str = input()
    left = int(input_str.split(" ")[0])
    right = int(input_str.split(" ")[1])
    list_of_segments.append([left, right])

pointsCover(list_of_segments)
