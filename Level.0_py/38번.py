def solution(a, b, c, d):
    answer = 0
    if a==b==c==d:
        answer=1111*a
    elif a==b==c:
        answer=(10*a+d)**2
    elif a==b==d:
        answer=(10*a+c)**2
    elif a==c==d: 
        answer=(10*a+b)**2
    elif b==c==d:
        answer=(10*d+a)**2
    elif a==b and c==d:
        answer=(a+c)*abs(a-c)
    elif a==c and b==d:
        answer=(a+b)*abs(a-b)
    elif a==d and b==c:
        answer=(a+b)*abs(a-b)
    elif a==b:
        answer=c*d
    elif a==c:
        answer=b*d
    elif a==d:
        answer=b*c
    elif b==c:
        answer=a*d
    elif b==d:
        answer=a*c
    elif c==d:
        answer=a*b
    else:
        answer=min(a,b,c,d)

    return answer

# 또는 
def solution(a, b, c, d):
    nums = [a, b, c, d]
    counts = [nums.count(i) for i in nums]
    if max(counts) == 4:
        return a * 1111
    elif max(counts) == 3:
        p = nums[counts.index(3)]
        q = nums[counts.index(1)]
        return (10 * p + q) ** 2
    elif max(counts) == 2:
        if min(counts) == 2:
            return (a + c) * abs(a - c) if a == b else (a + b) * abs(a - b)
        else:
            p = nums[counts.index(2)]
            return (a * b * c * d) / p**2
    else:
        return min(nums)