def pair_sum(arr, target):
    for i, elemen in enumerate(arr):
        for j, elemen in enumerate(arr):
            if arr[i]+arr[j] == target and i!=j and i<j :
                return [i,j]

if __name__ == '__main__':
    print(pair_sum([1, 2, 3, 4, 6], 6)) # [1, 3]
    print(pair_sum([2, 5, 9, 11], 11)) # [0, 2]
    print(pair_sum([1, 3, 5, 7], 12)) # [2, 3]
    print(pair_sum([1, 4, 6, 8], 10)) # [1, 2]
    print(pair_sum([1, 5, 6, 7], 6)) # [0, 1]