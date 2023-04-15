from random import randint

def insert_sort(A):
    N = len(A)
    for i in range(1,N):
        k = A[i]
        j = i-1
        while j>=0 and k < A[j] :
            A[j+1] = A[j]
            j = j - 1
        A[j+1] = k
    
def slive(A,B):
   i,j = 0,0
   C = []
   while i<len(A) and j<len(B):
       if A[i] < B[j]:
           C.append(A[i])
           i+=1
       else:
           C.append(B[j])
           j += 1
   if i == len(A):
       while j < len(B):
           C.append(B[j])
           j += 1
   else:
       while i < len(A):
           C.append(A[i])
           i += 1       
   return C

N = 1052
K = 100
Y = [randint(0,10) for i in range( N ) ]
print(Y)
A = Y[:K]
insert_sort(A)
i = K
while i < (N-K):
    B=Y[i:i+K]
    insert_sort(B) 
    A = slive(A,B)
    i += K
B=Y[i:]
insert_sort(B) 
A = slive(A,B)
print(A)