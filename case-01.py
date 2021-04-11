#!/usr/bin/env python

def hurufBergantian(inputString):
    hitung = 0
    
    for i in range(1, len(inputString)):
        if inputString[i-1] == inputString[i]:
            hitung += 1

    return hitung

def main():
    testCase = [
        'PCPCCPC',      # 1
        'PPCPPC',       # 2
        'PCPPCPPP',     # 3
        'CPCCPCCC',     # 3
        'CPPCPCPCP',    # 1
        'CCPCPPPCCP',   # 4
        'CCCCCCPCCCPP'  # 8
    ]

    for t in testCase:
        hasil = hurufBergantian(t)
        print(f'{t}\t --> {hasil}')

if __name__ == "__main__":
    main()

