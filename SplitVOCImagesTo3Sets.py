# -*- coding: utf-8 -*-
"""
@File    : SplitVOCImagesTo3Sets.py
@Time    : 11/19/20 8:30 PM
@Author  : Mingqiang Ning
@Email   : ningmq_cv@foxmail.com
@Modify Time        @Version    @Description
------------        --------    -----------
11/19/20 8:30 PM      1.0         None
# @Software: PyCharm
"""
# coding=utf-8
import cv2
import os

allims = './data/SSDD/VOC2007/JPEGImages'
out = './data/SSDD/VOC2007/test2007'
train = './data/SSDD/VOC2007/ImageSets/Main/test.txt'
f = open(train)
for line in f:
    im_path = os.path.join(allims, line[:-1] + '.jpg')
    im = cv2.imread(im_path)
    out_path = os.path.join(out, line[:-1] + '.jpg')
    cv2.imwrite(out_path, im)
