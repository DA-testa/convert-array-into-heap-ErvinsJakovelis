# python3

def sift_down(arr, i, swaps):
    min_index = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2
    n = len(arr)

    if left_child < n and arr[left_child] < arr[min_index]:
        min_index = left_child

    if right_child < n and arr[right_child] < arr[min_index]:
        min_index = right_child

    if i != min_index:
        arr[i], arr[min_index] = arr[min_index], arr[i]
        swaps.append((i, min_index))
        sift_down(arr, min_index, swaps)


def build_heap(arr):
    swaps = []
    n = len(arr)
    for i in range(n // 2, -1, -1):
        sift_down(arr, i, swaps)
    return swaps



def main():
    
    ievade = input()
    if 'F' in ievade:
        path = input()
        path = "tests/" + path
        with open(path, "r") as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))
            
    if 'I' in ievade:
        n = int(input())
        data = list(map(int, input().split()))

    
    assert len(data) == n

    swaps = build_heap(data)




    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
