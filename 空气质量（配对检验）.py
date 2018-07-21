'''
空气质量：
为了探索中国空气质量情况，现调查了主要城市的空气质量情况如下（2010年以及2014年链接分别为http://www.stats.gov.cn/tjsj/ndsj/2014/indexch.htm中8-19以及http://www.stats.gov.cn/tjsj/ndsj/2010/indexch.htm中12-23），以空气质量达到及好于二级的天数为例，探讨空气质量是否变差，并给出统计量的值？alpha=0.05, 使用配对数据检验方法，空气质量变差则返回’YES’
	帮助：
	1. 关于数据处理，可以自行将数据保存为csv文件，上传至慕测在线做题项目空间。(problem目录下)
	操作步骤：
	文件->新建文件
	2. 必须要有文件IO操作，不能直接在本地计算

数据输入格式：
	本题没有数据输入

数据返回格式示例：
	[1, 'NO'] 或 [2, 'YES']
'''

#-*- coding:utf-8 -*-
import numpy as np
from scipy import stats
class Solution:
    def solve(self):
        aList_2010=[285,307,318,296,346,328,340,311,334,315,327,321,353,347,295,322,301,333,347,362,365,303,315,347,365,361,304,236,280,328,262]
        aList_2014=[167,145,49,162,213,215,230,239,246,198,212,180,343,230,79,134,161,196,259,275,342,207,139,278,329,341,157,193,216,249,184]
        diff = np.array(aList_2014) - np.array(aList_2010)
        n = diff.size
        mean = diff.mean()
        s = (diff.var() * n / (n-1))**0.5
        result = mean / s * (n**0.5)
        t = stats.t.ppf(1 - 0.05, n-1)
        judge = "YES" if result < t else "NO"
        return [result, judge]
        pass