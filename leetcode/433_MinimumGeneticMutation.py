"""
BFS
Time Complexity:
trying the gene variations are 4 options and length 8 thus constant time complexity
making bank a set or checking if current neighbor exist in bank is both O(N), where n is length of bank

If genes were of length n and variation m, it would be m*m*m*...*m thus m^n
convert bank to set is O(nB), as converting a single string of length n is O(n), every character is processed when hashing
-> O(nB + n* n*m * m^n), nB for hash conversion, m^n for available edges, n*m for loop, n for slicing the array
"""
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        visited = set()
        q = deque([(0, startGene)])

        while q:
            step, cur = q.popleft()
            
            if cur == endGene:
                return step
            for i in range(8):
                for c in ['A', 'C', 'G', 'T']:
                    newGene = cur[:i] + c + cur[i+1:]
                    if newGene in bank and newGene not in visited:
                        q.append((step+1, newGene))
                        visited.add(newGene)

        return -1
