class Solution(object):
    def mergeAlternately(self, word1, word2):
        results = []
        i = 0
        for i in range(max(len(word1),len(word2))):
            if i < len(word1):
                results.append(word1[i])
            if i < len(word2):
                results.append(word2[i])
            letters = "".join(results)
        return letters

