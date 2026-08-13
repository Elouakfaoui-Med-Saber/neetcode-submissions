class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for word in strs:
            encoded += str(len(word)) + "#" + word

        return encoded


    def decode(self, s: str) -> List[str]:
        decoded = []

        i = 0

        while i < len(s):

            # Find the position of '#'
            j = i
            while s[j] != '#':
                j += 1

            # Extract the length
            length = int(s[i:j])

            # Move after '#'
            j += 1

            # Extract the string using the length
            word = s[j:j + length]

            decoded.append(word)

            # Move i to the next encoded string
            i = j + length

        return decoded