"""
TC: O(N*M) {here N is the length of the strs list of words and M is the lenght of each word. At every case
            we need to iterate through the list and every character of each word.}
SC: O(N) {We use a dictionary and at worst-case, ie for every word being unique, the length of the dictionary is N.}

Approach:
We devise a hastable/dictionary which is of type list and for every word, we get the character map array, 
turn that into a tuple (since array is not hashable). Using the character map array as a key in the dictionary, we append the 
word to that key's value.
We then iterate through the dictionary for values and return a list of list in the end.

This problem ran successfully on Leetcode.

"""
from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d1 = defaultdict(list)

        for each in strs:
            key = [0]*26
            for ch in each:
                key[ord(ch)-ord("a")] += 1
            d1[tuple(key)].append(each)
        
        return [x for x in d1.values()]
            
        
        

    