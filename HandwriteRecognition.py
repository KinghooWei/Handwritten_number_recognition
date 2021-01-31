import cv2
from numpy import *
import os
import operator


def main():
    if os.path.exists('labels.npy') & os.path.exists('trainingMat.npy'):
        labels = load('labels.npy')
        trainingMat = load('trainingMat.npy')
        print(labels)
        print(trainingMat)
    else:
        labels, trainingMat = createTrainSet()
        save('labels.npy', labels)
        save('trainingMat.npy', trainingMat)

    cap = cv2.VideoCapture(0)  # 开摄像头
    while 1:
        ret, frame = cap.read()  # 读视频帧
        img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ret, img_bin = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)  # 二值化

        # 闭操作
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
        bin_close = cv2.morphologyEx(img_bin, cv2.MORPH_CLOSE, kernel)

        contours, hierarchy = cv2.findContours(bin_close, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # 获取连通区域
        for cnt in contours:  # 外接矩形
            x, y, width, height = cv2.boundingRect(cnt)
            if width <= height & height > 40:
                img = bin_close[y:y + height, x:x + width]
                # img = skewCorrection(img)
                img = cv2.resize(img, (32, 32), interpolation=cv2.INTER_CUBIC)
                imgFeature = get_feature(img)
                classifyResult = sort(imgFeature, trainingMat, labels, 7)
                frame = cv2.putText(frame, str(classifyResult), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 2)

                cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 0, 255), 1)

        # cv2.imshow("bin", img_bin)
        # cv2.imshow("binOpen", bin_close)
        cv2.imshow("capture", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


# 倾斜校正
def skewCorrection(img):
    moments = cv2.moments(img)
    skew = moments['mu11'] / moments['mu02']
    if abs(moments['mu02']) < 1e-2:
        return img.copy()
    M = float32([[1, skew, -0.5 * 28 * skew], [0, 1, 0]])
    img_out = cv2.warpAffine(img, M, (28, 28), flags=cv2.WARP_INVERSE_MAP | cv2.INTER_LINEAR)
    return img_out


# 裁剪伸缩
def crop(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    x, y, w, h = cv2.boundingRect(contours[0])
    img_crop = img[y:y + h, x:x + w]
    imgOut = cv2.resize(img_crop, (32, 32), interpolation=cv2.INTER_CUBIC)
    return imgOut


# 提取特征
def get_feature(img):
    feature = []
    for i in range(32):
        for j in range(32):
            if img[i, j] == 0:
                pixel = 0
            else:
                pixel = 1
            feature.append(pixel)
    return feature


# 由图像名称得到数字类别
def getNumLabel(file_name):
    fileStr = file_name.split('.')[0]  # 根据文件名中的字符"."进行切片
    numLabel = int(fileStr.split('_')[0])  # 根据文件切片结果中的"_"进行再次切片
    return numLabel


# 构建训练集
def createTrainSet():
    labels = []
    fileList = os.listdir('numberDigits/image/trainingSet')
    m = len(fileList)
    trainingMat = zeros((m, 1024))
    for i in range(m):
        fileName = fileList[i]
        labels.append(getNumLabel(fileName))
        ori = cv2.imread('numberDigits/image/trainingSet/%s' % fileName)  # 读取训练样本
        img_gray = cv2.cvtColor(ori, cv2.COLOR_BGR2GRAY)
        ret, img_bin = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)  # 二值化
        img = skewCorrection(img_bin)  # 倾斜校正
        img = crop(img)
        trainingMat[i, :] = get_feature(img)
    return labels, trainingMat


# KNN算法
def sort(imgFeature, trainingMat, labels, k):
    trainingSetSize = trainingMat.shape[0]
    diffMat = tile(imgFeature, (trainingSetSize, 1)) - trainingMat
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)  # 每一行上元素之和
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()    # 从小到大排序，返回下标
    classCount = {}
    for i in range(k):
        voteLabel = labels[sortedDistIndicies[i]]  # 距离第i小的训练样本的类型
        classCount[voteLabel] = classCount.get(voteLabel, 0) + 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


if __name__ == '__main__':
    main()
