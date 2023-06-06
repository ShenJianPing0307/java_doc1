def binary_search(x, A, left, right):
    begin = left
    end = right
    while begin < end:
        middle = (begin + end) // 2
        if x <= A[middle]:
            end = middle 
        else:
            begin = middle + 1
    return end

def merge(A, B, C, R1, R2, R3):
    [[p1, r1], [p2, r2], [p3, r3]] = [R1, R2, R3]

    m = r1 - p1
    n = r2 - p2

    if m < n: # ensure thet m >= n
        A, B = B, A
        m, n = n, m
        [p1, r1], [p2, r2] = R2, R1

    if m <= 0: # both empty?
        return 

    q1 = (p1 + r1) // 2 + 1
    q2 = binary_search(A[q1], B, p2, r2)
    q3 = p3 + (q1 - p1) + (q2 - p2)
    C[q3] = A[q1]

    merge(A, B, C, [p1, q1-1], [p2, q2-1], [p3, q3])
    merge(A, B, C, [q1+1, r1], [q2, r2], [q3+1, r3])

A = [2,3,7,8,11,16]
B = [1,5,7,10,15,19]

C = [0 for i in range(len(A)+len(B))]
merge(A, B, C, [0, len(A)-1], [0, len(B)-1], [0, len(C)-1])
print(C)