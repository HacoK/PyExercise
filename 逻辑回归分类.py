#使用sklearn对数据集做逻辑回归预测，要求返回对测试数据的预测结果

# -*- coding:utf-8 -*- #
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler

iris = datasets.load_iris()
iris_x = iris.data
iris_y = iris.target
# 使用x_train y_train作为训练集
x_train, x_test, y_train, y_test = train_test_split(iris_x, iris_y, test_size=0.3)


class Solution():
    def solve(self, test_data):
        sc = StandardScaler()
        sc.fit(x_train)
        x_train_std = sc.transform(x_train)
        x_test_std = sc.transform(x_test)

        lr = linear_model.LogisticRegression(C=1e5)
        lr.fit(x_train, y_train)
        prepro = lr.predict_proba(x_test_std)
        acc = lr.score(x_test_std,y_test)
        return lr.predict(test_data)
        pass
