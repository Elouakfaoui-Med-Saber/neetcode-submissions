from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            # Frequency array for 26 lowercase letters
            count = [0] * 26

            # Count each character
            for ch in word:
                index = ord(ch) - ord('a')
                count[index] += 1

            # Convert list to tuple so it can be a dictionary key
            key = tuple(count)

            # Add the word to its group
            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())