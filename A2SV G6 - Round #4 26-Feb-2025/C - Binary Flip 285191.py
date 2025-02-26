# Problem: C - Binary Flip - https://codeforces.com/gym/590053/problem/C


"""

https://codeforces.com/problemset/problem/1504/B

"""

for _ in range(int(input())):
    n = int(input())
    a = input()
    b = input()

    prefix = []
    zeros = ones = 0
    
    for i in a:
        zeros += 1 if i == "0" else 0
        ones += 1 if i == "1" else 0
        prefix.append(zeros == ones)
    
    flipped = False
    can = True

    for i in reversed(range(n)):
        if flipped:
            if a[i] == b[i]:
                if prefix[i]:
                    flipped = False
                else:
                    can = False
                    break
        else:
            if a[i] != b[i]:
                if prefix[i]:
                    flipped = True
                else:
                    can = False
                    break
    
    print('YES' if can else 'NO')