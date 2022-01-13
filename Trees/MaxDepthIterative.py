class Solution(object):
    def maxDepth(self, root):
        """
        Python 2
        Note:
        Using queue for DFS
        """
        queue = deque()
        if not root:
            return 0
        queue.append(root)
        maxDep = 0
        while queue:
            maxDep += 1
            level_len = len(queue)
            
            for _ in range(level_len):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return maxDep
