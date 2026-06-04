class Solution:
    def compress(self, chars: List[str]) -> int:
        read, write = 0, 0
        n = len(chars)

        while read < n:
            ch = chars[read]
            start = read

            while read < n and chars[read] == ch:
                read += 1
            
            count = read - start
            chars[write] = ch
            write += 1

            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1
            
        return write