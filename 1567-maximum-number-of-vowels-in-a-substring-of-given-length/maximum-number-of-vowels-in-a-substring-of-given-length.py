class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = list('aeiou')
        counter = 0        
        for char in s[:k]:
            if char in vowels:
                counter +=1
        max_vowels = counter
        for i in range(k,len(s)):
            if s[i] in vowels:
                counter += 1
            if s[i-k] in vowels:
                counter -= 1
            max_vowels = max(max_vowels, counter)
        return max_vowels