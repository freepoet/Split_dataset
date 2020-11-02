# -*- coding: utf-8 -*-
"""
@File    : create_label_map.py
@Time    : 10/26/20 9:00 PM
@Author  : Mingqiang Ning
@Email   : ningmq_cv@foxmail.com
@Modify Time        @Version    @Description
------------        --------    -----------
10/26/20 9:00 PM      1.0         None
# @Software: PyCharm
"""
import os
import json
import cv2
path = os.getcwd()   # acquire local path
AnnotationsPath = os.listdir(os.path.join(path, "Annotations"))

from xml.etree.ElementTree import parse

words = []
for file in AnnotationsPath:
    tree = parse(os.path.join(path,"Annotations", file))
    root = tree.getroot()
    objects = root.findall("object")
    names = [x.findtext("name") for x in objects]

    for name in names:
        if name not in words:
            words.append(name)

tempDictionary = {}
train_id = 1
for word in words:
    tempDictionary[word] = train_id
    train_id += 1

print(tempDictionary)
with open("voc_label_map.json", "w") as write_file:
    json.dump(tempDictionary, write_file)