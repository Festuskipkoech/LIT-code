class Solution(object):
    def mergeAlternatively(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged=[]
        i, j =0,0
        while i < len(word1) or j < len(word2):
            if i < len(word1):
                merged.append(word1[i])
                i +=1
            if j < len(word2):
                merged.append(word2[2])
                i +=1
        return ''.join(merged)
merger=Solution()
print(merger.mergeAlternatively("abc", "pqr"))
print(merger.mergeAlternatively("ab", "pqrs"))
print(merger.mergeAlternatively("abcd", "pq"))
