# Handwritten_number_recognition
Video handwritten digit recognition based on k-NN algorithm 基于k-NN算法的视频手写数字识别
华南理工大学模式识别实践

记得**star一下**呀！

README只列了框架，详情可以跳转[https://juejin.cn/post/6923916531965362184](https://juejin.cn/post/6923916531965362184)

## 最终效果图

![最终效果图](https://p3-juejin.byteimg.com/tos-cn-i-k3u1fbpfcp/863afe3f4e7140928fd3d397f8e2cdfc~tplv-k3u1fbpfcp-watermark.image)

## 设计思路

编程环境为python3.7.7，编译器使用pycharm2019.3.4 x64。程序开启电脑摄像头，读取视频帧，对每帧图像进行二值化处理、获取连通区域，通过设定连通区域的最小内接矩形的最小高度和长宽比范围，筛选合适的连通区域从而完成对手写数字的定位，接着通过k-NN算法对手写数字进行分类识别，实时在视频中显示识别结果。

### 手写数字定位

- **闭操作**

- **定位**

### 特征描述

### k-NN分类算法

## 改进和结果

## 参考
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