from collections import deque
from collections import Counter

def watchedVideosByFriends(watchedVideos, friends, id, level):
    q, visited = deque([id]), set([id])
    _level = -1
    people_at_level = None
    while q:
        _level += 1
        if _level == level:
            people_at_level = list(q)
            break
        for _ in range(len(q)):
            current_person = q.popleft()
            for friend in friends[current_person]:
                if friend not in visited:
                    q.append(friend)
                visited.add(friend)
    videos = []
    for person in people_at_level:
        videos.extend(watchedVideos[person])
    frequencies = list(Counter(videos).items())
    frequencies.sort(key=lambda t: (t[1], t[0]))
    return [video_id for video_id, freq in frequencies]


print(watchedVideosByFriends(watchedVideos=[["A", "B"], ["C"], ["B", "C"], ["D"]],
                             friends=[[1, 2], [0, 3], [0, 3], [1, 2]],
                             id=0,
                             level=1))  # ["B","C"]


print(watchedVideosByFriends(watchedVideos=[["A", "B"], ["C"], ["B", "C"], ["D"]],
                             friends=[[1, 2], [0, 3], [0, 3], [1, 2]],
                             id=0,
                             level=2))  # ["D"]
