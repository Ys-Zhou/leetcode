class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        mat = [[0] * n for _ in xrange(n)]
        for pair in edges:
            mat[pair[0]][pair[1]] = mat[pair[1]][pair[0]] = 1

        nodes = set(xrange(n))
        leaves = set()

        while len(nodes) > 2:
            for node in nodes:
                if sum(mat[node]) == 1:
                    leaves.add(node)
            nodes -= leaves
            for node in nodes:
                for leaf in leaves:
                    mat[node][leaf] = 0
            leaves.clear()
        return list(nodes)
