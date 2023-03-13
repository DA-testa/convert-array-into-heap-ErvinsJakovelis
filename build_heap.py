# python3

import math
def build_heap(data):
    swaps = []
    for i in range(len(data)-1, 0, -1):
        if data[1] > data[i]:
            swaps.append([1, i])
            data[1], data[i] = data[i], data[1]
            i=1
            if(data[math.floor(i/2)] > data[1]):
                swaps.append([math.floor(i/2), 1])
                data[math.floor(i/2)], data[1] = data[1], data[math.floor(i/2)]



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

    

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
