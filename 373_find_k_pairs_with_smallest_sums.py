import heapq

def kSmallestPairs(nums1, nums2, k):

    def insert_in_priority_queue(i, j):
        if i < len(nums1) and j < len(nums2):
            heapq.heappush(pq, (nums1[i] + nums2[j], i, j))

    pq = []
    insert_in_priority_queue(0, 0)
    pairs = []
    while pq and len(pairs) < k:
        _, i, j = heapq.heappop(pq)
        pairs.append([nums1[i], nums2[j]])
        insert_in_priority_queue(i, j + 1)
        if j == 0:
            insert_in_priority_queue(i + 1, 0)
    return pairs



print(kSmallestPairs(nums1=[1, 7, 11], nums2=[2, 4, 6], k=3))  # [[1,2],[1,4],[1,6]]
print(kSmallestPairs(nums1=[1, 1, 2], nums2=[1, 2, 3], k=2))  # [[1,1],[1,1]]
print(kSmallestPairs(nums1=[1, 2], nums2=[3], k=3))  # [[1,3],[2,3]]
