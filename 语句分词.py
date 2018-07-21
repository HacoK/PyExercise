#-*- coding:utf-8 -*-
import nltk
import codecs
import collections
import string

class Solution():
    def solve(self):
        file = codecs.open('A.txt', 'r', 'utf-8')
        sentences = file.read()
        tempStr = string.punctuation+'\n'

        toReplace = ''
        for i in range(len(tempStr)):
            toReplace += ' '

        words = nltk.word_tokenize(sentences.encode('utf-8').translate(string.maketrans(tempStr, toReplace)))

        return [5059]+list(zip(*(collections.Counter(words).most_common(10)))[0])
        pass
