'''
Here is a database of financial reforms, covering some economies over 1973 - 2005. You can get it from url
"https://www.imf.org/external/pubs/ft/wp/2008/Data/wp08266.zip", using requests library. In .zip file, Excel file
contains variable names and long labels, and .dta file contains data types.

Then finish these question in problem.py using pandas library:
(1)How many countries in this database of financial reforms?
(2)What is the median number of the year observations in this database of financial reforms for each country?

return [countries, medianNumber];
countries is the answer of question (1);
medianNumber is the answer of question (2);
'''

#-*- coding:utf-8 -*-
import requests
import zipfile
import pandas as pd
import numpy as np

class Solution():
    def solve(self):
        countries = 0
        medianNumber = 0.00 
        url = "https://www.imf.org/external/pubs/ft/wp/2008/Data/wp08266.zip"
        r = requests.get(url) 
        with open("wp08266.zip", "wb") as tmp:
            tmp.write(r.content)
        filename = 'wp08266.zip'  #要解压的文件
        filedir = 'data/'  #解压后放入的目录
        fz = zipfile.ZipFile(filename,'r')
        for file in fz.namelist():
            fz.extract(file,filedir)
        data = pd.read_stata("data/Financial Reform Dataset Dec 2008.dta")
        countries=data['country'].drop_duplicates().count()
        years=data.groupby(['country'])['year'].max()-data.groupby(['country'])['year'].min()
        medianNumber=np.median(years)+1
        return [countries, medianNumber]
        pass