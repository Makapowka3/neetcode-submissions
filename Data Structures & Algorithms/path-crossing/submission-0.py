class Solution:
    def isPathCrossing(self, path: str) -> bool:
        locations = set([(0,0)])

        start = [0,0]
        for move in path:
            if move == 'N':
                start[0] += 1
            elif move == 'S':
                start[0] -= 1
            elif move == 'W':
                start[1] += 1
            else:
                start[1] -= 1
            
            locations.add(tuple(start))
        return len(locations) != len(path)+1