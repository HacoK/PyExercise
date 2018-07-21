'''
随机变量分布：
假定一块蛋糕上的葡萄干粒数服从泊松分布，如果想让每块蛋糕上至少有一粒葡萄干的概率大于等于0.98，
   蛋糕上葡萄干的平均粒数应该是多少？

数据输入格式：
	本题没有数据输入；

数据返回格式示例：
	n
'''

import math
import pandas as pd
import numpy as np
class Solution:
    def solve(self):
        x = int(round(math.log(50),0))
        return x