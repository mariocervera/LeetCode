
def update_balls(balls, ball, color):
    balls[ball] = color


def update_colors(colors, old_color, new_color):
    if old_color != new_color:
        colors[new_color] = colors.get(new_color, 0) + 1
        if old_color is not None:
            colors[old_color] -= 1
            if colors[old_color] == 0:
                del colors[old_color]

def queryResults(limit, queries):
    res = []
    balls, colors = {}, {}
    for ball, new_color in queries:
        old_color = balls[ball] if ball in balls else None
        update_balls(balls, ball, new_color)
        update_colors(colors, old_color, new_color)
        res.append(len(colors))
    return res


print(queryResults(limit=4, queries=[[1, 4], [2, 5], [1, 3], [3, 4]]))  # [1,2,2,3]
print(queryResults(limit=4, queries=[[0, 1], [1, 2], [2, 2], [3, 4], [4, 5]]))  # [1,2,2,3,4]
print(queryResults(limit=1, queries=[[0, 1], [1, 4], [1, 1], [1, 4], [1, 1]]))  # [1,2,1,2,1]
print(queryResults(limit=1, queries=[[0, 1], [0, 4], [0, 4], [0, 1], [1, 2]]))  # [1,1,1,1,2]
