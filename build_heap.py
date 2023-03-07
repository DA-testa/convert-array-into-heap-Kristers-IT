# python3

def build_heap(data,n):
    swaps = []
    for pedejais_elements in range (n // 2, -1, -1):
        j = pedejais_elements

        if 2*pedejais_elements+1 < n and data[2*pedejais_elements+1] < data[j]:
            j = 2*pedejais_elements+1

        if 2*pedejais_elements+2 < n and data[2*pedejais_elements+2] < data[j]:
            j = 2*pedejais_elements+2
            
        if j != pedejais_elements:
            swaps.append((pedejais_elements,j))
            data[pedejais_elements], data[j] = data[j], data[pedejais_elements]
            pedejais_elements = j
        
            i = j
            
            while  i < n // 2:
                j = i

                if 2*i+1 < n and data[2*i+1] < data[j]:
                    j = 2*i+1

                if 2*i+2 < n and data[2*i+2] < data[j]:
                    j = 2*i+2
                
                if j != i:
                    swaps.append((j, i))
                    data[i], data[j] = data[j], data[i]
                    i = j

                else:
                    break

    return swaps

def main():
    
    text = input()

    if text.startswith('I'):
        n = int(input())
        data = list(map(int, input().split()))
        
    elif text.startswith('F'):
        nosaukums = input("Ievadi faila nosaukumu: ") 
        fails = open("./tests/" + nosaukums, "r")
        n = int(fails.readline())
        data = list(map(int,fails.readline().split()))
    
    assert len(data) == n

    swaps = build_heap(data, n)

    print(len(swaps))
    if len(swaps)<4:
        for i, j in swaps:
            print(i, j)

if __name__ == "__main__":
    main()
