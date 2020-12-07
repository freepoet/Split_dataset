# -*- coding: utf-8 -*-
"""
@File    : png2jpg.py
@Time    : 12/7/20 9:11 PM
@Author  : Mingqiang Ning
@Email   : ningmq_cv@foxmail.com
@Modify Time        @Version    @Description
------------        --------    -----------
12/7/20 9:11 PM      1.0         None
# @Software: PyCharm
"""
"""
    先来说一下jpg图片和png图片的区别
    jpg格式:是有损图片压缩类型,可用最少的磁盘空间得到较好的图像质量
    png格式:不是压缩性,能保存透明等图

"""
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 10:39:03 2019

@author: wsb
"""

import cv2
import os

# print('----------------------------------------------------')
# print('程序的功能为：将该目录下输入的文件内的图片转为指定格式')  # 目前我测试了jpg转化为png和png转化为jpg。
# print('转化结果保存在当前目录下的new_picture内')
# print('----------------------------------------------------')
#
# son = raw_input('请输入需要转化的文件夹名：')
# picture_type = raw_input('请输入想要将图片转化的类型：')
son='data/coco/SSDD/test2007'
daddir = './'
path = daddir + son
picture_type='png'
newpath = 'data/coco/SSDD/test_png'
if not os.path.exists(newpath):
    os.mkdir(newpath)

path_list = os.listdir(path)
number = 0  # 统计图片数量
for filename in path_list:
    number += 1
    portion = os.path.splitext(filename)
    print('convert  ' + filename + '  to ' + portion[0] + '.' + picture_type)
    img = cv2.imread(path + "/" + filename)
    cv2.imwrite("./" + newpath + "/" + portion[0] + '.' + picture_type, img)
print("共转化了%d张图片" % number)
print('转换完毕，文件存入 ' + newpath + ' 中')
cv2.waitKey(0)
cv2.destroyAllWindows()

