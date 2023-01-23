def solution(arr1, arr2):
    for i, i_value in enumerate(arr1):
        for j in range(len(i_value)):
            arr1[i][j] = arr1[i][j] + arr2[i][j]

    return arr1