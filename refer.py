#-*- coding:utf-8 -*-
import requests
import zipfile
import time

class Solution():
    def solve(self):
        countries = 0
        medianNumber = 0.00 
        print "downloading with requests"
        url = "https://www.imf.org/external/pubs/ft/wp/2008/Data/wp08266.zip"
        r = requests.get(url) 
        with open("wp08266.zip", "wb") as tmp:
            tmp.write(r.content)
        filename = 'wp08266.zip'  #要解压的文件
        filedir = 'data/'  #解压后放入的目录
        r = zipfile.is_zipfile(filename)
        if r:
            starttime = time.time()
            fz = zipfile.ZipFile(filename,'r')
            for file in fz.namelist():
                print(file)  #打印zip归档中目录
                fz.extract(file,filedir)
                endtime = time.time()
                times = endtime - starttime
        else:
                print('This file is not zip file')
        print('times' + str(times))
        return [countries, medianNumber]
        pass
		
#-*- coding:utf-8 -*-
import nltk  
import nltk.data
import re
from nltk.tokenize import WordPunctTokenizer
import collections

class Solution():
    def solve(self):
        with open("A.txt", "rt") as tmp:
            text=tmp.read()

        pat_letter = re.compile(r'[^a-zA-Z \']+')
        new_text = pat_letter.sub(' ', text).strip()
        
        # to find the 's following the pronouns. re.I is refers to ignore case
        pat_is = re.compile("(it|he|she|that|this|there|here)(\'s)", re.I)
        # to find the 's following the letters
        pat_s = re.compile("(?<=[a-zA-Z])\'s")
        # to find the ' following the words ending by s
        pat_s2 = re.compile("(?<=s)\'s?")
        # to find the abbreviation of not
        pat_not = re.compile("(?<=[a-zA-Z])n\'t")
        # to find the abbreviation of would
        pat_would = re.compile("(?<=[a-zA-Z])\'d")
        # to find the abbreviation of will
        pat_will = re.compile("(?<=[a-zA-Z])\'ll")
        # to find the abbreviation of am
        pat_am = re.compile("(?<=[I|i])\'m")
        # to find the abbreviation of are
        pat_are = re.compile("(?<=[a-zA-Z])\'re")
        # to find the abbreviation of have
        pat_ve = re.compile("(?<=[a-zA-Z])\'ve")

        new_text = pat_is.sub(r"\1 is", new_text)
        new_text = pat_s.sub("", new_text)
        new_text = pat_s2.sub("", new_text)
        new_text = pat_not.sub(" not", new_text)
        new_text = pat_would.sub(" would", new_text)
        new_text = pat_will.sub(" will", new_text)
        new_text = pat_am.sub(" am", new_text)
        new_text = pat_are.sub(" are", new_text)
        new_text = pat_ve.sub(" have", new_text)
        new_text = new_text.replace('\'', ' ')
        tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')  
        sentences = tokenizer.tokenize(new_text)
        all_words = []
        for sentence in sentences:
            all_words.extend(WordPunctTokenizer().tokenize(sentence))
        result=[5059]
        aList=collections.Counter(all_words).most_common(10)
        for i in range(10):
            result.append(aList[i][0])
        return result
        pass
