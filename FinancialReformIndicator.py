'''
Here is a database of financial reforms, covering some economies over 1973 - 2005. You can get it from url
"https://www.imf.org/external/pubs/ft/wp/2008/Data/wp08266.zip", using requests library. In .zip file, Excel file
contains variable names and long labels, and .dta file contains data types.

Then finish these question in problem.py using pandas library:
(1)Which one country has the highest pace of implementing finacial reforms among transition countries?
'''

# -*- coding:utf-8 -*-
import pandas as pd


class Solution():
    def solve(self):
        df = pd.read_stata('target.dta').query('Transition==1')[['country', 'finreform_n']]

        listCountry = []
        listPace = []

        for item in df.groupby('country'):
            listCountry.append(item[0])  # item是一个元组
            listFin = list(item[1]['finreform_n'])
            listPace.append(max([listFin[i + 1] - listFin[i] for i in range(len(listFin) - 1)]))

        return listCountry[listPace.index(max(listPace))]
        pass