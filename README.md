# Handwritten_number_recognition
Video handwritten digit recognition based on k-NN algorithm 基于k-NN算法的视频手写数字识别

## 一、github

[https://github.com/KinghooWei/Handwritten_number_recognition](url)

开门见山了，记得**star一下**呀！

## 二、最终效果图

![最终效果图](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/863afe3f4e7140928fd3d397f8e2cdfc~tplv-k3u1fbpfcp-watermark.image)

## 三、设计思路

编程环境为python3.7.7，编译器使用pycharm2019.3.4 x64。程序开启电脑摄像头，读取视频帧，对每帧图像进行二值化处理、获取连通区域，通过设定连通区域的最小内接矩形的最小高度和长宽比范围，筛选合适的连通区域从而完成对手写数字的定位，接着通过k-NN算法对手写数字进行分类识别，实时在视频中显示识别结果。

### 手写数字定位

- **闭操作**

在定位手写数字前，要先对连通区域做闭操作。有时光线太强，笔画太细，会造成视频帧中的手写数字笔画断裂，对连通区域进行闭操作可以将间隙连接起来。

闭操作可使轮廓线更光滑，通常用来消弥狭窄的间断和长细的鸿沟，消除小的空洞，并填补轮廓线中的断裂。使用结构元素B对集合A的闭操作就是用B对A进行膨胀，然后用B对结果进行腐蚀，公式如下：

$$ A \cdot B = (A \oplus B) \ominus B $$

- **定位**

通过设定连通区域的最小内接矩形的最小高度和长宽比范围，筛选出合适的连通区域，从而完成对手写数字的定位。项目采取的最小高度为60个像素，宽高比小于1。

### 特征描述

把定位后的连通区域的最小正接矩形的二值图像调整为32\*32像素的二值图像，逐行读取像素值，从而得到1024维向量，此向量作为手写数字的特征。

由于训练样本的手写数字有各种角度不同程度的倾斜，因此在特征提取描述之前还对训练样本进行了倾斜校正。

### k-NN算法

在模式识别领域中，k-NN算法是一种用于分类和回归的非参数统计方法。在k-NN分类算法中，输入包含k个最接近的特征空间的训练样本，输出是一个分类族群。一个对象的分类是由其邻近样本占多数的类别确定的，k为正整数，通常为奇数。k个最邻近样本中最多的分类类别决定了赋予该对象的类别，若$k = 1$，则该对象的类别直接由最近的一个节点赋予。

k-NN算法是所有的机器学习算法中最简单的之一。k个最邻近样本都是已经正确分类的对象，虽然没要求明确的训练步骤，但这也可以当作是此算法的一个训练样本集。训练样本是多维特征空间向量，其中每个训练样本带有一个类别标签。算法的训练阶段只包含存储的特征向量和训练样本的标签。k-NN算法的缺点是对数据的局部结构非常敏感。

在分类阶段，k是一个常数，项目中选取$k = 7$。

一般情况下，可以用欧氏距离作为距离度量。在欧几里得空间中，点$x = (x_1,x_2,...,x_n)$和点$y = (y_1,y_2,...,y_n)$之间的欧式距离为

$$d(x,y) = \sqrt{(x_1-y_1)^2+(x_2-y_2)^2+...+(x_n-y_n)^2}$$

k-NN算法分类会在类别分布不均时出现缺陷，也就是说，出现频率较多的样本将会影响测试样本的预测结果。因为样本更多的类别更可能出现在测试点的K邻域，而测试点的属性又是通过k邻域内的样本计算出来的。解决这个缺点的方法之一是在进行分类时将样本到k个近邻点的距离考虑进去。k近邻点中每一个的分类都乘以与测试点之间距离的成反比的权重。

## 四、改进和结果

![改进前效果图](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/7f4add90a0f64043834d999240eaf46b~tplv-k3u1fbpfcp-watermark.image)

改进前效果图如上，准确率很一般，原因可能有一下几点：

- k-NN算法所用的训练样本少，每个数字的训练样本只有10个；

- 手写数字没有统一规范，加大了难度；

- 选择的特征描述方法有待改进，用的是模式识别课程提到的方法，把数字图像调整为32\*32像素的二值图像，逐行读取像素值，从而得到1024维向量。这种描述方法不够直观，对书写规范要求比较高，如果采用笔画走势、端点特征等作为特征，效果可能会更好；

- k-NN算法本身存在缺陷，它把特征距离最近的7个训练样本的分类作为分类依据，不仅舍弃了其余样本，而且把这7个样本看的同等重要，按数量作为分类依据，这显然不甚合理。改进的办法可以增加权重，把距离的倒数作为权重，或者更换其他分类算法。

根据第2个原因，将训练样本替换为书写较为规范的样本，得到的最终识别效果如下，可以看到识别能力有所提高，但这样对书写规范的要求同样也有所提高。

![最终效果图](https://p6-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/759e809399f14e6abd6ebb2476dabb40~tplv-k3u1fbpfcp-watermark.image)

## 五、参考
[OpenCV+python调用摄像头](https://blog.csdn.net/weixin_39272225/article/details/79931882?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522158503782819725211937107%2522%252C%2522scm%2522%253A%252220140713.130056874..%2522%257D&request_id=158503782819725211937107&biz_id=0&utm_source=distribute.pc_search_result.none-task)

[OpenCV-Python 图像二值化](https://blog.csdn.net/hedgehog__/article/details/104199805?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522158522576219725219919436%2522%252C%2522scm%2522%253A%252220140713.130056874..%2522%257D&request_id=158522576219725219919436&biz_id=0&utm_source=distribute.pc_search_result.none-task)

[python画出最小外接矩形及其中心点](https://blog.csdn.net/zhou4411781/article/details/103159158?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522158522844619195162546213%2522%252C%2522scm%2522%253A%252220140713.130056874..%2522%257D&request_id=158522844619195162546213&biz_id=0&utm_source=distribute.pc_search_result.none-task)

[Python+OpenCV 开闭操作](https://blog.csdn.net/Acmer_future_victor/article/details/104160441?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522158528274319195162504405%2522%252C%2522scm%2522%253A%252220140713.130056874..%2522%257D&request_id=158528274319195162504405&biz_id=0&utm_source=distribute.pc_search_result.none-task)

[python调节图片尺寸大小](https://blog.csdn.net/weixin_45334587/article/details/104391403?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522158530125119724845025249%2522%252C%2522scm%2522%253A%252220140713.130056874..%2522%257D&request_id=158530125119724845025249&biz_id=0&utm_source=distribute.pc_search_result.none-task)

[python cv2图片剪裁](https://blog.csdn.net/FormatFa/article/details/80353235?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522158530157519724839255983%2522%252C%2522scm%2522%253A%252220140713.130056874..%2522%257D&request_id=158530157519724839255983&biz_id=0&utm_source=distribute.pc_search_result.none-task)

[python openCV 获取图像像素点](https://blog.csdn.net/qq_42265536/article/details/104054342?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522158530277019724811849490%2522%252C%2522scm%2522%253A%252220140713.130056874..%2522%257D&request_id=158530277019724811849490&biz_id=0&utm_source=distribute.pc_search_result.none-task)

[基于python的手写数字识别（KNN算法）](https://blog.csdn.net/waitting_for_youth/article/details/74122838?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522158503301119725256715844%2522%252C%2522scm%2522%253A%252220140713.130056874..%2522%257D&request_id=158503301119725256715844&biz_id=0&utm_source=distribute.pc_search_result.none-task)

[Python numpy数据的保存和读取](https://blog.csdn.net/ctwy291314/article/details/88951073?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522158531769619725256712328%2522%252C%2522scm%2522%253A%252220140713.130056874..%2522%257D&request_id=158531769619725256712328&biz_id=0&utm_source=distribute.pc_search_result.none-task)

[python 判断文件是否存在](http://www.tjunk.club/?p=415)

[python数字转字符串](https://blog.csdn.net/yuanren201/article/details/88652680)