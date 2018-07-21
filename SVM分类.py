# 使用sklearn对数据集分类，要求返回对测试数据的预测结果

# -*- coding:utf-8 -*- #
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB # 1. choose model class
# add package here

iris = datasets.load_iris()
iris_x = iris.data
iris_y = iris.target
# 利用x_train y_train作为训练集
x_train, x_test, y_train, y_test = train_test_split(iris_x, iris_y, test_size=0.3)


class Solution():
    def solve(self, test_data):
        # call function classification
        model = GaussianNB()                       # 2. instantiate model
        model.fit(x_train, y_train)                  # 3. fit model to data
        y_model = model.predict(test_data)             # 4. predict on new data
        return y_model
        pass
