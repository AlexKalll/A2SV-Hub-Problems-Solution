# Problem: Skibidus and Fanum Tax (hard version) - http://codeforces.com/problemset/problem/2065/C2

t = int(input().split()[0])
out_lines = []
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b.sort()
  
    cur = float("-inf")
    can_sort = True
    for ai in a:
        
        cand1 = ai if ai >= cur else None
        
        needed = cur + ai
        left, right = 0, len(b) - 1
        cand2 = None
        while left <= right:
            mid = (left + right) // 2
            if b[mid] >= needed:
                cand2 = b[mid] - ai
                right = mid - 1
            else:
                left = mid + 1
        
        if not cand1 and not cand2:
            can_sort = False
            break
      
        if cand1 is not None and cand2 is not None:
            new_val = cand1 if cand1 < cand2 else cand2
        else:
            new_val = cand1 if cand1 is not None else cand2
        
        cur = new_val

    if can_sort:
        print("YES")
    else:
        print("NO")