def diagonalDifference(arr):
    lenght = arr[0][0]
    main_diagonal = 0
    second_diagonal = 0
    print(lenght)
    for i in range(1, (lenght+1)):
        main_diagonal = main_diagonal + arr[i][i-1]
        second_diagonal = second_diagonal + arr[i][lenght-i]
    print("Diagonal principal:", main_diagonal)
    print("Diagonal secundaria:", second_diagonal)
    return (main_diagonal - second_diagonal)

if __name__ == '__main__':
    arr = []
    arr = [[3], [11, 2, 4], [4, 5, 6], [10, 8, -12]]
    print(diagonalDifference(arr))
