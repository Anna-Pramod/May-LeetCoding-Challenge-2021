#Design a special dictionary which has some words and allows you to search the words in it by a prefix and a suffix.
#Implement the WordFilter class:
#WordFilter(string[] words) Initializes the object with the words in the dictionary.
#f(string prefix, string suffix) Returns the index of the word in the dictionary which has the prefix prefix and the suffix suffix. 
#If there is more than one valid index, return the largest of them. If there is no such word in the dictionary, return -1.

#Example 1:
#Input
#["WordFilter", "f"]
#[[["apple"]], ["a", "e"]]

#Output
#[null, 0]
#Explanation
#WordFilter wordFilter = new WordFilter(["apple"]);
#wordFilter.f("a", "e"); // return 0, because the word at index 0 has prefix = "a" and suffix = 'e".
 
class WordFilter:

    def __init__(self, words: List[str]):
        wrdict = {}
        for ind,wrd in enumerate(words):
            wrdict[wrd] = ind
        
        self.words = [(key+"#"+key,value) for key,value in wrdict.items()]
        

    def f(self, prefix: str, suffix: str) -> int:
        check = suffix+"#"+prefix
        for wrd,ind in reversed(self.words):
            if check in wrd:
                return ind
        return -1
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
