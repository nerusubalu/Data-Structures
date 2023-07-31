'''
Write a program to find given array is unique or not
Eg: [1,2,3,4,5f]
'''


#Running time of O(n^2)
def unique(S):
    n = len(S)
    for i in range(n):
        for j in range(i+1, n):
            if S[i]==S[j]:
                return False
    return True

#Running time of O(n)
def unique_v2(S):
    n = len(S)
    S.sort()
    for i in range(1,n):
        if S[i]==S[i-1]:
            return False
    return True


S = [1,2,34,5,6,7]
print(unique(S))
print(unique_v2(S))