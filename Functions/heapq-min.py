import heapq

'''
힙 기능을 위해 heapq 라이브러리를 사용한다.
heapq는 다익스트라 최단 경로 알고리즘  + 우선순위 큐 기능 구현
보통 최소 힙 자료구조의 최상단 원소는 항상 '가장 작은' 원소이기 떄문에 오름차순 정렬이 돤료된다.
원소 삽입 : heapq.heappush()
원소 빼기 : heapq.heappop()
'''


def heapsort(iterable):
    h = []
    result = []

    # 모든 원소를 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)  # h 리스트에 value를 힙 구조로 추가하기 => 자동으로 최소 힙 구조를 유지함.

    # 힙에 삽입된(정렬된) 원소를 차례대로 꺼내어 담기
    for _ in range(len(h)):  # 변수를 쓰지 않을 때 '_' 라고 표시함. 단순히 len(h)만큼만 반복하면 되기 떄문!
        result.append(heapq.heappop(h))
    return result


result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)
