class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)

        for word in strs:
            arr = [0] * 26
            for char in word:
                char_index = ord(char) - ord("a")
                arr[char_index] += 1

            dic[tuple(arr)].append(word)

        return dic.values()
        