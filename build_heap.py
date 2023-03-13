# python3

import math

def build_heap(n,data):
    swaps = []
    n = n-1
    for indekss in range(n, 0, -1):
        berns = indekss
        vecaks = math.floor((indekss-1)/2)
        for indekss in range (n):
            if vecaks >= 0 and data[berns] < data[vecaks]:
                vertiba = data[berns]
                data[berns] = data[vecaks]
                data[vecaks] = vertiba
                swaps.append((vecaks, berns))
            else:
                break
            
            berns = vecaks 
            vecaks = math.floor((berns-1)/2)

           # while  i < n / 2:
               # j = i

               # if 2*i+1 < n and data[2*i+1] < data[j]:
                   # j = 2*i+1

               # if 2*i+2 < n and data[2*i+2] < data[j]:
                   # j = 2*i+2
                
               # if j != i:
                   # swaps.append((j, i))
                   # data[i], data[j] = data[j], data[i]
                   # i = j

               # else:
                   # break

    return swaps

def main():
    
    text = input("Režīms:")

    if text.startswith('I'):
        n = int(input())
        data = list(map(int, input().split()))
        
    elif text.startswith('F'):
        nosaukums = input("Faila nosaukumu: ") 
        fails = open("./tests/" + nosaukums, "r")
        n = int(fails.readline())
        data = list(map(int,fails.readline().split()))
    
    assert len(data) == n
    swaps = build_heap(n,data)

    
    print(len(swaps))
    for i, j in swaps:
        print(i,j)

if __name__ == "__main__":
    main()

