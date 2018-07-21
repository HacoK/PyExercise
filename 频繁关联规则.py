#-*- coding:utf-8 -*-
from __future__ import division
import pandas as pd
from pandas import DataFrame,Series

#FP树中节点的类定义
class treeNode:
    def __init__(self, nameValue, numOccur, parentNode):
        self.name = nameValue
        self.count = numOccur
        self.nodeLink = None #nodeLink 变量用于链接相似的元素项
        self.parent = parentNode #指向当前节点的父节点
        self.children = {} #空字典，存放节点的子节点

    def inc(self, numOccur):#计数加1
        self.count += numOccur

#构建FP-tree
def createTree(dataSet, minSup=1):
    headerTable = {}
    for trans in dataSet:  #第一次遍历：统计各个数据的频繁度
        for item in trans:
            headerTable[item] = headerTable.get(item, 0) + dataSet[trans]
            #用头指针表统计各个类别的出现的次数，计算频繁量：头指针表[类别]=出现次数
    for k in list(headerTable):  #删除未达到最小频繁度的数据
        if headerTable[k] < minSup:
            del (headerTable[k])
    freqItemSet = set(headerTable.keys())#保存达到要求的数据
    if len(freqItemSet) == 0:
        return None, None  #若达到要求的数目为0
    for k in headerTable: #遍历头指针表
        headerTable[k] = [headerTable[k], None]  #保存计数值及指向每种类型第一个元素项的指针
    retTree = treeNode('Null Set', 1, None)  #初始化tree
    for tranSet, count in dataSet.items():  # 第二次遍历：
        localD = {}
        for item in tranSet:  # put transaction items in order
            if item in freqItemSet:#只对频繁项集进行排序
                localD[item] = headerTable[item][0]

        #使用排序后的频率项集对树进行填充
        if len(localD) > 0:
            orderedItems = [v[0] for v in sorted(localD.items(), key=lambda p: p[1], reverse=True)]
            updateTree(orderedItems, retTree, headerTable, count)  # populate tree with ordered freq itemset
    return retTree, headerTable  #返回树和头指针表


def updateTree(items, inTree, headerTable, count):
    if items[0] in inTree.children:  # 首先检查是否存在该节点
        inTree.children[items[0]].inc(count)  # 存在则计数增加
    else:  # 不存在则将新建该节点
        inTree.children[items[0]] = treeNode(items[0], count, inTree)#创建一个新节点
        if headerTable[items[0]][1] == None:  # 若原来不存在该类别，更新头指针列表
            headerTable[items[0]][1] = inTree.children[items[0]]#更新指向
        else:#更新指向
            updateHeader(headerTable[items[0]][1], inTree.children[items[0]])
    if len(items) > 1:  #仍有未分配完的树，迭代
        updateTree(items[1::], inTree.children[items[0]], headerTable, count)

#节点链接指向树中该元素项的每一个实例。
# 从头指针表的 nodeLink 开始,一直沿着nodeLink直到到达链表末尾
def updateHeader(nodeToTest, targetNode):
    while (nodeToTest.nodeLink != None):
        nodeToTest = nodeToTest.nodeLink
    nodeToTest.nodeLink = targetNode

#createInitSet() 用于实现上述从列表到字典的类型转换过程
def createInitSet(dataSet):
    retDict = {}
    for trans in dataSet:
        retDict[frozenset(trans)] = 1
    return retDict

#从FP树中发现频繁项集
def ascendTree(leafNode, prefixPath):  #递归上溯整棵树
    if leafNode.parent != None:
        prefixPath.append(leafNode.name)
        ascendTree(leafNode.parent, prefixPath)


def findPrefixPath(basePat, treeNode):  #参数：指针，节点；
    condPats = {}
    while treeNode != None:
        prefixPath = []
        ascendTree(treeNode, prefixPath)#寻找当前非空节点的前缀
        if len(prefixPath) > 1:
            condPats[frozenset(prefixPath[1:])] = treeNode.count #将条件模式基添加到字典中
        treeNode = treeNode.nodeLink
    return condPats

#递归查找频繁项集
def mineTree(inTree, headerTable, minSup, preFix, freqItemList):
    # 头指针表中的元素项按照频繁度排序,从小到大
    bigL = [v[0] for v in sorted(headerTable.items(), key=lambda p: str(p[1]))]#python3修改
    for basePat in bigL:  #从底层开始
        #加入频繁项列表
        newFreqSet = preFix.copy()
        newFreqSet.add(basePat)
        freqItemList.append(newFreqSet)
        #递归调用函数来创建基
        condPattBases = findPrefixPath(basePat, headerTable[basePat][1])

        #2. 构建条件模式Tree
        myCondTree, myHead = createTree(condPattBases, minSup)
        #将创建的条件基作为新的数据集添加到fp-tree
        if myHead != None: #3. 递归
            mineTree(myCondTree, myHead, minSup, newFreqSet, freqItemList)
def check(left_set, right_set, data, count, minSup, minConf, rules):
    left_count=0
    both_count=0
    sum=left_set|right_set
    for trans in data:
        if(left_set.issubset(trans)):
            left_count+=data.get(trans)
        if(sum.issubset(trans)):
            both_count+=data.get(trans)
    sup=both_count/count
    conf=both_count/left_count
    if sup>=minSup and conf>=minConf:
        rule=[left_set,right_set]
        if(rule not in rules):
            rules.append(rule)
    if len(right_set)>1:
        tmp=list(right_set)
        for i in range(len(right_set)):
            new_left=left_set.copy()
            new_right=right_set.copy()
            new_left.add(tmp[i])
            new_right.remove(tmp[i])
            check(new_left, new_right, data, count, minSup, minConf, rules)
class Solution():
    def solve(self):
        data = {}
        count = 0
        with open('A.csv','rb') as file:
            for line in file:
                line=line.strip('\n')
                trans=frozenset(line.split(','))
                data[trans]=data.get(trans,0)+1
                count+=1
        fpTree, headerTable=createTree(data, minSup=150)
        preFix=set()
        freqItemList=[]
        mineTree(fpTree, headerTable, 150, preFix, freqItemList)
        for fset in freqItemList[:]:
            if len(fset)==1 or ('republican0' not in fset and 'democrat0' not in fset):
                freqItemList.remove(fset)
        rules=[]
        for cand_set in freqItemList:
            left_set=set()
            right_set=set()
            if 'republican0' in cand_set:
                left_set.add('republican0')
            else:
                left_set.add('democrat0')
            right_set=cand_set-left_set
            check(left_set,right_set, data, count, 0.45, 0.9, rules)     
        print rules
        return rules
        pass