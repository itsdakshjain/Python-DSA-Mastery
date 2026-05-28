class TrieNode:
    def __init__(self):
        self.children = {}
        self.idx = -1


class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        root = TrieNode()

        best = 0
        for i in range(1, len(wordsContainer)):
            if len(wordsContainer[i]) < len(wordsContainer[best]):
                best = i

        root.idx = best

        for i, word in enumerate(wordsContainer):
            node = root
            rev = word[::-1]

            for ch in rev:
                if ch not in node.children:
                    node.children[ch] = TrieNode()

                node = node.children[ch]

                if (
                    node.idx == -1
                    or len(wordsContainer[i]) < len(wordsContainer[node.idx])
                ):
                    node.idx = i

        ans = []

        for word in wordsQuery:
            node = root

            for ch in word[::-1]:
                if ch not in node.children:
                    break
                node = node.children[ch]

            ans.append(node.idx)

        return ans