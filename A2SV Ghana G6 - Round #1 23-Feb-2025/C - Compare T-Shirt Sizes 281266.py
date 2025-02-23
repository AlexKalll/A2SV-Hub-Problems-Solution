# Problem: C - Compare T-Shirt Sizes - https://codeforces.com/gym/585132/problem/C

# https://codeforces.com/gym/585107/problem/C
t = int(input())
for _ in range(t):
    a, b = input().split()
    
    if a == b:
        print('=')

    elif a[-1] == 'L':
        if b[-1] != 'L':
            print('>')
        else:
            print('>') if len(a) > len(b) else print('<')

    elif a[-1] == 'M':
        if b[-1] != 'L':
            print('>')
        else:
            print('<')

    elif a[-1] == 'S':
        if b[-1] != 'S':
            print('<')
        else:
            print('<') if len(a) > len(b) else print('>')