class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        # write your code here

        if not dict or len(dict) == 0:
            return 0
        wordDict = set([])
        for word in dict:
            wordDict.add(word)

        wordDict.add(end)
        queue = [start]
        dist = 1
        while len(queue) > 0:
            layer = len(queue)
            #print 'layer', layer
            for i in range(layer):
                word = queue.pop(0)
                if word == end:
                    return dist
                self.addNextWords(word, wordDict,queue)
            dist += 1
            #print queue
        return 0


    def addNextWords(self, beginWord, wordDict, queue):
        if beginWord in wordDict:
            wordDict.remove(beginWord)
        for i in range(len(beginWord)):
            letter = beginWord[i]
            partA = beginWord[:i]
            partB = beginWord[i+1:]
            for p in "abcdefghijklmnopqrstuvwxyz":
                if p == letter:
                    continue
                beginWord= partA +  p + partB
                if beginWord in wordDict:
                    queue.append(beginWord)
                    wordDict.remove(beginWord)
                beginWord= partA +  letter + partB




