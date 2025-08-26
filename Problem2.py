"""
TC: O(N) {we only iterate once through the string s/t (len(s) == len(t))}
SC: O(N) {we use one char map array and a set to track already mapped characters}

Approach:

We iterate throught the array and map the non-mapped characters from s to their corresponding position characters in t. 
While doing so, if a character was already mapped and the current character is not the same mapped character, return False as
when we replace the char in s with mapped character, its not the same character as t, hence its a false.
Also, we used a mapped set, to keep track of the characters in t which are already mapped with characters from s.


This problem successfully ran on Leetcode.
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_map = {}
        mapped = set()

        for i in range(len(s)):
            if s[i] not in char_map:
                char_map[s[i]] = t[i]

                #if the char from t is already mapped, return False as we cant map multiple characters from s to single char in t
                if t[i] in mapped:
                    return False
                mapped.add(t[i])
            else:

                # if the character already mapped in s is not same as the ith character at t, return False
                if char_map[s[i]] != t[i]:
                    return False
            

        return True


