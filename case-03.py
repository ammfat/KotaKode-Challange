#!/usr/bin/env python

def subsetTerbesar(inputList):
    '''
    Mengembalikan subset dari elemen tak bersebalahan
    yang jika ditotal memiliki jumlah terbesar. Bila semua
    elemen bernilai negatif, maka akan dikembalikan nilai 0
    '''

    subset = []
    maksTotal = 0

    for i in range(len(inputList)):

        ## Bagian 1
        for j in inputList[i+2:]:
            subset.append([inputList[i], j])

        ## Bagian 2
        tempList = [inputList[i]]
        sisiKanan = inputList[i+2:]
        
        if len(sisiKanan) == 0:
            continue

        for t in range(0, len(sisiKanan), 2):
            tempList.append(sisiKanan[t])

        if tempList not in subset:
            subset.append(tempList)

    ## Menemukan subset dengan total nilai antar elemen terbesar
    for total in subset:
        maksTotal = sum(total) if sum(total) > maksTotal else maksTotal

    return maksTotal


def main():  
    testCase = [
        [1, 2, 300, -400, 5],       # 306
        [3, 7, 4, 6, 5],            # 13
        [2, 1, 5, 8, 4],            # 11
        [3, 5, -7, 8, 10],          # 15
        [-1, -2, -3, -4, -22],      # 0
        [-2, 1, 2, 10, 22, 0],      # 24
        [0, 0, 0, 0, 0, 0]          # 0
    ]

    for t in testCase:
        hasil = subsetTerbesar(t)        
        print(f'--> {hasil}')


# DRIVER CODE
if __name__ == "__main__":
    main()