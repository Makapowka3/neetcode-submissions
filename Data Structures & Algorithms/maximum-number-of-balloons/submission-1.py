class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon_map = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
        for ch in text:
            if ch in balloon_map:
                balloon_map[ch] += 1
        
        max_b = float('inf')
        for k, v in balloon_map.items():
            if k == 'o' or k == 'l':
                max_b = min(max_b, v//2)
            else:
                max_b = min(max_b, v)

        return max_b