# Problem: B - Square String? - https://codeforces.com/gym/585132/problem/B

t = int(input())

for _ in range(t):
    string = input()
    l = len(string) % 2
    square = string[len(string)//2:] == string[:len(string)//2]

    if l == 0:
        if square:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')