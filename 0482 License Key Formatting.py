# https://leetcode.com/problems/license-key-formatting/

# Version 1
class SolutionOne:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        part, parts = '', []
        
        for i in range(len(S))[::-1]:
            if S[i] == "-":
                continue
            
            part = f'{S[i].upper()}{part}'
            
            if len(part) == K:
                parts = [part] + parts
                part = ''
        
        if len(part) > 0:
            parts = [part] + parts
        
        # print(parts)
        return '-'.join(parts)
        
# Version 2
class SolutionTwo:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        reverse = S.replace('-', '').upper()[::-1]
        reverse_parts = [reverse[i:i + K][::-1] for i in range(0, len(reverse), K)]
        return '-'.join(reverse_parts[::-1])
    
# Version 3
class SolutionThree:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        part, parts = '', []
        
        for idx, val in enumerate(S.replace('-', '')[::-1]):
            if len(part) == K:
                parts.append(part)
                part = ''
            part = val.upper() + part
        if part != '':
            parts.append(part)
        return '-'.join(parts[::-1])
