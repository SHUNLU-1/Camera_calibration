# 张正友相机标定原理

## 一、相机成像原理

### 1、相机成像系统中，共包含四个坐标系：世界坐标系、相机坐标系、图像坐标系、像素坐标系。

![](https://s5.51cto.com/images/blog/202107/14/4dca84ba1b3cb9fd049a50c95219d631.png?x-oss-process=image/watermark,size_16,text_QDUxQ1RP5Y2a5a6i,color_FFFFFF,t_100,g_se,x_10,y_10,shadow_90,type_ZmFuZ3poZW5naGVpdGk=)

### 2、这四个坐标系之间的转化关系为：

![](https://pic1.zhimg.com/80/v2-665648ff84735e54ea26e34ed9096ba8_1440w.jpg)

![](https://pic2.zhimg.com/80/v2-7813885e0d781a4301feee1ce9f52041_1440w.jpg)

- 其中， $(U,V,W)$ 为在**世界坐标系下一点的物理坐标**，$(u,v)$ 为该点对应的在**像素坐标系下的像素坐标**， Z 为**尺度因子**。

### 3、内参矩阵和外参矩阵

![内参矩阵](https://www.zhihu.com/equation?tex=%5Cleft%28%5Cbegin%7Barray%7D%7Bccc%7D%7B%5Cfrac%7B1%7D%7Bd+X%7D%7D+%26+%7B-%5Cfrac%7B%5Ccot+%5Ctheta%7D%7Bd+X%7D%7D+%26+%7Bu_%7B0%7D%7D+%5C%5C+%7B0%7D+%26+%7B%5Cfrac%7B1%7D%7Bd+Y+%5Csin+%5Ctheta%7D%7D+%26+%7Bv_%7B0%7D%7D+%5C%5C+%7B0%7D+%26+%7B0%7D+%26+%7B1%7D%5Cend%7Barray%7D%5Cright%29%5Cleft%28%5Cbegin%7Barray%7D%7Bcccc%7D%7Bf%7D+%26+%7B0%7D+%26+%7B0%7D+%26+%7B0%7D+%5C%5C+%7B0%7D+%26+%7Bf%7D+%26+%7B0%7D+%26+%7B0%7D+%5C%5C+%7B0%7D+%26+%7B0%7D+%26+%7B1%7D+%26+%7B0%7D%5Cend%7Barray%7D%5Cright%29+%3D+%5Cleft%28%5Cbegin%7Barray%7D%7Bcccc%7D%7B%5Cfrac%7Bf%7D%7Bd+X%7D%7D+%26+%7B-%5Cfrac%7Bf%5Ccot+%5Ctheta%7D%7Bd+X%7D%7D+%26+%7Bu_%7B0%7D%7D+%26+%7B0%7D+%5C%5C+%7B0%7D+%26+%7B%5Cfrac%7Bf%7D%7Bd+Y+%5Csin+%5Ctheta%7D%7D+%26+%7Bv_%7B0%7D%7D+%26+%7B0%7D+%5C%5C+%7B0%7D+%26+%7B0%7D+%26+%7B1%7D+%26+%7B0%7D%5Cend%7Barray%7D%5Cright%29+%5C%5C)

- 我们将这样的矩阵称为**内参矩阵**，内参矩阵取决于相机的内部参数。其中，$f$为**焦距**，$dX$,$dY$分别表示$X$,$Y$方向上的**一个像素在相机感光板上的物理长度（即一个像素在感光板上是多少毫米**，$u_0$,$v_0$分别表示**相机感光板中心在像素坐标系下的坐标**，$\theta$表示**感光板的横边和纵边之间的角度**。
  ![](https://pic3.zhimg.com/80/v2-f1e31af73f94b6edbacee6b237702f02_1440w.png)
- 我们将这样的矩阵称为相机的**外参矩阵**，外参矩阵取决于相机坐标系和世界坐标系的相对位置,$R$ 表示**旋转矩阵**，$T$ 表示**平移矢量**。

### 4、畸变与畸变矫正

- 另外，相机拍摄的图片还存在一定的畸变，畸变包括**桶形畸变和枕形畸变**，畸变模型包括**径向畸变和切向畸变**。
  ![](https://img-blog.csdnimg.cn/20190412190959963.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQwMzY5OTI2,size_16,color_FFFFFF,t_70)
  ![](https://img-blog.csdnimg.cn/20190412190949639.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQwMzY5OTI2,size_16,color_FFFFFF,t_70)
  
  **径向畸变公式（3 阶）如下：**
  ![](https://www.zhihu.com/equation?tex=%5Chat%7Bx%7D+%3D+x%281%2Bk_1r%5E2%2Bk_2r%5E4%2Bk_3r%5E6%29+%5C%5C+%5Chat%7By%7D+%3D+y%281%2Bk_1r%5E2%2Bk_2r%5E4%2Bk_3r%5E6%29)
  
  **切向畸变公式如下：**
  ![](https://www.zhihu.com/equation?tex=%5Chat%7Bx%7D+%3D+x%2B%282p_1y%2Bp_2%28r%5E2%2B2x%5E2%29%29+%5C%5C+%5Chat%7By%7D+%3D+y%2B%28p_1%28r%5E2%2B2y%5E2%29%2B2p_2x%29+)

- 其中，$(x,y)$,$(\hat{x},\hat{y})$分别为**理想的无畸变的归一化的图像坐标、畸变后的归一化图像坐标**， $r^2=x^2+y^2$为**图像像素点到图像中心点的距离**。

## 二、张正友相机标定原理

### 1、相机标定的目的是什么？

- 为什么要进行相机标定呢？比如，当我们拿到一张图片，进行识别之后，得到的两部分之间的距离为多少多少像素，但是这多少多少像素究竟对应实际世界中的多少米呢？这就需要利用相机标定的结果来将**像素坐标转换到物理坐标来计算距离**（当然这里值得说明，仅仅利用单目相机标定的结果，是无法直接从像素坐标转化到物理坐标的，因为透视投影丢失了一个维度的坐标，所以测距其实需要双目相机）。
- ###### 相机标定的目的其实很简单，我们要想对一个成像系统建模，进而进行相应的计算，所必须的参数就是相机的**内参矩阵**和相机的**外参矩阵**，因此，**相机标定的第一个目的就是获得相机的内参矩阵和外参矩阵**。
- **相机标定的第二个目的就是获得相机的畸变参数**，进而对拍摄的图片进行去畸变处理。

### 2、张正友标定法简介

- 张正友标定法用如下图所示的棋盘格标定板，在得到一张标定板的图像之后，可以利用相应的图像检测算法得到每一个角点的**像素坐标 $(u,v)$**。

- 张正友标定法将世界坐标系固定于棋盘格上，则棋盘格上任一点的**物理坐标 $W=0$**，由于标定板的世界坐标系是人为事先定义好的，标定板上每一个格子的大小是已知的，我们可以计算得到每一个角点在世界坐标系下的**物理坐标 $(U,V,W = 0)$** 。

- 我们将利用这些信息：每一个角点的**像素坐标 $(u,v)$** 、每一个角点在世界坐标系下的**物理坐标 $(U,V,W = 0)$**，来进行相机的标定，获得相机的**内外参矩阵、畸变参数**。
  ![](https://pic1.zhimg.com/80/v2-5b33936d1763e5b569ab23162745b544_1440w.jpg)

### 3、标定相机的内参矩阵和外参矩阵

#### 张正友标定法标定相机的内外参数的思路如下：

- (1)、求解内参矩阵与外参矩阵的积；
- (2)、求解内参矩阵；
- (3)、求解外参矩阵。
- (4)、标定相机的畸变参数
- (5)、L-M 算法参数优化

#### (1)、求解内参矩阵与外参矩阵的积

将世界坐标系固定于棋盘格上，则棋盘格上任一点的物理坐标 $W=0$ ，因此，原单点无畸变的成像模型可以化为下式。其中， $R1,R2$ 为旋转矩阵 $R$ 的前两列。为了简便，将内参矩阵记为 $A$ 。

![](https://www.zhihu.com/equation?tex=Z%5Cleft%28%5Cbegin%7Barray%7D%7Bl%7D%7Bu%7D+%5C%5C+%7Bv%7D+%5C%5C+%7B1%7D%5Cend%7Barray%7D%5Cright%29%3D%5Cleft%28%5Cbegin%7Barray%7D%7Bccc%7D%7B%5Cfrac%7Bf%7D%7Bd+X%7D%7D+%26+%7B-%5Cfrac%7Bf+%5Ccot+%5Ctheta%7D%7Bd+X%7D%7D+%26+%7Bu_%7B0%7D%7D+%5C%5C+%7B0%7D+%26+%7B%5Cfrac%7Bf%7D%7Bd+Y+%5Csin+%5Ctheta%7D%7D+%26+%7Bv_%7B0%7D%7D+%5C%5C+%7B0%7D+%26+%7B0%7D+%26+%7B1%7D%5Cend%7Barray%7D%5Cright%29%5Cleft%28%5Cbegin%7Barray%7D%7Blll%7D%7BR+1%7D+%26+%7BR+2%7D+%26+%7BT%7D%5Cend%7Barray%7D%5Cright%29%5Cleft%28%5Cbegin%7Barray%7D%7Bl%7D%7BU%7D+%5C%5C+%7BV%7D+%5C%5C+%7B1%7D%5Cend%7Barray%7D%5Cright%29%3DA%28R+1+%5Cquad+R+2+%5Cquad+T%29%5Cleft%28%5Cbegin%7Barray%7D%7Bl%7D%7BU%7D+%5C%5C+%7BV%7D+%5C%5C+%7B1%7D%5Cend%7Barray%7D%5Cright%29+%5C%5C)

我们对于上式做一定的说明。对于不同的图片，内参矩阵 $A$ 为定值；对于同一张图片，内参矩阵 $A$，外参矩阵 $(R1,R2,T)$ 为定值；对于同一张图片上的单点，内参矩阵 $A$，外参矩阵 $(R1,R2,T)$ ，尺度因子 $Z$ 为定值。

我们将 $A(R1,R2,T)$ 记为矩阵 $H$ ，$H$ 即为内参矩阵和外参矩阵的积，记矩阵 $H$ 的三列为 $(H1,H2,H3)$ ，则有：

![](https://www.zhihu.com/equation?tex=%5Cleft%28%5Cbegin%7Barray%7D%7Bl%7D%7Bu%7D+%5C%5C+%7Bv%7D+%5C%5C+%7B1%7D%5Cend%7Barray%7D%5Cright%29%3D%5Cfrac%7B1%7D%7BZ%7D+H%5Cleft%28%5Cbegin%7Barray%7D%7Bl%7D%7BU%7D+%5C%5C+%7BV%7D+%5C%5C+%7B1%7D%5Cend%7Barray%7D%5Cright%29+%3D+%5Cfrac%7B1%7D%7BZ%7D++%5Cleft%5B%5Cbegin%7Barray%7D%7Bccc%7D%7BH_%7B11%7D%7D+%26+%7BH_%7B12%7D%7D+%26+%7BH_%7B13%7D%7D+%5C%5C+%7BH_%7B12%7D%7D+%26+%7BH_%7B22%7D%7D+%26+%7BH_%7B32%7D%7D+%5C%5C+%7BH_%7B31%7D%7D+%26+%7BH_%7B32%7D%7D+%26+%7BH_%7B33%7D%7D%5Cend%7Barray%7D%5Cright%5D%5Cleft%28%5Cbegin%7Barray%7D%7Bl%7D%7BU%7D+%5C%5C+%7BV%7D+%5C%5C+%7B1%7D%5Cend%7Barray%7D%5Cright%29+%5C%5C)

利用上式，消去尺度因子 $Z$，可得：

![](https://www.zhihu.com/equation?tex=u+%3D+%5Cfrac%7BH_%7B11%7DU%2BH_%7B12%7DV%2BH_%7B13%7D%7D%7BH_%7B31%7DU%2BH_%7B32%7DV%2BH_%7B33%7D%7D%5C%5C+v+%3D+%5Cfrac%7BH_%7B21%7DU%2BH_%7B22%7DV%2BH_%7B23%7D%7D%7BH_%7B31%7DU%2BH_%7B32%7DV%2BH_%7B33%7D%7D+%5C%5C+)

此时，尺度因子 $Z$ 已经被消去，因此上式**对于同一张图片上所有的角点均成立**。$(u,v)$ 是像素坐标系下的标定板角点的坐标， $(U,V)$ 是世界坐标系下的标定板角点的坐标。通过图像识别算法，我们可以得到标定板角点的像素坐标 $(u,v)$，又由于标定板的世界坐标系是人为定义好的，标定板上每一个格子的大小是已知的，我们可以计算得到世界坐标系下的 $(U,V)$。

由这里的 $H$ 是齐次矩阵，有 8 个独立未知元素。每一个标定板角点可以提供两个约束方程 $(u,U,V)$ 的对应关系、 $(u,U,V)$ 的对应关系提供了两个约束方程，因此，当一张图片上的标定板角点数量等于 4 时，即可求得该图片对应的矩阵 $H$ 。当一张图片上的标定板角点数量大于 4 时，利用最小二乘法回归最佳的矩阵 $H$。

#### (2)、求解内参矩阵

我们已知了矩阵 $H=A(R1,R2,T)$ ，接下来需要求解相机的内参矩阵 $A$ 。
我们利用 $R1,R2$ 作为旋转矩阵 $R$ 的两列，存在单位正交的关系，即：

![](https://www.zhihu.com/equation?tex=R+1%5E%7BT%7D+R+2%3D0+%5C%5C+R+1%5E%7BT%7D+R+1%3DR+2%5E%7BT%7D+R+2%3D1)

则由 $H$ 和 $R1,R2$ 的关系，可知：

![](https://www.zhihu.com/equation?tex=R1%3D+A%5E%7B-1%7D+H1+%5C%5C+R+2%3D+A%5E%7B-1%7D+H+2)

代入可得：

![](https://www.zhihu.com/equation?tex=H+1%5E%7BT%7D+++A%5E%7B-T%7D+A%5E%7B-1%7D+H+2%3D0+%5C%5C+H+1%5E%7BT%7D++A%5E%7B-T%7D+A%5E%7B-1%7D+H+1+%3D+H+2%5E%7BT%7D+A%5E%7B-T%7D+A%5E%7B-1%7D+H+2%3D1)

另外，我们发现，上述两个约束方程中均存在矩阵 $A^{-T}A^{-1}$ 。因此，我们记 $A^{-T}A^{-1}=B$ ，则 $B$ 为对称阵。我们试图先求解出矩阵 $B$ ，通过矩阵 $B$ 再求解相机的内参矩阵 $A$ 。
同时，为了简便，我们记相机内参矩阵 $A$ 为：

![](https://www.zhihu.com/equation?tex=A%3D%5Cleft%28%5Cbegin%7Barray%7D%7Bcccc%7D%7B%5Cfrac%7Bf%7D%7Bd+X%7D%7D+%26+%7B-%5Cfrac%7Bf%5Ccot+%5Ctheta%7D%7Bd+X%7D%7D+%26+%7Bu_%7B0%7D%7D+%26+%7B0%7D+%5C%5C+%7B0%7D+%26+%7B%5Cfrac%7Bf%7D%7Bd+Y+%5Csin+%5Ctheta%7D%7D+%26+%7Bv_%7B0%7D%7D+%26+%7B0%7D+%5C%5C+%7B0%7D+%26+%7B0%7D+%26+%7B1%7D+%26+%7B0%7D%5Cend%7Barray%7D%5Cright%29+%3D+%5Cleft%5B%5Cbegin%7Barray%7D%7Bccc%7D%7B%5Calpha%7D+%26+%7B%5Cgamma%7D+%26+%7Bu_%7B0%7D%7D+%5C%5C+%7B0%7D+%26+%7B%5Cbeta%7D+%26+%7Bv_%7B0%7D%7D+%5C%5C+%7B0%7D+%26+%7B0%7D+%26+%7B1%7D%5Cend%7Barray%7D%5Cright%5D+%5C%5C)

则：

![](https://www.zhihu.com/equation?tex=A%5E%7B-1%7D%3D%5Cleft%5B%5Cbegin%7Barray%7D%7Bccc%7D%7B%5Cfrac%7B1%7D%7B%5Calpha%7D%7D+%26+%7B-%5Cfrac%7B%5Cgamma%7D%7B%5Calpha+%5Cbeta%7D%7D+%26+%7B%5Cfrac%7B%5Cgamma+v_%7B0%7D-%5Cbeta+u_%7B0%7D%7D%7B%5Calpha+%5Cbeta%7D%7D+%5C%5C+%7B0%7D+%26+%7B%5Cfrac%7B1%7D%7B%5Cbeta%7D%7D+%26+%7B-%5Cfrac%7Bv_%7B0%7D%7D%7B%5Cbeta%7D%7D+%5C%5C+%7B0%7D+%26+%7B0%7D+%26+%7B1%7D%5Cend%7Barray%7D%5Cright%5D+%5C%5C)

则用矩阵 $A$ 表示矩阵 $B$ 得：

![](https://www.zhihu.com/equation?tex=B+%3D+A%5E%7B-T%7D+A%5E%7B-1%7D+%3D+%5Cleft%5B%5Cbegin%7Barray%7D%7Bccc%7D%7B%5Cfrac%7B1%7D%7B%5Calpha%5E%7B2%7D%7D%7D+%26+%7B-%5Cfrac%7B%5Cgamma%7D%7B%5Calpha%5E%7B2%7D+%5Cbeta%7D%7D+%26+%7B%5Cfrac%7B%5Cgamma+v_%7B0%7D-%5Cbeta+u_%7B0%7D%7D%7B%5Calpha%5E%7B2%7D+%5Cbeta%7D%7D+%5C%5C+%7B-%5Cfrac%7B%5Cgamma%7D%7B%5Calpha%5E%7B2%7D+%5Cbeta%7D%7D+%26+%7B%5Cfrac%7B1%7D%7B%5Cbeta%5E%7B2%7D%7D%2B%5Cfrac%7B%5Cgamma%5E%7B2%7D%7D%7B%5Calpha%5E%7B2%7D+%5Cbeta%5E%7B2%7D%7D%7D+%26+%7B%5Cfrac%7B%5Cgamma%5Cleft%28%5Cbeta+u_%7B0%7D-%5Cgamma+v_%7B0%7D%5Cright%29%7D%7B%5Calpha%5E%7B2%7D+%5Cbeta%5E%7B2%7D%7D-%5Cfrac%7Bv_%7B0%7D%7D%7B%5Cbeta%5E%7B2%7D%7D%7D+%5C%5C+%7B%5Cfrac%7B%5Cgamma+v_%7B0%7D-%5Cbeta+u_%7B0%7D%7D%7B%5Calpha%5E%7B2%7D+%5Cbeta%7D%7D+%26+%7B%5Cfrac%7B%5Cgamma%5Cleft%28%5Cbeta+u_%7B0%7D-%5Cgamma+v_%7B0%7D%5Cright%29%7D%7B%5Calpha%5E%7B2%7D+%5Cbeta%5E%7B2%7D%7D-%5Cfrac%7Bv_%7B0%7D%7D%7B%5Cbeta%5E%7B2%7D%7D%7D+%26+%7B%5Cfrac%7B%5Cleft%28%5Cbeta+u_%7B0%7D-%5Cgamma+v_%7B0%7D%5Cright%29%5E%7B2%7D%7D%7B%5Calpha%5E%7B2%7D+%5Cbeta%5E%7B2%7D%7D%2B%5Cfrac%7Bv_%7B0%7D%5E%7B2%7D%7D%7B%5Cbeta%5E%7B2%7D%7D%2B1%7D%5Cend%7Barray%7D%5Cright%5D%3D+%5Cleft%5B%5Cbegin%7Barray%7D%7Blll%7D%7BB_%7B11%7D%7D+%26+%7BB_%7B12%7D%7D+%26+%7BB_%7B13%7D%7D+%5C%5C+%7BB_%7B12%7D%7D+%26+%7BB_%7B22%7D%7D+%26+%7BB_%7B23%7D%7D+%5C%5C+%7BB_%7B13%7D%7D+%26+%7BB_%7B23%7D%7D+%26+%7BB_%7B33%7D%7D%5Cend%7Barray%7D%5Cright%5D+%5C%5C)

注意：由于 $B$ 为对称阵，上式出现了两次 $B_{12},B_{13},B_{23}$ 。
这里，我们可以使用 $B=A^{-T}A^{-1}$ 将前面通过 $R1,R2$ 单位正交得到的约束方程化为：

![](https://www.zhihu.com/equation?tex=H+1%5E%7BT%7D++B+H+2+%3D+0+%5C%5C++H+1%5E%7BT%7D+B+H+1%3DH+2%5E%7BT%7DB+H+2%3D1)

因此，为了求解矩阵 $B$ ，我们必须计算 $B{^T_i}BH_j$ 。则：

![](https://www.zhihu.com/equation?tex=H_%7Bi%7D%5E%7BT%7D+B+H_%7Bj%7D%3D%5Cleft%5B%5Cbegin%7Barray%7D%7Bccc%7D%7BH_%7B1+i%7D%7D+%26+%7BH_%7B2+i%7D%7D+%26+%7BH_%7B3+i%7D%7D%5Cend%7Barray%7D%5Cright%5D%5Cleft%5B%5Cbegin%7Barray%7D%7Bccc%7D%7BB_%7B11%7D%7D+%26+%7BB_%7B12%7D%7D+%26+%7BB_%7B13%7D%7D+%5C%5C+%7BB_%7B12%7D%7D+%26+%7BB_%7B22%7D%7D+%26+%7BB_%7B32%7D%7D+%5C%5C+%7BB_%7B31%7D%7D+%26+%7BB_%7B32%7D%7D+%26+%7BB_%7B33%7D%7D%5Cend%7Barray%7D%5Cright%5D%5Cleft%5B%5Cbegin%7Barray%7D%7Bc%7D%7BH_%7B1+j%7D%7D+%5C%5C+%7BH_%7B2+j%7D%7D+%5C%5C+%7BH_%7B3+j%7D%7D%5Cend%7Barray%7D%5Cright%5D+%5C%5C++%3D+%5Cleft%5B%5Cbegin%7Barray%7D%7Bllll%7D%7BH_%7B1+i%7D+H_%7B1+j%7D%7D+%26+%7BH_%7B1+i%7D+H_%7B2+j%7D%2BH_%7B2+i%7D+H_%7B1+j%7D%7D+%26+%7BH_%7B2+i%7D+H_%7B2+j%7D%7D+%26+%7BH_%7B1+i%7D+H_%7B3+j%7D%2BH_%7B3+i%7D+H_%7B1+j%7D%7D+%26+%7BH_%7B2+i%7D+H_%7B3+j%7D%2BH_%7B3+i%7D+H_%7B2+j%7D%7D+%26+%7BH_%7B3+i%7D+H_%7B3+j%7D%7D%5Cend%7Barray%7D%5Cright%5D+%5Cleft%5B%5Cbegin%7Barray%7D%7Bl%7D%7BB_%7B11%7D%7D+%5C%5C+%7BB_%7B12%7D%7D+%5C%5C+%7BB_%7B22%7D%7D+%5C%5C+%7BB_%7B13%7D%7D+%5C%5C+%7BB_%7B23%7D%7D+%5C%5C+%7BB_%7B33%7D%7D%5Cend%7Barray%7D%5Cright%5D)
![](https://www.zhihu.com/equation?tex=H_%7Bi%7D%5E%7BT%7D+B+H_%7Bj%7D%3D%5Cleft%5B%5Cbegin%7Barray%7D%7Bccc%7D%7BH_%7B1+i%7D%7D+%26+%7BH_%7B2+i%7D%7D+%26+%7BH_%7B3+i%7D%7D%5Cend%7Barray%7D%5Cright%5D%5Cleft%5B%5Cbegin%7Barray%7D%7Bccc%7D%7BB_%7B11%7D%7D+%26+%7BB_%7B12%7D%7D+%26+%7BB_%7B13%7D%7D+%5C%5C+%7BB_%7B12%7D%7D+%26+%7BB_%7B22%7D%7D+%26+%7BB_%7B32%7D%7D+%5C%5C+%7BB_%7B31%7D%7D+%26+%7BB_%7B32%7D%7D+%26+%7BB_%7B33%7D%7D%5Cend%7Barray%7D%5Cright%5D%5Cleft%5B%5Cbegin%7Barray%7D%7Bc%7D%7BH_%7B1+j%7D%7D+%5C%5C+%7BH_%7B2+j%7D%7D+%5C%5C+%7BH_%7B3+j%7D%7D%5Cend%7Barray%7D%5Cright%5D+%5C%5C++%3D+%5Cleft%5B%5Cbegin%7Barray%7D%7Bllll%7D%7BH_%7B1+i%7D+H_%7B1+j%7D%7D+%26+%7BH_%7B1+i%7D+H_%7B2+j%7D%2BH_%7B2+i%7D+H_%7B1+j%7D%7D+%26+%7BH_%7B2+i%7D+H_%7B2+j%7D%7D+%26+%7BH_%7B1+i%7D+H_%7B3+j%7D%2BH_%7B3+i%7D+H_%7B1+j%7D%7D+%26+%7BH_%7B2+i%7D+H_%7B3+j%7D%2BH_%7B3+i%7D+H_%7B2+j%7D%7D+%26+%7BH_%7B3+i%7D+H_%7B3+j%7D%7D%5Cend%7Barray%7D%5Cright%5D+%5Cleft%5B%5Cbegin%7Barray%7D%7Bl%7D%7BB_%7B11%7D%7D+%5C%5C+%7BB_%7B12%7D%7D+%5C%5C+%7BB_%7B22%7D%7D+%5C%5C+%7BB_%7B13%7D%7D+%5C%5C+%7BB_%7B23%7D%7D+%5C%5C+%7BB_%7B33%7D%7D%5Cend%7Barray%7D%5Cright%5D)

上述方程看起来有点复杂，但是其实不然，我们可以记：

![](https://www.zhihu.com/equation?tex=v_%7Bi+j%7D%3D%5Cleft%5B%5Cbegin%7Barray%7D%7Bllll%7D%7BH_%7B1+i%7D+H_%7B1+j%7D%7D+%26+%7BH_%7B1+i%7D+H_%7B2+j%7D%2BH_%7B2+i%7D+H_%7B1+j%7D%7D+%26+%7BH_%7B2+i%7D+H_%7B2+j%7D%7D+%26+%7BH_%7B1+i%7D+H_%7B3+j%7D%2BH_%7B3+i%7D+H_%7B1+j%7D%7D+%26+%7BH_%7B2+i%7D+H_%7B3+j%7D%2BH_%7B3+i%7D+H_%7B2+j%7D%7D+%26+%7BH_%7B3+i%7D+H_%7B3+j%7D%7D%5Cend%7Barray%7D%5Cright%5D%5E%7BT%7D+%5C%5C+b%3D%5Cleft%5B%5Cbegin%7Barray%7D%7Bllllll%7D%7BB_%7B11%7D%7D+%26+%7BB_%7B12%7D%7D+%26+%7BB_%7B22%7D%7D+%26+%7BB_%7B13%7D%7D+%26+%7BB_%7B23%7D%7D+%26+%7BB_%7B33%7D%7D%5Cend%7Barray%7D%5Cright%5D%5E%7BT%7D)

则上述方程化为： $H{^T_i}BH_j=v_{ij}b$
此时，通过 $R1,R2$ 单位正交得到的约束方程可化为：

![](https://www.zhihu.com/equation?tex=v_%7B12%7D%5E%7BT%7D+b%3D0+%5C%5C+v_%7B11%7D%5E%7BT%7D+b%3D++v_%7B22%7D%5E%7BT%7D+b%3D1%5C%5C)

即：
![](https://www.zhihu.com/equation?tex=%5Cleft%5B%5Cbegin%7Barray%7D%7Bc%7D%7Bv_%7B12%7D%5E%7BT%7D%7D+%5C%5C+%7Bv_%7B11%7D%5E%7BT%7D-v_%7B22%7D%5E%7BT%7D%7D%5Cend%7Barray%7D%5Cright%5D+b%3Dv+b%3D0+%5C%5C)

其中，矩阵 $v= \begin{bmatrix}
v^t_{12} \\   
v^T_{11}-v^T_{22}\\
\end{bmatrix}$

由于矩阵 $H$ 已知，矩阵 $v$ 又全部由矩阵 $H$ 的元素构成，因此矩阵 $v$ 已知。

此时，我们只要求解出向量 $b$ ，即可得到矩阵 $B$ 。每张标定板图片可以提供一个 $vb=0$ 的约束关系，该约束关系含有两个约束方程。但是，向量 $b$ 有 6 个未知元素。因此，单张图片提供的两个约束方程是不足以解出来向量 $b$。因此，我们只要取 3 张标定板照片，得到 3 个 $vb=0$ 的约束关系，即 6 个方程，即可求解向量 $b$。当标定板图片的个数大于 3 时（事实上一般需要 15 到 20 张标定板图片），可采用最小二乘拟合最佳的向量 $b$ ，并得到矩阵 $B$。

![](https://www.zhihu.com/equation?tex=B%3D%5Cleft%5B%5Cbegin%7Barray%7D%7Bccc%7D%7B%5Cfrac%7B1%7D%7B%5Calpha%5E%7B2%7D%7D%7D+%26+%7B-%5Cfrac%7B%5Cgamma%7D%7B%5Calpha%5E%7B2%7D+%5Cbeta%7D%7D+%26+%7B%5Cfrac%7B%5Cgamma+v_%7B0%7D-%5Cbeta+u_%7B0%7D%7D%7B%5Calpha%5E%7B2%7D+%5Cbeta%7D%7D+%5C%5C+%7B-%5Cfrac%7B%5Cgamma%7D%7B%5Calpha%5E%7B2%7D+%5Cbeta%7D%7D+%26+%7B%5Cfrac%7B1%7D%7B%5Cbeta%5E%7B2%7D%7D%2B%5Cfrac%7B%5Cgamma%5E%7B2%7D%7D%7B%5Calpha%5E%7B2%7D+%5Cbeta%5E%7B2%7D%7D%7D+%26+%7B%5Cfrac%7B%5Cgamma%5Cleft%28%5Cbeta+u_%7B0%7D-%5Cgamma+v_%7B0%7D%5Cright%29%7D%7B%5Calpha%5E%7B2%7D+%5Cbeta%5E%7B2%7D%7D-%5Cfrac%7Bv_%7B0%7D%7D%7B%5Cbeta%5E%7B2%7D%7D%7D+%5C%5C+%7B%5Cfrac%7B%5Cgamma+v_%7B0%7D-%5Cbeta+u_%7B0%7D%7D%7B%5Calpha%5E%7B2%7D+%5Cbeta%7D%7D+%26+%7B%5Cfrac%7B%5Cgamma%5Cleft%28%5Cbeta+u_%7B0%7D-%5Cgamma+v_%7B0%7D%5Cright%29%7D%7B%5Calpha%5E%7B2%7D+%5Cbeta%5E%7B2%7D%7D-%5Cfrac%7Bv_%7B0%7D%7D%7B%5Cbeta%5E%7B2%7D%7D%7D+%26+%7B%5Cfrac%7B%5Cleft%28%5Cbeta+u_%7B0%7D-%5Cgamma+v_%7B0%7D%5Cright%29%5E%7B2%7D%7D%7B%5Calpha%5E%7B2%7D+%5Cbeta%5E%7B2%7D%7D%2B%5Cfrac%7Bv_%7B0%7D%5E%7B2%7D%7D%7B%5Cbeta%5E%7B2%7D%7D%2B1%7D%5Cend%7Barray%7D%5Cright%5D%3D%5Cleft%5B%5Cbegin%7Barray%7D%7Bccc%7D%7BB_%7B11%7D%7D+%26+%7BB_%7B21%7D%7D+%26+%7BB_%7B13%7D%7D+%5C%5C+%7BB_%7B21%7D%7D+%26+%7BB_%7B22%7D%7D+%26+%7BB_%7B23%7D%7D+%5C%5C+%7BB_%7B13%7D%7D+%26+%7BB_%7B23%7D%7D+%26+%7BB_%7B33%7D%7D%5Cend%7Barray%7D%5Cright%5D+%5C%5C)

根据矩阵 $B$ 的元素和相机内参 $\alpha,\beta,\gamma,u_0,v_0$的对应关系（如上式），可得到：

![](https://www.zhihu.com/equation?tex=+%5Cbegin%7Baligned%7D++v_%7B0%7D%3D%26+%5Cfrac%7BB_%7B12%7D+B_%7B13%7D-B_%7B11%7D+B_%7B23%7D%7D%7B+B_%7B11%7D+B_%7B22%7D-B_%7B12%7D%5E%7B2%7D%7D+%5C%5C+%5Calpha+%26%3D%5Csqrt%7B%5Cfrac%7B1%7D%7BB_%7B11%7D%7D%7D+%5C%5C++%5Cbeta%3D%26+%5Csqrt%7B%5Cfrac%7BB_%7B11%7D%7D%7BB_%7B11%7D+B_%7B22%7D-B_%7B12%7D%5E%7B2%7D%7D%7D+%5C%5C+%5Cgamma%3D%26-B_%7B12%7D+%5Calpha%5E%7B2%7D+%5Cbeta+%5C%5C++u_%7B0%7D%3D%26+%5Cfrac%7B%5Cgamma+v_%7B0%7D%7D%7B%5Cbeta%7D-B_%7B13%7D+%5Calpha%5E%7B2%7D%5Cend%7Baligned%7D%5C%5C)

即可求得相机的内参矩阵![](https://www.zhihu.com/equation?tex=A%3D%5Cleft%28%5Cbegin%7Barray%7D%7Bcccc%7D%7B%5Cfrac%7Bf%7D%7Bd+X%7D%7D+%26+%7B-%5Cfrac%7Bf%5Ccot+%5Ctheta%7D%7Bd+X%7D%7D+%26+%7Bu_%7B0%7D%7D+%26+%7B0%7D+%5C%5C+%7B0%7D+%26+%7B%5Cfrac%7Bf%7D%7Bd+Y+%5Csin+%5Ctheta%7D%7D+%26+%7Bv_%7B0%7D%7D+%26+%7B0%7D+%5C%5C+%7B0%7D+%26+%7B0%7D+%26+%7B1%7D+%26+%7B0%7D%5Cend%7Barray%7D%5Cright%29+%3D+%5Cleft%5B%5Cbegin%7Barray%7D%7Bccc%7D%7B%5Calpha%7D+%26+%7B%5Cgamma%7D+%26+%7Bu_%7B0%7D%7D+%5C%5C+%7B0%7D+%26+%7B%5Cbeta%7D+%26+%7Bv_%7B0%7D%7D+%5C%5C+%7B0%7D+%26+%7B0%7D+%26+%7B1%7D%5Cend%7Barray%7D%5Cright%5D) 。

#### (3)、求解外参矩阵

这里再次强调一下，对于同一个相机，相机的内参矩阵取决于相机的内部参数，无论标定板和相机的位置关系是怎么样的，相机的内参矩阵不变。这也正是在第 2 部分“求解内参矩阵”中，我们可以利用不同的图片（标定板和相机位置关系不同）获取的矩阵 $H$ ，共同求解相机内参矩阵 $A$ 的原因。

但是，外参矩阵反映的是标定板和相机的位置关系。对于不同的图片，标定板和相机的位置关系已经改变，此时每一张图片对应的外参矩阵都是不同的。

在关系： $A(R1\ R2\ T)=H$ 中，我们已经求解得到了矩阵 $H$（对于同一张图片相同，对于不同的图片不同）、矩阵 $A$（对于不同的图片都相同）。通过公式： $(R1\ R2\ T)=A^{-1}H$ ，即可求得每一张图片对应的外参矩阵 $(R1\ R2\ T)$ 。

注意，这里值得指出，完整的外参矩阵为 $\begin{bmatrix}R&T \\ 0&1\\ \end{bmatrix}$ 。但是，由于张正友标定板将世界坐标系的原点选取在棋盘格上，则棋盘格上任一点的物理坐标 $W=0$，将旋转矩阵的 $R$ 的第三列 $R3$ 消掉，因此， $R3$ 在坐标转化中并没有作用。但是 $R3$ 要使得 $R$ 满足旋转矩阵的性质，即列与列之间单位正交，因此可以通过向量 $R1,R2$ 的叉乘，即 $R3=R1*R2$ ，计算得到 $R3$。

此时，相机的内参矩阵和外参矩阵均已得到。

注：以上推导都是假设不存在畸变参数的情况下成立的。但是事实上，相机是存在畸变参数的，因此，张正友标定法还需要通过 L-M 算法对于参数进行迭代优化。

#### (4)、标定相机的畸变参数

张正友标定法仅仅考虑了畸变模型中影响较大的径向畸变。
径向畸变公式（2 阶）如下：
![](https://www.zhihu.com/equation?tex=%5Cbegin%7Barray%7D%7Bl%7D%7B%5Chat%7Bx%7D%3Dx%5Cleft%281%2Bk_%7B1%7D+r%5E%7B2%7D%2Bk_%7B2%7D+r%5E%7B4%7D%5Cright%29%7D+%5C%5C+%7B%5Chat%7By%7D%3Dy%5Cleft%281%2Bk_%7B1%7D+r%5E%7B2%7D%2Bk_%7B2%7D+r%5E%7B4%7D%5Cright%29%7D%5Cend%7Barray%7D+%5C%5C)

其中，$(x,y),(\hat{x},\hat{y})$ 分别为理想的无畸变的归一化的图像坐标、畸变后的归一化图像坐标，$r$ 为图像像素点到图像中心点的距离，即 $r^2=x^2+y^2$。

图像坐标和像素坐标的转化关系为：

![](https://www.zhihu.com/equation?tex=%5Cleft%28%5Cbegin%7Barray%7D%7Bl%7D%7Bu%7D+%5C%5C+%7Bv%7D+%5C%5C+%7B1%7D%5Cend%7Barray%7D%5Cright%29+%3D+%5Cleft%28%5Cbegin%7Barray%7D%7Bccc%7D%7B%5Cfrac%7B1%7D%7Bd+X%7D%7D+%26+%7B-%5Cfrac%7B%5Ccot+%5Ctheta%7D%7Bd+X%7D%7D+%26+%7Bu_%7B0%7D%7D+%5C%5C+%7B0%7D+%26+%7B%5Cfrac%7B1%7D%7Bd+Y+%5Csin+%5Ctheta%7D%7D+%26+%7Bv_%7B0%7D%7D+%5C%5C++%7B0%7D%26+%7B0%7D+%26%7B1%7D%5Cend%7Barray%7D%5Cright%29%5Cleft%28%5Cbegin%7Barray%7D%7Bl%7D%7Bx%7D+%5C%5C+%7By%7D+%5C%5C+%7B1%7D%5Cend%7Barray%7D%5Cright%29%5C%5C)

其中，$(u,v)$ 为理想的无畸变的像素坐标。由于 $\theta$ 接近于 $90^{\circ}$ ，则上式近似为：

![](https://www.zhihu.com/equation?tex=%5Cbegin%7Barray%7D%7Bl%7D%7Bu%3D%5Cfrac%7Bx%7D%7BdX%7D%2Bu_0%7D+%5C%5C+%7Bv%3D%5Cfrac%7By%7D%7BdY%7D%2Bv_0%7D%5Cend%7Barray%7D%5C%5C)

同理可得畸变后的像素坐标 $(\hat{u},\hat{v})$ 的表达式为：

![](https://www.zhihu.com/equation?tex=%5Cbegin%7Barray%7D%7Bl%7D%7B%5Chat%7Bu%7D%3D%5Cfrac%7B%5Chat%7Bx%7D%7D%7BdX%7D%2Bu_0%7D+%5C%5C+%7B%5Chat%7Bv%7D%3D%5Cfrac%7B%5Chat%7By%7D%7D%7BdY%7D%2Bv_0%7D%5Cend%7Barray%7D%5C%5C)

代入径向畸变公式（2 阶）则有：

![](https://www.zhihu.com/equation?tex=%5Cbegin%7Barray%7D%7Bl%7D%7B%5Chat%7Bu%7D-u_0%3D%5Cleft%28u-u_%7B0%7D%5Cright%29%5Cleft%281%2Bk_%7B1%7D+r%5E%7B2%7D%2Bk_%7B2%7D+r%5E%7B4%7D%5Cright%29%7D+%5C%5C+%7B%5Chat%7Bv%7D-v_0%3D%5Cleft%28v-v_%7B0%7D%5Cright%29%5Cleft%281%2Bk_%7B1%7D+r%5E%7B2%7D%2Bk_%7B2%7D+r%5E%7B4%7D%5Cright%29%7D%5Cend%7Barray%7D+%5C%5C)

可化简得：

![](https://www.zhihu.com/equation?tex=%5Cbegin%7Barray%7D%7Bl%7D%7B%5Chat%7Bu%7D%3Du%2B%5Cleft%28u-u_%7B0%7D%5Cright%29%5Cleft%28k_%7B1%7D+r%5E%7B2%7D%2Bk_%7B2%7D+r%5E%7B4%7D%5Cright%29%7D+%5C%5C+%7B%5Chat%7Bv%7D%3Dv%2B%5Cleft%28v-v_%7B0%7D%5Cright%29%5Cleft%28k_%7B1%7D+r%5E%7B2%7D%2Bk_%7B2%7D+r%5E%7B4%7D%5Cright%29%7D%5Cend%7Barray%7D+%5C%5C)

即为：
![](https://www.zhihu.com/equation?tex=%5Cleft%5B%5Cbegin%7Barray%7D%7Bcc%7D%7B%5Cleft%28u-u_%7B0%7D%5Cright%29+r%5E%7B2%7D%7D+%26+%7B%5Cleft%28u-u_%7B0%7D%5Cright%29+r%5E%7B4%7D%7D+%5C%5C+%7B%5Cleft%28v-v_%7B0%7D%5Cright%29+r%5E%7B2%7D%7D+%26+%7B%5Cleft%28v-v_%7B0%7D%5Cright%29+r%5E%7B4%7D%7D%5Cend%7Barray%7D%5Cright%5D%5Cleft%5B%5Cbegin%7Barray%7D%7Bl%7D%7Bk_%7B1%7D%7D+%5C%5C+%7Bk_%7B2%7D%7D%5Cend%7Barray%7D%5Cright%5D%3D%5Cleft%5B%5Cbegin%7Barray%7D%7Bc%7D%7B%5Chat%7Bu%7D-u%7D+%5C%5C+%7B%5Chat%7Bv%7D-v%7D%5Cend%7Barray%7D%5Cright%5D+%5C%5C)

每一个角点，只要知道畸变后的像素坐标 $(\hat{u},\hat{v})$ 、理想的无畸变的像素坐标 $(u,v)$ ，就可以构造两个上述等式。那么，有 m 幅图像，每幅图像上有 n 个标定板角点，则将得到的所有等式组合起来，可以得到 mn 个未知数为 $k=[k_1,k_2]^T$ 的约束方程，将约束方程系数矩阵记为 $D$ ，等式右端非齐次项记为 $d$ ，可将其记着矩阵形式：$Dk=d$之后，利用最小二乘法可得：![](https://www.zhihu.com/equation?tex=k%3D%5Cleft%5B%5Cbegin%7Barray%7D%7Bl%7D%7Bk_%7B1%7D%7D+%5C%5C+%7Bk_%7B2%7D%7D%5Cend%7Barray%7D%5Cright%5D%3D%5Cleft%28D%5E%7BT%7D+D%5Cright%29%5E%7B-1%7D+D%5E%7BT%7D+d+%5C%5C)

此时，相机的畸变矫正参数已经标定好。
那么，如何获得畸变后的像素坐标 $(\hat{u},\hat{v})$ 和理想的无畸变的像素坐标 $(u,v)$ 呢？
$(\hat{u},\hat{v})$ 可以通过识别标定板的角点获得， $(u,v)$ 可以通过如下方法近似求得。世界坐标系下每一个角点的坐标 $(U,V)$ 是可以计算得到的，我们利用已经求得的外参矩阵 $(R1\ R2\ T)$ 和内参矩阵 $A$ 进行反投影。

![](https://www.zhihu.com/equation?tex=Z%5Cleft%28%5Cbegin%7Barray%7D%7Bl%7D%7Bu%7D+%5C%5C+%7Bv%7D+%5C%5C+%7B1%7D%5Cend%7Barray%7D%5Cright%29%3DA%28R+1+%5Cquad+R+2+%5Cquad+T%29%5Cleft%28%5Cbegin%7Barray%7D%7Bl%7D%7BU%7D+%5C%5C+%7BV%7D+%5C%5C+%7B1%7D%5Cend%7Barray%7D%5Cright%29+%3DH%5Cleft%28%5Cbegin%7Barray%7D%7Bl%7D%7BU%7D+%5C%5C+%7BV%7D+%5C%5C+%7B1%7D%5Cend%7Barray%7D%5Cright%29+%5C%5C)

利用上式，消去尺度因子 $Z$，可得：

![](https://www.zhihu.com/equation?tex=u+%3D+%5Cfrac%7BH_%7B11%7DU%2BH_%7B12%7DV%2BH_%7B13%7D%7D%7BH_%7B31%7DU%2BH_%7B32%7DV%2BH_%7B33%7D%7D%5C%5C+v+%3D+%5Cfrac%7BH_%7B21%7DU%2BH_%7B22%7DV%2BH_%7B23%7D%7D%7BH_%7B31%7DU%2BH_%7B32%7DV%2BH_%7B33%7D%7D+%5C%5C+)

即可得到理想的、无畸变的像素坐标 $(u,v)$。当然，由于外参矩阵 $(R1\ R2\ T)$ 和内参矩阵 $A$ 是在有畸变的情况下获得的，这里得到的像素坐标 $(u,v)$ 并不是完全理想的、无畸变的。我们的总逻辑是，在进行内参矩阵和外参矩阵的求解的时候，我们假设不存在畸变；在进行畸变系数的求解的时候，我们假设求得的内参矩阵和外参矩阵是无误差的。最后，我们再通过 L-M 算法对于参数进行迭代优化。

需要指出，上述公式推导的时候以 2 阶径向畸变为例，但实际上更高阶的径向畸变同理，只是需要的约束方程个数更多而已。

#### (5)、L-M 算法参数优化

从上述推导过程就可以看出，张正友标定法是有很多近似的，所以仅仅利用上述的过程进行标定误差肯定是很大的。所以张正友标定法还利用 L-M（Levenberg-Marquardt）算法对参数进行了优化。
##### 5.1、最小二乘法
![](https://www.zhihu.com/equation?tex=x%3Darg%5Cmin_%7Bx%7D+%7BF%28x%29%7D%3Darg%5Cmin_%7Bx%7D+%5Cfrac%7B1%7D%7B2%7D+%5Csum_%7Bi%3D1%7D%5EN%5Cparallel+f%28x%29+%5Cparallel+%5E2+%5C%5C+F%28x%29%3D%5Cfrac%7B1%7D%7B2%7D+%5Csum_%7Bi%3D1%7D%5EN%5Cparallel+f%28x%29+%5Cparallel+%5E2%3D%5Cfrac%7B1%7D%7B2%7D%5Cparallel%5Cmathbf%7Bf%7D%28x%29%5Cparallel%5E2%3D%5Cfrac%7B1%7D%7B2%7D%5Cmathbf%7Bf%7D%28x%29%5ET%5Cmathbf%7Bf%7D%28x%29)
将 $f$ 一阶泰勒展开：
![](https://www.zhihu.com/equation?tex=%5Cmathbf%7Bf%7D%28x%2Bh%29%3D%5Cmathbf%7Bf%7D%28x%29%2B%5Cmathbf%7BJ%7D%28x%29+h+%2B+O%28h%5ETh%29+%5C%5C+)

去掉高阶项，带入到 $F$ :
![](https://www.zhihu.com/equation?tex=F%28x%2Bh%29%5Capprox+L%28h%29%3D%5Cfrac%7B1%7D%7B2%7D%5Cmathbf%7Bf%7D%5ET%5Cmathbf%7Bf%7D%2Bh%5ET%5Cmathbf%7BJ%7D%5Cmathbf%7Bf%7D%2B%5Cfrac%7B1%7D%7B2%7Dh%5ET%5Cmathbf%7BJ%7D%5ET%5Cmathbf%7BJ%7Dh+%5C%5C)

阻尼法的的思想是再加入一个阻尼项![](https://www.zhihu.com/equation?tex=+%5Cfrac%7B1%7D%7B2%7D%5Cmu+h%5ETh)：
![](https://www.zhihu.com/equation?tex=h%3Darg%5Cmin_h+%7B%5Cmathbf%7BG%7D%28h%29%7D+%3D+arg%5Cmin_h+%5Cfrac%7B1%7D%7B2%7D%5Cmathbf%7Bf%7D%5ET%5Cmathbf%7Bf%7D%2Bh%5ET%5Cmathbf%7BJ%7D%5ET%5Cmathbf%7Bf%7D%2B%5Cfrac%7B1%7D%7B2%7Dh%5ET%5Cmathbf%7BJ%7D%5ET%5Cmathbf%7BJ%7Dh+%2B+%5Cfrac%7B1%7D%7B2%7D%5Cmu+h%5ETh%5C%5C)

对上式求偏导数，并令为０．
![](https://www.zhihu.com/equation?tex=%5Cmathbf%7BJ%7D%5ETf%2B%5Cmathbf%7BJ%7D%5ET%5Cmathbf%7BJ%7Dh%2B%5Cmu+h%3D+0+%5C%5C+%28%5Cmathbf%7BJ%7D%5ET%5Cmathbf%7BJ%7D%2B%5Cmu+%5Cmathbf%7BI%7D%29h%3D-%5Cmathbf%7BJ%7D%5ETf%5C%5C+%28%5Cmathbf%7BH%7D%2B%5Cmu+%5Cmathbf%7BI%7D+%29h%3D-g)


阻尼参数 $\mu$ 的作用有：

1. 对与 $\mu>0$，$(H+\mu I)$ 正定，保证了 $h$ 是梯度下降的方向。
2. 当 $\mu$ 较大时:![](https://www.zhihu.com/equation?tex=h%5Capprox-%5Cfrac%7B1%7D%7B%5Cmu%7Dg%3D-%5Cfrac%7B1%7D%7B%5Cmu%7DF%27%28x%29)，其实就是梯度、最速下降法，当离最终结果较远的时候，很好。
3. 当 $\mu$ 较小时，方法接近与高斯牛顿，当离最终结果很近时，可以获得二次收敛速度，很好。
看来，$\mu$ 的选取很重要。初始时，取
![](https://www.zhihu.com/equation?tex=%5Cmathbf%7BA%7D_0%3D%5Cmathbf%7BJ%7D%28x_0%29%5ET%5Cmathbf%7BJ%7D%28x_0%29%5C%5C+%5Cmu_0%3D%5Ctau+%5Ccdot+%5Cmax_i%5C%7Ba_%7Bii%7D%5E0%5C%7D)

其他情况，利用cost增益来确定:![](https://www.zhihu.com/equation?tex=%5Cvarrho%3D%5Cfrac%7BF%28x%29-f%28x%2Bh%29%7D%7B+L%280%29-L%28h%29%7D+%5C%5C)

**迭代终止条件**
> １．一阶导数为０： ![](https://www.zhihu.com/equation?tex=F%27%28x%29%3Dg%28x%29%3D0)，使用![](https://www.zhihu.com/equation?tex=%5Cparallel+g%28x%29+%5Cparallel+%3C+%5Cvarepsilon_1), $\varepsilon_1$ 是设定的终止条件；
> ２．$ｘ$变化步距离足够小，![](https://www.zhihu.com/equation?tex=%5Cparallel+h%5Cparallel%3D%5Cparallel+x_%7Bnew%7D-x+%5Cparallel+%3C+%5Cvarepsilon_2%28+%5Cparallel+x+%5Cparallel+%2B+%5Cvarepsilon_2+%29)；
> ３．超过最大迭代次数。

##### 5.2、LM算法的步骤
![2022-03-07_18-09.png](https://s2.loli.net/2022/03/07/GsVFUkxSmCunOB1.png)

##### 5.3、算法实现

问题：（高斯牛顿同款问题）非线性方程: ![](https://www.zhihu.com/equation?tex=y%3Dexp%28ax%5E2%2Bbx%2Bc%29) ，给定 $N$ 组观测数据 ${x_i,y_i}$ ，求系数 $X=[a,b,c]^T$ .
分析：![](https://www.zhihu.com/equation?tex=f%28X%29%3Dy-exp%28ax%5E2%2Bbx%2Bc%29),$N$ 组数据可以组成一个大的非线性方程组
![](https://www.zhihu.com/equation?tex=F%28X%29%3D%5Cleft%5B%5Cbegin%7Barray%7D%5Bc%5D%7Bc%7D+y_1-exp%28ax_1%5E2%2Bbx_1%2Bc%29%5C%5C+%5Cdots%5C%5C+y_N-exp%28ax_N%5E2%2Bbx_N%2Bc%29%5Cend%7Barray%7D+%5Cright%5D)

我们可以构建一个最小二乘问题：![](https://www.zhihu.com/equation?tex=x+%3D+%5Cmathrm%7Barg%7D%5Cmin_%7Bx%7D%5Cfrac%7B1%7D%7B2%7D%5Cparallel+F%28X%29+%5Cparallel%5E2)

要求解这个问题，根据推导部分可知，需要求解雅克比。
![](https://www.zhihu.com/equation?tex=J%28X%29%3D%5Cleft%5B%5Cbegin%7Bmatrix%7D+-x_1%5E2exp%28ax_1%5E2%2Bbx_1%2Bc%29+%26+-x_1exp%28ax_1%5E2%2Bbx_1%2Bc%29+%26-exp%28ax_1%5E2%2Bbx_1%2Bc%29+%5C%5C+%5Cdots+%26+%5Cdots+%26+%5Cdots+%5C%5C+-x_N%5E2exp%28ax_N%5E2%2Bbx_N%2Bc%29+%26+-x_Nexp%28ax_N%5E2%2Bbx_N%2Bc%29+%26-exp%28ax_N%5E2%2Bbx_N%2Bc%29+%5Cend%7Bmatrix%7D+%5Cright%5D)

```c++
#include <iostream>
#include <eigen3/Eigen/Core>
#include <eigen3/Eigen/Dense>
#include <opencv2/opencv.hpp>
#include <eigen3/Eigen/Cholesky>
#include <chrono>

/* 计时类 */
class Runtimer{
public:
    inline void start()
    {
        t_s_  = std::chrono::steady_clock::now();
    }
    
    inline void stop()
    {
        t_e_ = std::chrono::steady_clock::now();
    }
    
    inline double duration()
    {
        return std::chrono::duration_cast<std::chrono::duration<double>>(t_e_ - t_s_).count() * 1000.0;
    }
    
private:
    std::chrono::steady_clock::time_point t_s_; //start time ponit
    std::chrono::steady_clock::time_point t_e_; //stop time point
};

/*  优化方程 */
class LevenbergMarquardt{
public:
    LevenbergMarquardt(double* a, double* b, double* c):
    a_(a), b_(b), c_(c)
    {
        epsilon_1_ = 1e-6;
        epsilon_2_ = 1e-6;
        max_iter_ = 50;
        is_out_ = true;
    }
    
    void setParameters(double epsilon_1, double epsilon_2, int max_iter, bool is_out)
    {
        epsilon_1_ = epsilon_1;
        epsilon_2_ = epsilon_2;
        max_iter_ = max_iter;
        is_out_ = is_out;
    }
    
    void addObservation(const double& x, const double& y)
    {
        obs_.push_back(Eigen::Vector2d(x, y));
    }
    
    void calcJ_fx()
    {
        J_ .resize(obs_.size(), 3);
        fx_.resize(obs_.size(), 1);
        
        for ( size_t i = 0; i < obs_.size(); i ++)
        {
            const Eigen::Vector2d& ob = obs_.at(i);
            const double& x = ob(0);
            const double& y = ob(1);
            double j1 = -x*x*exp(*a_ * x*x + *b_*x + *c_);
            double j2 = -x*exp(*a_ * x*x + *b_*x + *c_);
            double j3 = -exp(*a_ * x*x + *b_*x + *c_);
            J_(i, 0 ) = j1;
            J_(i, 1) = j2;
            J_(i, 2) = j3;
            fx_(i, 0) = y - exp( *a_ *x*x + *b_*x +*c_);
        }
    }
    
    void calcH_g()
    {
        H_ = J_.transpose() * J_;
        g_ = -J_.transpose() * fx_;
    }
        
    double getCost()
    {
        Eigen::MatrixXd cost= fx_.transpose() * fx_;
        return cost(0,0);
    }
    
    double F(double a, double b, double c)
    {
        Eigen::MatrixXd fx;
        fx.resize(obs_.size(), 1);
        
        for ( size_t i = 0; i < obs_.size(); i ++)
        {
            const Eigen::Vector2d& ob = obs_.at(i);
            const double& x = ob(0);
            const double& y = ob(1);
            fx(i, 0) = y - exp( a *x*x + b*x +c);
        }
        Eigen::MatrixXd F = 0.5 * fx.transpose() * fx;
        return F(0,0);
    }
    
    double L0_L( Eigen::Vector3d& h)
    {
           Eigen::MatrixXd L = -h.transpose() * J_.transpose() * fx_ - 0.5 * h.transpose() * J_.transpose() * J_ * h;
           return L(0,0);
    }

    void solve()
    {
        int k = 0;
        double nu = 2.0;
        calcJ_fx();
        calcH_g();
        bool found = ( g_.lpNorm<Eigen::Infinity>() < epsilon_1_ );
        
        std::vector<double> A;
        A.push_back( H_(0, 0) );
        A.push_back( H_(1, 1) );
        A.push_back( H_(2,2) );
        auto max_p = std::max_element(A.begin(), A.end());
        double mu = *max_p;
        
        double sumt =0;

        while ( !found && k < max_iter_)
        {
            Runtimer t;
            t.start();
            
            k = k +1;
            Eigen::Matrix3d G = H_ + mu * Eigen::Matrix3d::Identity();
            Eigen::Vector3d h = G.ldlt().solve(g_);
            
            if( h.norm() <= epsilon_2_ * ( sqrt(*a_**a_ + *b_**b_ + *c_**c_ ) +epsilon_2_ ) )
                found = true;
            else
            {
                double na = *a_ + h(0);
                double nb = *b_ + h(1);
                double nc = *c_ + h(2);
                
                double rho =( F(*a_, *b_, *c_) - F(na, nb, nc) )  / L0_L(h);

                if( rho > 0)
                {
                    *a_ = na;
                    *b_ = nb;
                    *c_ = nc;
                    calcJ_fx();
                    calcH_g();
                                      
                    found = ( g_.lpNorm<Eigen::Infinity>() < epsilon_1_ );
                    mu = mu * std::max<double>(0.33, 1 - std::pow(2*rho -1, 3));
                    nu = 2.0;
                }
                else
                {
                    mu = mu * nu; 
                    nu = 2*nu;
                }// if rho > 0
            }// if step is too small
            
            t.stop();
            if( is_out_ )
            {
                std::cout << "Iter: " << std::left <<std::setw(3) << k << " Result: "<< std::left <<std::setw(10)  << *a_ << " " << std::left <<std::setw(10)  << *b_ << " " << std::left <<std::setw(10) << *c_ << 
                " step: " << std::left <<std::setw(14) << h.norm() << " cost: "<< std::left <<std::setw(14)  << getCost() << " time: " << std::left <<std::setw(14) << t.duration()  <<
                " total_time: "<< std::left <<std::setw(14) << (sumt += t.duration()) << std::endl;
            }   
        } // while
        
        if( found  == true)
            std::cout << "\nConverged\n\n";
        else
            std::cout << "\nDiverged\n\n";
        
    }//function 
    
    
    
    Eigen::MatrixXd fx_; 
    Eigen::MatrixXd J_; // 雅克比矩阵
    Eigen::Matrix3d H_; // H矩阵
    Eigen::Vector3d g_;
    
    std::vector< Eigen::Vector2d> obs_; // 观测
   
   /* 要求的三个参数 */
   double* a_, *b_, *c_;
    
    /* parameters */
    double epsilon_1_, epsilon_2_;
    int max_iter_;
    bool is_out_;
};//class LevenbergMarquardt
int main(int argc, char **argv) {
    const double aa = 0.1, bb = 0.5, cc = 2; // 实际方程的参数
    double a =0.0, b=0.0, c=0.0; // 初值
    
    /* 构造问题 */
    LevenbergMarquardt lm(&a, &b, &c);
    lm.setParameters(1e-10, 1e-10, 100, true);
    
    /* 制造数据 */
    const size_t N = 100; //数据个数
    cv::RNG rng(cv::getTickCount());
    for( size_t i = 0; i < N; i ++)
    {
        /* 生产带有高斯噪声的数据　*/
        double x = rng.uniform(0.0, 1.0) ;
        double y = exp(aa*x*x + bb*x + cc) + rng.gaussian(0.05);
        
        /* 添加到观测中　*/
        lm.addObservation(x, y);
    }
    /* 用LM法求解 */
    lm.solve();
    
    return 0;
}
```
### 4、相机标定的步骤

(1)、准备一个张正友标定法的棋盘格，棋盘格大小已知，用相机对其进行不同角度的拍摄，得到一组图像；

(2)、对图像中的特征点如标定板角点进行检测，得到标定板角点的像素坐标值，根据已知的棋盘格大小和世界坐标系原点，计算得到标定板角点的物理坐标值；

(3)、求解内参矩阵与外参矩阵。
根据物理坐标值和像素坐标值的关系，求出 $H$ 矩阵，进而构造 $v$ 矩阵，求解 $B$ 矩阵，利用 $B$ 矩阵求解相机内参矩阵 $A$ ，最后求解每张图片对应的相机外参矩阵 $\begin{bmatrix}R&T \\ 0&1\\ \end{bmatrix}$ ；

(4)、求解畸变参数。
利用 $\hat{u},u,\hat{v},v$ 构造 $D$ 矩阵，计算径向畸变参数；

(5)、利用 L-M（Levenberg-Marquardt）算法对上述参数进行优化。

**这是相机标定的代码[Camera_calibration](https://github.com/SHUNLU-1/Camera_calibration.git)**
