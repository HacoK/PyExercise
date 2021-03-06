'''
聚类问题：
编写聚类函数solve(data)，数据集data为一个二维数组，其类别个数为12，即在聚类时，设置k为12。返回参数为数据集的类标签数组idx，idx为一维行向量。
使用调和平均值v-measure对聚类结果进行评价，若v-measure值大于0.7，则证明聚类算法有效。

数据格式：
'FrogsMFCCs': array([[ 1.        ,  0.1529363 , -0.1055859 , ...,  0.05768398,
         0.11868014,  0.01403845],
       [ 1.        ,  0.17153426, -0.09897474, ...,  0.02013996,
         0.08226299,  0.02905574],
       [ 1.        ,  0.15231709, -0.08297267, ..., -0.02508323,
         0.0991084 ,  0.07716238],
       ..., 
       [ 1.        ,  0.25324917, -0.18068288, ..., -0.03053587,
         0.07844945,  0.08050997],
       [ 1.        ,  0.22105732, -0.11394731, ...,  0.03072397,
         0.16392708,  0.11973469],
       [ 1.        ,  0.15597953, -0.24736819, ..., -0.01421714,
         0.1042441 ,  0.04346174]])
'''

#-*- coding:utf-8 -*-
from sklearn.mixture import GMM      # 1. Choose the model class

class Solution():
    def solve(self, X):
        model = GMM(n_components=12,covariance_type='full')  # 2. Instantiate the model with hyperparameters
        model.fit(X)                    # 3. Fit to data. Notice y is not specified!
        y_gmm = model.predict(X)        # 4. Determine cluster labels
        return y_gmm
        pass