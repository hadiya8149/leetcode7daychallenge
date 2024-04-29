class Solution:
    def  longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:  # Handle the case where the input list is empty
            return ""
        if len(strs) == 1:
            return strs[0]
        
        def lcp(str1, str2):
                min_length = min(len(str1), len(str2))
                i = 0
                while i < min_length and  str1[i]==str2[i]:            
                    i+=1               
                return str1[:i]

        answer = strs[0]
        for i in range(1,len(strs)):
            if not answer:
                break
            if len(strs[i])==0:
                return ""
            answer = lcp(answer, strs[i])
        return answer
        