'''
Write a program to test three-way set disjointness.
'''

def disjoint(A, B, C):
    for a in A:
        for b in B:
            for c in C:
                if a==b==c:
                    return False
    return True

def disjoint_v2(A, B, C):
    for a in A:
        for b in B:
            if a==b:
                for c in C:
                    if a==c:
                        return False
    return True

A = {1,2,3}
B = {4,5,6}
C = {7,8,9}
print(disjoint(A, B, C))
            