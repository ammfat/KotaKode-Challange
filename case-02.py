#!/usr/bin/env python

def cariPasangan(inputList, inputInt):
    pasangan = []

    for i in range(len(inputList)):
        print(inputList[i], end=' | ')

        for j in inputList[i+1:]:
            print(j, end=', ')

            if inputList[i] + j == inputInt:
                pasangan.append([inputList[i], j])

        print()

    return pasangan

def main():
    testCase = [
        [[1, 2, 3, 4, 5], 7],           # [[2, 5], [3, 4]]
        [[1, 2, 4, 6, 9], 15],          # [[6, 9]]
        [[2, 2, 1, 3, 0, 4, 5, 2], 4]   # [[2, 2], [2, 2], [2, 2], [1, 3], [0, 4]]
    ]

    for t in testCase:
        hasil = cariPasangan(t[0], t[1])

        print(f'--> {hasil}')

if __name__ == "__main__":
    main()
