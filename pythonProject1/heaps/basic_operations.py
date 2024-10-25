from heapq import heappush, heappop, heapify

if __name__ == "__main__":
    heap = []

    heappush(heap, 1)
    heappush(heap, 2)
    heappush(heap, 3)
    heappush(heap, 2)

    while heap:
        print(heappop(heap))

    heap = [43, 4, 13, 634, 120]
    heapify(heap)

    print(heap[0])
    print("end")
