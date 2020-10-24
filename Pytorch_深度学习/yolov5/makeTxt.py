#coding=utf-8
import os
import random


trainval_percent = 0.1
train_percent = 0.9
xmlfilepath = 'data/Annotations/outputs'
txtsavepath = 'data/ImageSets'

total_xml = os.listdir(xmlfilepath)  # 收集指定目录下文件名
num = len(total_xml)
list = range(num)

tv = int(num * trainval_percent)     # 验证集数
tr = int(tv * train_percent)         # 验证集数 * 0.9

trainval = random.sample(list, tv)   # 验证集
train = random.sample(trainval, tr)  # 验证集 * 0.9

ftrainval = open('data/ImageSets/trainval.txt', 'w')  # 验证
ftest = open('data/ImageSets/test.txt', 'w')
ftrain = open('data/ImageSets/train.txt', 'w')        # 训练
fval = open('data/ImageSets/val.txt', 'w')

for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)       # 验证集
        if i in train:
            ftest.write(name)       # 验证集 * 0.9 为测试集
        else:
            fval.write(name)        # 其余验证集为验证集
    else:
        ftrain.write(name)          # 训练集

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()
