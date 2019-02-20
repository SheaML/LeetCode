class Solution:
    def findDiagonalOrder(self, matrix: 'List[List[int]]') -> 'List[int]':
        if matrix == []:
            return []
        
        N=len(matrix) 
        M=len(matrix[0])
        if N==1:
            return matrix[0]
        if M==1:
            return [i for x in matrix for i in x]
        diags=[[] for i in range(M+N-1)]
        for i in range(N):
            for j in range(M):
                diags[i+j].append(matrix[i][j])
        inorder=[x[::-1] if diags.index(x) % 2 == 0 else x for x in diags]
        return [i for x in inorder for i in x]
