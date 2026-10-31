class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        unpack = path.split('/')
        
        for w in unpack:
            if w == '.':
                pass

            elif w == '..':
                if stack:
                    stack.pop()
            
            elif w == '':
                pass
            
            else:
                stack.append(w)
        
        return '/'+ '/'.join(stack)