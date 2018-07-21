'''
﻿推荐系统：
同学们需要完成solve(R ,Y ,ratings ,k)函数，Y是包含1到5等级的（电影数量（行）*用户数量（列））二维数组。R是包含指示用户是否已经评级电影的二进制值的“指示”数组。两者具有相同的形状；ratings为传入的待推荐用户评分数据，其为一维列向量（电影数量（行）*1），每一个数字代表该用户在此电影上的评分；k为要返回的推荐列表中电影的个数。
评分标准为，|output_id&standard_id|/k，output_id为返回的结果，standard_id为后台标准推荐id，当重合度>=0.6时，证明推荐有效。

输入数据格式：
'R': array([[1, 1, 0, ..., 1, 0, 0],
        [1, 0, 0, ..., 0, 0, 1],
        [1, 0, 0, ..., 0, 0, 0],
        ..., 
        [0, 0, 0, ..., 0, 0, 0],
        [0, 0, 0, ..., 0, 0, 0],
        [0, 0, 0, ..., 0, 0, 0]], dtype=uint8),
'Y': array([[5, 4, 0, ..., 5, 0, 0],
        [3, 0, 0, ..., 0, 0, 5],
        [4, 0, 0, ..., 0, 0, 0],
        ..., 
        [0, 0, 0, ..., 0, 0, 0],
        [0, 0, 0, ..., 0, 0, 0],
        [0, 0, 0, ..., 0, 0, 0]], dtype=uint8),

数据返回格式示例：
{1,2,3,4,...,k}
'''

#-*- coding:utf-8 -*-

class Solution():
    def solve(self, R, Y, ratings, k):
        abs_r = (ratings*ratings).sum()**0.5
        R = R.T
        Y = Y.T
        count = R.shape[1]
        sim_list = []
        rec = set()
        for i in range(Y.shape[0]):
            abs_s = (Y[i]*Y[i]).sum()**0.5
            prod = (Y[i]*ratings.T).sum()
            sim = prod/(abs_r*abs_s)
            sim_list.append(sim)
        temp = sim_list[:]
        temp.sort(reverse=True)
        index = 0
        rate = 5
        while len(rec)<k:
            id = sim_list.index(temp[index])
            for i in range(count):
                if len(rec)<k:
                    if ratings[i][0] == 0 and R[id][i] == 1 and Y[id][i] == rate:
                        rec.add(i)
                else:
                    return rec
            index += 1
            if index == len(temp):
                index = 0
                rate -= 1
        return rec
        pass