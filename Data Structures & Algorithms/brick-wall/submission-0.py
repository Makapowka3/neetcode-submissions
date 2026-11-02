class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edge_count = {}

        for row in wall:
            col = 0
            for width in row[:-1]:
                col += width
                edge_count[col] = edge_count.get(col, 0) + 1

        most_edges = max(edge_count.values(), default=0)
        return len(wall) - most_edges