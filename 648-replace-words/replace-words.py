
# # Method 1: Trie
# class Solution:
#     def replaceWords(self, dictionary: List[str], sentence: str) -> str:
#         # method: prefix-tree(Trie)
#         prefixTree = Trie()
#         for word in dictionary: # prefix Tree
#             prefixTree.insert(word)
#         res = []
#         for word in sentence.split():
#             prefix = prefixTree.getShortestPrefix(word)
#             if prefix:
#                 res.append(prefix)   
#             else:
#                 res.append(word)
#         return ' '.join(res)            

# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.is_end_of_word = False
# class Trie:
#     def __init__(self):
#         self.root = TrieNode()
#     def insert(self,word):
#         node = self.root
#         for char in word:
#             if char not in node.children:
#                 node.children[char] = TrieNode()
#             node = node.children[char]
#         node.is_end_of_word = True
#     def search(self, word):
#         node = self.root
#         for char in word:
#             if char in node.children:
#                 node = node.children[char]
#             return False
#         return node.is_end_of_word
#     def startwith(self, prefix):
#         node = self.root
#         for char in prefix:
#             if char not in node.children:
#                 return False
#             node = node.children[char]
#         return True
#     def getShortestPrefix(self, word):
#         node = self.root
#         prefix = ""
#         for char in word:
#             if char in node.children:
#                 node = node.children[char]
#                 prefix += char
#                 if node.is_end_of_word:
#                     return prefix
#             else:
#                 break
#         return ""
#     def getLongestPrefix(self, word):
#         # 从根节点开始
#         node = self.root
#         prefix = ""
#         for char in word:
#             if char in node.children:
#                 node = node.children[char]
#                 prefix += char
#         if node.is_end_of_word:

#             return prefix

# ========================================================================
# Method 2: HashSet
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        wordArray = sentence.split()
        dictSet = set(dictionary)
        def shortest_root(word,dictSet): # find the shortest root from a given word
            for i in range(len(word)):
                root = word[0:i]
                if root in dictSet:
                    return root
            return word
        for i in range(len(wordArray)):
            wordArray[i] = shortest_root(wordArray[i],dictSet)
        return " ".join(wordArray)