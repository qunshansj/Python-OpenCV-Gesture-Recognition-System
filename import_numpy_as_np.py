
import numpy as np
import cv2
imname = "6358772.jpg"
# 读入图像
'''
使用函数 cv2.imread() 读入图像。这幅图像应该在此程序的工作路径，或者给函数提供完整路径.
警告：就算图像的路径是错的，OpenCV 也不会提醒你的，但是当你使用命令print(img)时得到的结果是None。
'''
img = cv2.imread(imname, cv2.IMREAD_COLOR)
'''
imread函数的第一个参数是要打开的图像的名称(带路径)
第二个参数是告诉函数应该如何读取这幅图片. 其中
cv2.IMREAD_COLOR 表示读入一副彩色图像, alpha 通道被忽略, 默认值
cv2.IMREAD_ANYCOLOR 表示读入一副彩色图像
cv2.IMREAD_GRAYSCALE 表示读入一副灰度图像
cv2.IMREAD_UNCHANGED 表示读入一幅图像，并且包括图像的 alpha 通道
'''
# 显示图像
'''
使用函数 cv2.imshow() 显示图像。窗口会自动调整为图像大小。第一个参数是窗口的名字，
其次才是我们的图像。你可以创建多个窗口，只要你喜欢，但是必须给他们不同的名字.
'''
cv2.imshow("image", img) # "image" 参数为图像显示窗口的标题, img是待显示的图像数据
cv2.waitKey(0) #等待键盘输入,参数表示等待时间,单位毫秒.0表示无限期等待
cv2.destroyAllWindows() # 销毁所有cv创建的窗口
# 也可以销毁指定窗口:
#cv2.destroyWindow("image") # 删除窗口标题为"image"的窗口
# 保存图像
'''
使用函数 cv2.imwrite() 来保存一个图像。首先需要一个文件名，之后才是你要保存的图像。
保存的图片的格式由后缀名决定.
'''
#cv2.imwrite(imname + "01.png", img)
cv2.imwrite(imname + "01.jpg", img)
