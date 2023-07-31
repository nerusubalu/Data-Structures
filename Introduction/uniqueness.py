'''
Write a program to find given array is unique or not
Eg: [1,2,3,4,5f]
'''


#Running time of O(n^2)
def unique(seq):
    n = len(seq)
    for i in range(n): 
        for j in range(i+1, n):
            if seq[i]==seq[j]:
                return False
    return True

#Running time of O(nlogn)
def unique_v2(seq):
    n = len(seq)
    seq.sort()
    for i in range(1,n):
        if seq[i]==seq[i-1]:
            return False
    return True


seq = [1,2,34,5,6,7]
print(unique(seq))
print(unique_v2(seq))