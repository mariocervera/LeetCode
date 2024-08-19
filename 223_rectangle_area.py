
def get_rectangle_area(x1, y1, x2, y2):
    return (x2-x1) * (y2-y1)


def get_intersection_area(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    if ax2 <= bx1 or by2 <= ay1 or ay2 <= by1:
        return 0

    bottom_left = max(ax1, bx1), max(ay1, by1)
    top_right = min(ax2, bx2), min(ay2, by2)

    return get_rectangle_area(bottom_left[0], bottom_left[1], top_right[0], top_right[1])



def computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    if bx1 < ax1:
        ax1, ay1, ax2, ay2, bx1, by1, bx2, by2 = bx1, by1, bx2, by2, ax1, ay1, ax2, ay2

    rect_1_area = get_rectangle_area(ax1, ay1, ax2, ay2)
    rect_2_area = get_rectangle_area(bx1, by1, bx2, by2)

    intersection_area = get_intersection_area(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)

    return rect_1_area + rect_2_area - intersection_area



print(computeArea(ax1=-3, ay1=0, ax2=3, ay2=4, bx1=0, by1=-1, bx2=9, by2=2))  # 45
print(computeArea(ax1=-2, ay1=-2, ax2=2, ay2=2, bx1=-2, by1=-2, bx2=2, by2=2))  # 16
print(computeArea(ax1=-2, ay1=-2, ax2=2, ay2=2, bx1=-1, by1=-1, bx2=1, by2=1))  # 16
