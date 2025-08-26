"""
TC: O(N) {we only iterate once through the string s/t (len(s) == len(t))}
SC: O(1) {The character space is only defined to a certain number, as we know the number of ascii characters as well}

Approach:

We iterate throught the array and map the non-mapped characters from pattern to their corresponding position word in s. 
While doing so, if a character was already mapped and the current word is not the same mapped word, return False as
when we replace the char in pattern with mapped word, its not the same word as s, hence its a false.
Also, we used a mapped set, to keep track of the words in s which are already mapped with characters from pattern.


This problem successfully ran on Leetcode.
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapped_word = {}
        mapped = set()
        s = s.split(" ")

        """Since here the len of the pattern and s can be different, we form a base-case to catch this before iteration"""
        if len(s) != len(pattern):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in mapped_word:
                mapped_word[pattern[i]] = s[i]

                #if the word from s is already mapped, return False as we cant map multiple characters from pattern to word in s
                if s[i] in mapped:
                    return False
                mapped.add(s[i])
            else:

                # if the word already mapped in pattern is not same as the ith word at s, return False
                if mapped_word[pattern[i]] != s[i]:
                    return False

        
        return True