# python3
import numpy as np


def build_heap(data,n):
    swaps = []

    pedejais_elements = n // 2
    while pedejais_elements >= 0:
        j = pedejais_elements
        if 2*pedejais_elements+1 <= n-1 and data[j] < data[2*pedejais_elements+1]:
            j = 2*pedejais_elements+1
            data[pedejais_elements], data[2*pedejais_elements + 1] = data[2*pedejais_elements + 1], data[pedejais_elements]
            if j != pedejais_elements:
                swaps.append((pedejais_elements,j))
        if 2*pedejais_elements+2 <= pedejais_elements -1 and data[j] < data[2*pedejais_elements+1]:
            data[pedejais_elements], data[2*pedejais_elements + 1] = data[2*pedejais_elements + 1], data[pedejais_elements]
            j = 2*pedejais_elements+2
            data[pedejais_elements], data[2*pedejais_elements + 2] = data[2*pedejais_elements + 2], data[pedejais_elements]
            if j != pedejais_elements:
                swaps.append((pedejais_elements,j))
        
        pedejais_elements = pedejais_elements - 1
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)


    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file

    text = input()

    if text.startswith('I'):

        n = int(input())
        data = list(map(int, input().split()))
        
    elif text.startswith('F'):
        nosaukums = input("Ievadi faila nosaukumu: ") 
        fails = open("./test/" + nosaukums, "r")
        n = int(fails.readline())
        data = np.asarray(list(map(int,fails.readline().split())))
    
    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data,n)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for pedejais_elements, j in swaps:
        print(pedejais_elements, j)


if __name__ == "__main__":
    main()
