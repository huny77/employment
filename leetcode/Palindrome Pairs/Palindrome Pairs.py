class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        result = []
        for a in range(len(words)):
            for b in range(len(words)):
                if a == b:
                    continue
                combine = words[a] + words[b]
                if combine == combine[::-1]:
                    result.append([a, b])
        return result
