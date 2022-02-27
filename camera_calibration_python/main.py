#!usr/bin/env/ python
# _*_ coding:utf-8 _*_
 
import cv2 as cv
import numpy as np
import os
from homography import get_homography
from intrinsics import get_intrinsics_param
from extrinsics import get_extrinsics_param
from distortion import get_distortion
from refine_all import refinall_all_param
 
 
def calibrate():
    '''求解单适应矩阵'''
    H = get_homography(pic_points, real_points_x_y)
 
    '''求解相机内参'''
    intrinsics_param = get_intrinsics_param(H)
 
    '''求解相机外参'''
    extrinsics_param = get_extrinsics_param(H, intrinsics_param)
 
    '''畸变矫正'''
    k = get_distortion(intrinsics_param, extrinsics_param, pic_points, real_points_x_y)
 
    '''微调所有参数'''
    [new_intrinsics_param, new_k, new_extrinsics_param]  = refinall_all_param(intrinsics_param,
                                                            k, extrinsics_param, real_points, pic_points)
 
    print("intrinsics_parm:\t", new_intrinsics_param)
    print("distortionk:\t", new_k)
    print("extrinsics_parm:\t", new_extrinsics_param)
 
 
if __name__ == "__main__":

    '''r+字符串 表示后面都是普通字符串 没有转义字符'''
    file_dir = r"/home/amber/code/opencv/Camera_calibration/image/"
    pic_name = os.listdir(file_dir)
 
    '''由于棋盘为二维平面,设定世界坐标系在棋盘上,一个单位代表一个棋盘宽度,产生世界坐标系三维坐标'''
    cross_corners = [11, 8] 
    real_coor = np.zeros((cross_corners[0] * cross_corners[1], 3), np.float32)

    '''
    np.mgrid()函数
    用法:返回多维结构,常见的如2D图形,3D图形。对比np.meshgrid,在处理大数据时速度更快,且能处理多维(np.meshgrid只能处理2维)
    ret = np.mgrid[ 第1维,第2维,第3维,…] 
    返回多值,以多个矩阵的形式返回,
    第1返回值为第1维数据在最终结构中的分布,
    第2返回值为第2维数据在最终结构中的分布,以此类推。(分布以矩阵形式呈现) 
    '''
    real_coor[:, :2] = np.mgrid[0:11, 0:8].T.reshape(-1, 2)
    
    real_points = []
    real_points_x_y = []
    pic_points = []
 
    for pic in pic_name:
        pic_path = os.path.join(file_dir, pic)
        pic_data = cv.imread(pic_path)
 
        '''opencv find chessboardcorners'''
        succ, pic_coor = cv.findChessboardCorners(pic_data, (cross_corners[0], cross_corners[1]), None)
 
        if succ:
            '''reshape'''
            pic_coor = pic_coor.reshape(-1, 2)
            """像素坐标系2d点"""
            pic_points.append(pic_coor)
            '''世界坐标系3d点 将z=0'''
            real_points.append(real_coor)
            real_points_x_y.append(real_coor[:, :2])
    calibrate()



